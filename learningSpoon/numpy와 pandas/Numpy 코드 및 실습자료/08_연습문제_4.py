from matplotlib import image
import matplotlib.pyplot as plt

path = "gray.jpg"
img = image.imread( path )
img = img[:,:,0].copy()

path = "logo.jpg"
logo = image.imread( path )
logo = logo[:,:,0].copy()

logo = logo[::2, ::2]
print(logo.shape)

img[0:logo.shape[0], 0:logo.shape[1]] = logo

plt.imshow(img, cmap='gray')
plt.show()