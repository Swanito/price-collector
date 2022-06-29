from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from datetime import datetime
from os import listdir
from os import environ

import pandas as pd
import json as json
import pymongo

mongo_uri = environ["MONGODB_URI"]
mongoClient = pymongo.MongoClient(mongo_uri)
database = mongoClient["testdb"]
collection = database["games-raws"]


def collect(path):
    with open('./input-files/'+path, 'r') as dc:
        data = json.load(dc)

    driver_path = './chromedriver_linux'
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(driver_path, options=options)

    driver.get('https://www.ebay.es')

    now = datetime.now()
    date = now.strftime('%d-%m-%Y')

    for game in data['games']:
        print('Searching '+game)
        stored_game = collection.find({"game": game, "sampleDate": date})

        buttons = driver.find_elements(By.CSS_SELECTOR, '#gdpr-banner-accept')
        for button in buttons:
            button.click()

        if len(list(stored_game)) == 0:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#gh-ac'))).clear()

            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#gh-ac'))).send_keys(game + ' ' + data['platform'])

            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#gh-btn'))).click()

            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#x-refine__group__4 > .x-refine__main__value > :nth-child(4)'))).click()

            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.x-refine__main__value > [name="LH_Sold"]'))).click()

            items = driver.find_elements(By.CSS_SELECTOR, 'li.s-item')

            for item in items:
                timestamp = datetime.timestamp(now)
                item_info = {}
                item_info['game'] = game
                item_info['platform'] = data['platform']
                item_info['sampleTimestamp'] = timestamp
                item_info['sampleDate'] = date

                title_element = item.find_elements(
                    By.CSS_SELECTOR, '.s-item__title')
                price_element = item.find_elements(
                    By.CSS_SELECTOR, '.s-item__price')
                shipping_element = item.find_elements(
                    By.CSS_SELECTOR, '.s-item__shipping')
                secondary_element = item.find_elements(
                    By.CSS_SELECTOR, 'div.s-item__subtitle > span.SECONDARY_INFO')
                selling_date_element = item.find_elements(
                    By.CSS_SELECTOR, '.s-item__title--tagblock > span.POSITIVE')
                location_element = item.find_elements(
                    By.CSS_SELECTOR, '.s-item__location')
                if len(title_element) > 0:
                    item_info['adTitle'] = title_element[0].text
                if len(price_element) > 0:
                    item_info['price'] = price_element[0].text
                if len(shipping_element) > 0:
                    item_info['shipping'] = shipping_element[0].text
                if len(secondary_element) > 0:
                    item_info['secondaryInfo'] = secondary_element[0].text
                if len(selling_date_element) > 0:
                    item_info['sellingDate'] = selling_date_element[0].text
                if len(location_element) > 0:
                    item_info['location'] = location_element[0].text

                if item_info['price'] != '':
                    collection.insert_one(item_info)
                    print(game + ' sample stored!')
        else:
            print(game+' is already stored')


files = listdir('./input-files')
for file in files:
    print('Current file '+file)
    collect(file)
