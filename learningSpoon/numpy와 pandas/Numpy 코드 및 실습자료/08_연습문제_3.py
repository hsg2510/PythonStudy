from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np

path = "gray.jpg"
img = image.imread( path )
img = img[:,:,0].copy()

# 1) 가로 축소
# img = img[ : : 2]

# 2) 가로, 세로 축소
img = img[ : : 2, : : 2]

plt.imshow(img, cmap='gray')
plt.show()