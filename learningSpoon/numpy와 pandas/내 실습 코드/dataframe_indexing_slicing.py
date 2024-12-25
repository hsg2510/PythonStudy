from pandas import DataFrame
import pandas as pd

df = pd.read_csv("../TSLA.csv") #index가 0, 1, 2로 자동 지정됨.
print(df)

df = pd.read_csv("../TSLA.csv", index_col=0)
print(df) #첫번째 컬림인 Date들이 index가 됨.

df = pd.read_csv("../TSLA.csv")
df = df.set_index('Date') #Date들이 index가 됨.

#컬럼 우선
print(df['High'])
print(type(df['High'])) #Series 이다.
print(df['High'].loc['2019-07-15'])
print(df['High'].iloc[0])
print(df['High']['2019-07-15'])
print(df['High'][0])

#로우 우선
df.loc['2019-07-15']
print(df.loc['2019-07-15'])
print(type(df.loc['2019-07-15'])) #Series 이다.
print(df.loc['2019-07-15'].loc['High'])
print(df.loc['2019-07-15'].iloc[1])
print(df.loc['2019-07-15']['High'])
print(df.loc['2019-07-15'][1])

print(df.iloc[0].loc['High'])
print(df.iloc[0].iloc[1])
print(df.iloc[0]['High'])
print(df.iloc[0][1])

#위에 것들은 로우 Series나 컬럼 Series를 가져온 후 하나를 선택하는데, 밑에 코드는 한번에 하나를 선택하기 때문에 더 빠르다.
print(df.loc['2019-07-15', 'High'])
print(df.iloc[0, 1])

#컬럼 우선
target = ['Open', 'High']
columns_first = df[target]
print(columns_first)
print(columns_first.iloc[:3])
print(df[target].loc["2019-07-15":"2019-07-17"])

#로우 우선
print(df.loc["2019-07-15":"2019-07-17"])
print(df.loc["2019-07-15":"2019-07-17"][['Open', 'High']])
print(df.iloc[:3][['Open', 'High']])
print(df.loc[["2019-07-15", "2019-07-16", "2019-07-17"]][['Open', 'High']])

print(df.iloc[[0, 3, 2]][['Open', 'High']])