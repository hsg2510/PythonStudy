from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np

path = "gray.jpg"
img = image.imread( path )
img = img[:,:,0].copy()

img = 255 - img

plt.imshow(img, cmap='gray')
plt.show()