import numpy as np

# 1)
점수 = [30, 25, 66, 23, 44, 23]
a = np.array(점수).reshape(2, 3)

# 2)
print(sum(a[1]))
print(a[-1].sum())
print(a.sum(axis=1)[1])

# 3)
print(a[ :, 1:2 ].sum())
print(a.sum(axis=0)[1])

