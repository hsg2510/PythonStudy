import numpy as np

#브로드캐스팅 기능 : 하나의 연산이 전체 데이터에 대해 적용 됨
a = np.arange(4)
print(a*3) #[0 3 6 9]
b = np.arange(4, 8) #[4 5 6 7]
print(a + b) #[4 6 8 10]

print(b.mean()) #평균계산 -> 5.5
print(b.var()) #분산 계산 -> (x - 평균)^2의 평균 -> 1.25

점수 = [30, 25, 66, 23, 44, 23]
a = np.arra y(점수).reshape(2, 3)
print(a.var(axis=0))

""" 
numpy의 수치연산 함수 
-mean()
-max()
-min()
-median()
-prod()
-cumprod()
-cumsum()
-np.abs()
-np.square()
"""
