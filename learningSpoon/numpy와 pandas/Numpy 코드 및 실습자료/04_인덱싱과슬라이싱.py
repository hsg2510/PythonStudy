import numpy as np

a = np.arange(25).reshape(5, 5)
print(a)
print(a[1:3])
print(a[1:3, :3])
print(a[:,:][:,:][:,:])
print(a[  [4, 0]  ])