from pandas import DataFrame

#딕셔너리 - 컬럼
딕셔너리 = {
    "시가" : [ 960, 200, 300 ],
    "고가" : [ 990, 300, 500 ],
    "저가" : [ 920, 180, 300 ],
    "종가" : [ 930, 180, 400 ]
}

인덱스 = ["비트코인", "리플", "이더리움"]
df = DataFrame(data=딕셔너리, index=인덱스)

print(df)

#리스트 - 로우
데이터 = [
    [980, 990, 920, 930],
    [200, 300, 180, 180],
    [300, 500, 300, 400]
]
columns = ["시가", "고가", "저가", "종가"]
df = DataFrame(data=데이터, columns=columns)
print(df)

#딕셔너리+리스트 - 로우
리스트 = [
    {"시가" : 900, "고가" : 990, "저가" : 920, "종가" : 930},
    {"시가" : 200, "고가" : 300, "저가" : 180, "종가" : 180},
    {"시가" : 380, "고가" : 500, "저가" : 300, "종가" : 400}
]
df = DataFrame(data=리스트)
print(df)


#csv 읽고 쓰기
import pandas as pd

df = pd.read_csv("../TSLA.csv")
print(df)
df.to_csv("out.csv")


