# 1. leer todos los raw del dia anterior
# 2. agruparlos por plataforma
# 3. agruparlos por juego
# 4. agruparlos por tipo
# 5. calcular el precio mediano para cada tipo de cada juego de cada plataforma
# 6. calcular el envío mediano para cada tipo de cada juego de cada plataforma
# 7. guardarlo en bbdd con la misma estructura que lo existente
# NOTAS:
# no importa la location
#
import pymongo
import statistics
import sys
from scipy import stats
from datetime import datetime, timedelta
from os import environ
import blacklist

mongo_uri = environ["MONGODB_URI"]
mongoClient = pymongo.MongoClient(mongo_uri)
database = mongoClient["testdb"]
raw_collection = database["games-raws"]
processed_collection = database["games-processeds"]


def get_unique_games_from_list(records):
    return {record["game"] for record in records}


def get_unique_types_from_list(records):
    return {record["type"] for record in records}


def get_prices_from_samples(records):
    return [record["price"] for record in records]


def get_samples_from_list(records, game):
    return [x for x in records if x["game"] == game]


def get_games_from_platform(records, platform):
    return [x for x in records if x["platform"] == platform]


def get_samples_for_type(records, type):
    return [x for x in records if x["type"] == type]


def get_date():
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    return yesterday.strftime('%d-%m-%Y')


def get_last_records():
    return raw_collection.find({"sampleDate": get_date(), 'isProcessed': {'$ne': True}, "type": {'$nin': [None, 'NOT_A_GAME', 'BUNDLE', 'PC']}})


def format_prices(samples):
    array = []
    for sample in samples:
        format_string = sample.replace('GBP ', '')
        format_string = format_string.replace('USD', '')
        format_string = format_string.split()[0]
        format_string = format_string.replace('.', '')
        format_string = format_string.replace(',', '.')
        array.append(float(format_string))
    array.sort()
    array = stats.trim1(array, 0.25, 'left')
    array = stats.trim1(array, 0.25, 'right')
    return array


def remove_blacklisted_from_samples(records, platform):
    blacklisted_words = blacklist.get_blacklist(platform=platform)
    return [x for x in records if any(w not in x["adTitle"] for w in blacklisted_words)]


records = get_last_records()

platforms = sys.argv[1].split(',')

print('Processing from date -> ' + get_date())
print('Processing platforms: ')
print(platforms)
for platform in platforms:
    print('Starting processing ' + platform)
    games = get_games_from_platform(records=records, platform=platform)
    unique_games = get_unique_games_from_list(records=games)
    for unique in unique_games:
        samples = get_samples_from_list(records=games, game=unique)
        samples = remove_blacklisted_from_samples(
            records=samples, platform=platform)
        types = get_unique_types_from_list(records=samples)
        for type in types:
            if type != 'NOT_A_GAME' and type != 'BUNDLE' and type != 'PC':
                samples_for_type = get_samples_for_type(
                    records=samples, type=type)
                prices_from_samples = get_prices_from_samples(samples_for_type)
                if len(prices_from_samples) > 0:
                    prices_from_samples = format_prices(prices_from_samples)
                    object = {
                        'name': unique,
                        'date': get_date(),
                        'platform': platform,
                        'type': type,
                        'timestamp': datetime.timestamp(datetime.now()),
                        'prices': {
                            'soldUnits': len(prices_from_samples),
                            'maxPrice': max(prices_from_samples),
                            'minPrice': min(prices_from_samples),
                            'medianPrice': statistics.median(prices_from_samples)
                        }
                    }
                    processed_collection.insert_one(object)
                    for sample in samples:
                        raw_collection.delete_one({'_id': sample['_id']})

    print('Finished processing ' + platform)
