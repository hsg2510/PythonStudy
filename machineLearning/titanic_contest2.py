import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, make_scorer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import Binarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

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


### 학습, 예측, 평가
y_titanic_df = titanic_df['Survived']
x_titanic_df = titanic_df.drop('Survived', axis=1)
x_train, x_test, y_train, y_test=train_test_split(x_titanic_df, y_titanic_df, test_size=0.2, random_state=14)
# x_train, x_test, y_train, y_test=train_test_split(x_titanic_df, y_titanic_df, test_size=0.2)

logistic_reg = LogisticRegression(solver='liblinear')
logistic_reg.fit(x_train, y_train)
data_predict = logistic_reg.predict(x_test)
accuracy, precision, recall, f1 = get_clf_eval(y_test, data_predict)
print('accuracy : ', accuracy)
print('precision : ', precision)
print('recall : ', recall)
print('f1 : ', f1)


thresholds = [0.4, 0.45, 0.50, 0.55, 0.60]

def get_eval_by_threshold(y_test , pred_proba_c1, thresholds):
    # thresholds list객체내의 값을 차례로 iteration하면서 Evaluation 수행.
    for custom_threshold in thresholds:
        binarizer = Binarizer(threshold=custom_threshold).fit(pred_proba_c1) 
        custom_predict = binarizer.transform(pred_proba_c1)
        print('임곗값:',custom_threshold)
        accuracy, precision, recall, f1 = get_clf_eval(y_test , custom_predict)

        print('accuracy : ', accuracy)
        print('precision : ', precision)
        print('recall : ', recall)
        print('f1 : ', f1)


pred_proba = logistic_reg.predict_proba(x_test)
get_eval_by_threshold(y_test ,pred_proba[:,1].reshape(-1,1), thresholds )
