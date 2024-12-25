import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

titanic_df = pd.read_csv('titanic_train.csv')

### remove null
# print(titanic_df.info())
titanic_df['Age'] = titanic_df['Age'].fillna(titanic_df['Age'].mean())
titanic_df['Cabin'] = titanic_df['Cabin'].fillna('N')
titanic_df['Embarked'] = titanic_df['Embarked'].fillna('N')
# print('Null count ',titanic_df.isnull().sum().sum())


### encoding to number
#print(titanic_df.dtypes[titanic_df.dtypes == 'object'].index.tolist())
#print('Cabin : ',titanic_df['Cabin'].value_counts())
titanic_df['Cabin'] = titanic_df['Cabin'].str[:1]
features = ['Cabin', 'Sex', 'Embarked']
label_encoder = LabelEncoder() 

for feature in features:
    titanic_df[feature] = label_encoder.fit_transform(titanic_df[feature])


### drop unnecessary columns
titanic_df = titanic_df.drop(['Name','Ticket'], axis=1)

y_titanic_df = titanic_df['Survived']
x_titanic_df = titanic_df.drop('Survived', axis=1)
x_train, x_test, y_train, y_test=train_test_split(x_titanic_df, y_titanic_df, test_size=0.2)
# print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
# print(titanic_df.head(5))

### 학습, 예측, 평가
decision_tree_cf = DecisionTreeClassifier()
decision_tree_cf.fit(x_train, y_train)
data_predict = decision_tree_cf.predict(x_test)
accuracy = accuracy_score(y_test, data_predict)
print('accuracy : ', accuracy)

### 교차 검증 및 최적 파라미터 찾기
grid_search_parameters = {'max_depth':[2,3,5,10], 'min_samples_split':[2,3,5], 'min_samples_leaf':[1,5,8]}
grid_cv = GridSearchCV(decision_tree_cf, param_grid=grid_search_parameters, scoring='accuracy', cv=5)
grid_cv.fit(x_train, y_train)
print('Grid 최고 score : ', grid_cv.best_score_)

best_estimator = grid_cv.best_estimator_
best_predict = best_estimator.predict(x_test)
best_accuracy = accuracy_score(y_test, best_predict)
print('best estimator score : ', best_accuracy)