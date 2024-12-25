import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, make_scorer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

### remove null
def fillna(df):
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    df['Cabin'] = df['Cabin'].fillna('N')
    df['Embarked'] = df['Embarked'].fillna('N')
    df['Fare'] = df['Fare'].fillna(0)

    return df

### drop unnecessary columns
def drop_features(df):
    df = df.drop(['PassengerId', 'Name','Ticket'], axis=1)

    return df

### encoding to number
def format_features(df):
    df['Cabin'] = df['Cabin'].str[:1]
    features = ['Cabin', 'Sex', 'Embarked']

    for feature in features:
        label_encoder = LabelEncoder()
        df[feature] = label_encoder.fit_transform(df[feature])
    
    return df

### cal accuracy, precision, recall, f1 
def get_clf_eval(y_test, pred):
    accuracy = accuracy_score(y_test, pred)
    precision = precision_score(y_test, pred)
    recall = recall_score(y_test, pred)
    f1 = f1_score(y_test, pred)

    return accuracy, precision, recall, f1

titanic_df = pd.read_csv('titanic_train.csv')
titanic_df = fillna(titanic_df)
titanic_df = drop_features(titanic_df)
titanic_df = format_features(titanic_df)


def evaluate_model(parameters, x_train, x_test, y_train, y_test):
    # 파라미터에 따라 모델 설정
    model = LogisticRegression(solver='liblinear', random_state=42,
                               penalty=parameters['classifier__penalty'],
                               C=parameters['classifier__C'],
                               fit_intercept=parameters['classifier__fit_intercept'],
                               class_weight=parameters['classifier__class_weight'])
    
    # 파이프라인 생성
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', model)
    ])
    
    # 모델 학습
    pipeline.fit(x_train, y_train)
    
    # 예측
    y_pred = pipeline.predict(x_test)
    
    # 평가 지표 계산
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    return accuracy, precision, recall, f1


### 학습, 예측, 평가
y_titanic_df = titanic_df['Survived']
x_titanic_df = titanic_df.drop('Survived', axis=1)
x_train, x_test, y_train, y_test=train_test_split(x_titanic_df, y_titanic_df, test_size=0.2)

logistic_reg = LogisticRegression(solver='lbfgs')
logistic_reg.fit(x_train, y_train)
data_predict = logistic_reg.predict(x_test)
accuracy, precision, recall, f1 = get_clf_eval(y_test, data_predict)
print('accuracy : ', accuracy)
print('precision : ', precision)
print('recall : ', recall)
print('f1 : ', f1)

### 교차 검증 및 최적 파라미터 찾기
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # 데이터 스케일링
    ('classifier', LogisticRegression(solver='liblinear', random_state=42))
])

# 하이퍼파라미터 그리드 설정
param_grid = {
    'classifier__penalty': ['l1', 'l2'],
    'classifier__C': [0.01, 0.1, 1, 10, 100],
    'classifier__fit_intercept': [True, False],
    'classifier__class_weight': [None, 'balanced']
}

# 스코어링 함수 정의
scoring = {
    'accuracy': make_scorer(accuracy_score),
    'precision': make_scorer(precision_score),
    'recall': make_scorer(recall_score),
    'f1': make_scorer(f1_score)
}

grid_cv = GridSearchCV(pipeline, param_grid, cv=5, scoring=scoring, refit='f1', verbose=1)
grid_cv.fit(x_train, y_train)
# 결과 출력
print("Best parameters for each metric:")
for metric in ['accuracy', 'precision', 'recall', 'f1']:
    print(evaluate_model(grid_cv.cv_results_['params'][grid_cv.cv_results_['rank_test_'+metric].argmin()], x_train, x_test, y_train, y_test))


