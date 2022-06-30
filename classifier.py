import json as j
import pandas as pd
import re
import numpy as np

from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2


def classify(train_file, target_names):
    json_data = None
    with open(train_file) as data_file:
        lines = data_file.readlines()
        joined_lines = "".join(lines)

        json_data = j.loads(joined_lines)

    data = pd.DataFrame(json_data)

    stemmer = SnowballStemmer('english')

    words = stopwords.words("english")

    data['cleaned'] = data['adTitle'].apply(lambda x: " ".join([stemmer.stem(
        i) for i in re.sub("[^a-zA-Z]", " ", x).split() if i not in words]).lower())

    x_train, x_test, y_train, y_test = train_test_split(
        data['cleaned'], data.type, test_size=0.2)

    pipeline = Pipeline([('vect', TfidfVectorizer(ngram_range=(1, 3), stop_words="english", sublinear_tf=True)),
                        ('chi',  SelectKBest(chi2, k=10000)),
                        ('clf', LinearSVC(C=1.0, penalty='l1', max_iter=3000, dual=False))])

    model = pipeline.fit(x_train, y_train)

    vectorizer = model.named_steps['vect']
    chi = model.named_steps['chi']
    clf = model.named_steps['clf']

    feature_names = vectorizer.get_feature_names()
    feature_names = [feature_names[i] for i in chi.get_support(indices=True)]
    feature_names = np.asarray(feature_names)

    print("top 10 keywords per class:")
    for i, label in enumerate(target_names):
        top10 = np.argsort(clf.coef_[i])[-10:]
        print("%s: %s" % (label, " ".join(feature_names[top10])))

    print("accuracy score: " + str(model.score(x_test, y_test)))

    return model


model = classify(train_file='./data/train_disk.json', target_names=['REPRO', 'NOT_A_GAME', 'BUNDLE', 'GRADED', 'SEALED', 'CIB', 'BOX_AND_GAME',
                                                                    'MANUAL_AND_GAME', 'BOX', 'MANUAL', 'BOX_AND_MANUAL', 'GAME'])


print(model.predict(
    ['Conflicto: tormenta Del Desierto | Playstation PS2 | completo | PAL']))
