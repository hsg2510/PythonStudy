import numpy as np

data = [ 1, 2, 3, 4]
#       0  1  2  3  4
a = np.array(data)

print(a[  2  ])
print(a[ 0:2 ])
print(a[[2,0]])

data = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
#      0         1         2            3
a = np.array(data)

print(a[  0  ])
print(a[ 0:2 ])
print(a[[0,2]])

print(a[0][2])
print(a[0, 2])
print(a[0:2,0:2])