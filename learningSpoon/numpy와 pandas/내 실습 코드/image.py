import numpy as np
from matplotlib import image
import matplotlib.pyplot as plt

img = image.imread('test.png')

print(img.dtype)
print(img.ndim)
print(img.shape)

img = img[:, :, 0].copy()
#img[:100] = 255

print(img[0]) # y좌표 0인 픽셀들의 컬러값들
img[50:100] = 0.0 #-> y좌표 50 ~ 99에 있는 픽셀은 검은색으로 칠해라

#img = np.where((img + 0.5) > 1.0, 1.0, (img + 0.5))
plt.imshow(img, cmap='gray')
plt.show()

