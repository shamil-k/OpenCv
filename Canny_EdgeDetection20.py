import cv2 as cv
from matplotlib import pyplot as plt


def nothing(x):
    pass

img = cv.imread('data/messi5.jpg', cv.IMREAD_GRAYSCALE)
# canny edge detection method
canny = cv.Canny(img, 100, 200)



titles = ['image', 'canny']
images = [img, canny]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
