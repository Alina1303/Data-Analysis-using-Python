# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cphcCJ5RLhSLz4vjg8xSCFj6z5SEixC2

**Загрузка библиотек**
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

"""**Загрузка датасета**"""

data = pd.read_csv('https://raw.githubusercontent.com/sanyathisside/Predicting-Heart-Disease-using-Machine-Learning/master/heart-disease.csv')
data.head()

"""**Подготовка данных**"""

X = data.drop(['target'], axis=1)
y = data['target']

"""Разделение данных на тренировочные и тестовые"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)

"""**Обучение с помощью метода Random Forest**"""

np.random.seed(0)
clf_rf =  RandomForestClassifier(10, max_depth=5)
clf_rf.fit(X_train, y_train)

"""**Предсказание**"""

prediction = clf_rf.predict(X_test)
prediction

"""**Расчёт важности переменных для классификации**

*Расчет точност и модели*
"""

clf_rf.score(X_test, y_test)

"""*Сортировка по важности переменных с визуадизацией*"""

feature_importances = clf_rf.feature_importances_
feature_importances_df = pd.DataFrame(clf_rf.feature_importances_, index=X_train.columns, columns=['importance'])
feature_importances_df.sort_values('importance').plot(kind='barh', figsize=(12, 8))