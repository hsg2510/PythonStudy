import numpy as np

점수 = [30, 25, 66, 23, 44, 23]
a = np.array(점수).reshape(2, 3)
print(a)

중간 = a[0]
분산 = 중간.var()
print(분산)
print(a.var( axis = 1 )[0])

기말 = a[-1]
분산 = 기말.var()
print(분산)
print(a.var( axis = 1 )[1])