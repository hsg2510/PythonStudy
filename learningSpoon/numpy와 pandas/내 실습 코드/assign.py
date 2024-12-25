import numpy as np

#ndarray의 대입 연산은 전체 데이터에 적용됨
a = np.arange(5)
a[2] = 0
print(a) #[0 1 0 3 4]
a = 0
print(a) #0 -> a는 adarray가 아니라 정수 type이 된다.
a = np.arange(5)
a[:] = 0
print(a) # [0 0 0 0 0]
a = np.arange(5)
a[[1, 3]] = 0 #불연속 된 위치에 값 대입
print(a) #[0 0 2 0 4]

a = np.arange(9).reshape(3, 3)
a[ [0, 2] ] = 0
print(a) #[[0 0 0] [3 4 5] [0 0 0]]
a = np.arange(9).reshape(3, 3)
a[0:2, 0:2] = 0
print(a) #[[0 0 2] [0 0 5] [6 7 8]]

#조건문 대입
a = np.arange(5)
a[a>2] = 0
print(a) #[0 1 2 0 0]

a = np.arange(9).reshape(3, 3)
a = np.where(a > 4, 10, a) # a>4인 경우 10을 대입, 그렇지 않으면 그대로 유지
print(a) #[[0 1 2] [3 4 10] [10 10 10]]

a = np.arange(9).reshape(3, 3)
a = np.where(a > 4, 10, 0) # a>4인 경우 10을 대입, 그렇지 않으면 0 대입
print(a) #[[0 0 0] [0 0 10] [10 10 10]]