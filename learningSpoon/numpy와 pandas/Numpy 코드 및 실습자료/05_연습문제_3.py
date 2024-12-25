import numpy as np

점수 = [30, 25, 66, 23, 44, 23]
a = np.array(점수).reshape(2, 3)

print(a[-1].var())
print(a.var(axis=1)[1])
