import numpy as np

#비교연산의 broadcasting

a = np.arange(5)
print(a>2) # [False False False True True]

b = np.array([-1, -1, 100, 100, 100])
print(a>b) # [True True False False False]

#필터링
b = b[ [True, True, False, True, False] ]
print(b) #True인 값만 필터링 되서 가져옴 -> [-1 -1 100]
a = a[a>2] # a>2가 broadcasting 되서 boolean형 adarray 객체가 리턴될 것이고, 그러면 True인 값만 필터링되서 가져온다.
print(a) #[3 4]

#고가와 저가의 차이가 100 이상인 날의 고가를 출력하라
저가 = np.array([10, 200, 200, 400, 600])
고가 = np.array([100, 300, 400, 500, 600])
print(고가[(고가 - 저가) >= 100]) # [300 400 500]
