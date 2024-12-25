import numpy as np

a = np.random.randint(4) # 0 ~ 3
a = np.random.randint(10, 20) # 10 ~ 19
a = np.random.randint(10, 20, size = (2, 2)) #2행 2열 ndarray 생성
a = np.random.choice(np.arange(4), size = (4, 1)) # 4행 1열 ndarray를 생성 하는데, 월소는 0~3중에 랜덤으로 생성한다.
a = np.random.choice(np.arange(10), size = 5, replace = False) # 1차월 배열 5개짜리 ndarray를 생성 하는데, 0~9 사이에서 중복 안되게 생성.
print(a)
print(type(a))

x = np.linspace(0, 10, 3) # 시작, 끝, 분할개수 -> 0~에서 10까지 정확히 3등분 한다. : [0. 5. 10]
print(x)

y = []
for val in x:
    y.append(val ** 2) # 제곱
print(y)


# 인덱싱, 슬라이싱 기본(파이썬의 리스트와 거의 똑같음)
a = np.arange(5)
print(type(a)) #ndarray type

print(a[0]) # 0
print(a[-1]) # 4
a = np.arange(9).reshape(3, 3)
print(len(a)) #3
print(a[0][1]) #1
print(a[0, 1]) #1
#list를 슬라이싱 하면 list, 문자열을 슬라이싱하면 문자열, ndarray를 슬라이싱하면 ndarray를 반환한다.
#2차원 ndarray를 슬라이싱하면 2차원 ndarray를 반환한다.
print(a[0:2]) #[[0, 1, 2], [3, 4, 5]]
print(a[0:2][0:2]) #[[0, 1, 2], [3, 4, 5]]
print(a[0:2, 0:2]) #[[0, 1], [3, 4]]

#비 연속적인 행 슬라이싱
target = [0, 2]
print(a[target]) #[[0, 1, 2], [6, 7, 8]]

a = np.arange(25).reshape(5, 5)
print(a[1:])
print(a[:, :]) #a 전체 가져옴
print(a[1].sum())
print(a.sum(axis=0)) #axis=0 이면 세로축으로 더해줌 -> [1열 합, 2열 합, 3열 합, 4열 합, 5열 합], 1이면 가로축으로 더해줌


