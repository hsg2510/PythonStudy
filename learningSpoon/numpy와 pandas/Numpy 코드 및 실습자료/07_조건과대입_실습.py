import numpy as np

# 3이하는 0으로 그렇지 않으면 기존값 + 2
# 0 0 0
# 0 6 7
# 8 9 10

# 1) 조건
a = np.arange(9).reshape(3,3)
print(a)
a[a<=3] = 0
print(a)
a[a>3] = a[a>3] + 2
print(a)

# 2) np.where
a = np.arange(9).reshape(3,3)
print(a)
a = np.where(a<=3, 0, a+2)
print(a)

