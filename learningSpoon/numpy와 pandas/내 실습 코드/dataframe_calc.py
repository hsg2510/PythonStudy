from pandas import DataFrame
import pandas as pd

df = pd.read_csv("../TSLA.csv", index_col=0)

#시가가 250 이상일때, 종가와 거래량 가져오기
print(df[df > 250]) #조건이 False인 값이 NaN으로 나타나기 때문에, 이렇게 DataFrame에 바로 조건식을 잘 사용하지 않는다.

cond = df['Open'] > 250 #Series객체에 조건식 계산
print(cond)
print(df.loc[cond])
print(df[cond])

target = ['Close', 'Volume']
temp = df[target]
print(temp)

print(df[cond][target])

#시가 250 이상일 때의 거래량의 합을 출력하라.
cond = df['Open'] > 250
volume_series = df[cond]['Volume']
print(volume_series)
print(sum(volume_series)) #파이썬 빌트인 함수
print(volume_series.sum()) #Series객체 메서드

#종가가 가장 높은 날의 날짜를 출력하라.
close_series = df['Close']
max_close = close_series.max()
cond = (close_series == max_close)
print(close_series[cond])
print(close_series[cond].index)
print(close_series[cond].index[0])

print(close_series.idxmax()) #series의 데이터중 max값인 index를 return
print(close_series.idxmin()) #min인 index

#주식 데이터 사용
"""
from pykrx import stock

df = stock.get_market_ohlcv_by_date("20200101", "20200731", "005930") #open, high, low, close, volume
print(df.head(5)) #상위 5개의 값만 출력

#삼성전자의 가장 낮은, 높은 가격 날짜는?
print(df['고가'].idxmax())
print(df['저가'].idxmin())

#최고가와 최저가의 차이는?
gap = df['고가'].max() - df['저가'].min()
print(gap)
"""
#컬럼 추가
df = pd.read_csv("../TSLA.csv", index_col=0)
s = df['Open'] + 100
df['OpenPlus100'] = s
print(df)

#컬럼 삭제
#-메서드 사용
df_delete = df.drop('OpenPlus100', axis=1) #DataFrame은 가로, 세로축이 있기 때문에 축 정보를 넣어줘야 한다. '0' = index, '1' = column 정보, 기본값은 0
print(df_delete)
#-슬라이싱으로 사용
df_delete = df[ df.columns[:-1]]
print(df_delete)

#로우 추가 및 삭제
df.loc['2019-07-19'] = [100, 200, 300, 400, 500, 600, 700]
print(df)
print(df.columns)

df = df[df.columns[:4]]
print(df)

df.loc['abc'] = [10, 20, 30, 40]
print(df)
df = df.drop('abc', axis=0)
print(df)

#warning
pointerDf = df[:2][:2]
print(pointerDf)
pointerDf.iloc[1][0] = 2 #이러면 원본인 df 까지 변경된다. 그러나 값을 변경하는거니까 warning 안뜸(python 3.8기준)
print(pointerDf)
print(df)
"""
pointerDf = df[['Open', 'High']]
print(pointerDf)
pointerDf['New'] = 20 #이러면 원본인 df 까지 변경됨. 원본의 Column을 추가하는 것이기 때문에, warning 뜨고 원본 변경하지 않음(python3.8 기준)
print(pointerDf)
print(df)
"""
pointerDf = df[['Open', 'High']].copy()
pointerDf['New'] = 20 #copy() 메서드로 가져와서 컬럼 추가하는 것이기 때문에, 경고 안뜸.
print(pointerDf)
print(df)

#데이터 프레임 이어 붙이기
import numpy as np

df1 = DataFrame(np.arange(6).reshape(2, 3))
print(df1)
df2 = DataFrame(np.arange(6, 12).reshape(2, 3))
print(df2)
df = pd.concat([df1, df2], axis=1) #axis=1 이면 컬럼 방향으로 합침, 이러면 index들이 같아야 함.
print(df)
df = pd.concat([df1, df2], axis=0) #axis=0 이면 인덱스 방향으로 합침, 이러면 column들이 같아야 함.
print(df)