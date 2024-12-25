from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np

path = "gray.jpg"
img = image.imread( path )
img = img[:,:,0].copy()

# img = img + 50
img = np.where(img >= 205, 255, img + 50)

plt.imshow(img, cmap='gray')
plt.show()
