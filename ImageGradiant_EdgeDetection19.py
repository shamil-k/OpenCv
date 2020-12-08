# image gradient is a directional change in the intensity or color in an image
import cv2 as cv
import numpy as np
from  matplotlib import pyplot as plt

#img = cv.imread('data/messi5.jpg', cv.IMREAD_GRAYSCALE)
img = cv.imread('data/sudoku.png', cv.IMREAD_GRAYSCALE)
# laplacian dt type 64 bit flot it support -ve numbers which  dealing with laplacian method run on image
lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
# taking the absolute value of laplacian image transformation
# convert value back to the un-sign 8 bit integer which is suitable for our o/p
lap = np.uint8(np.absolute(lap))

# sobel gradient representation
# DX stand for order of derivative X , DY derivative of Y
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

# sobelx and sobaly compain
sobelCompained = cv.bitwise_or(sobelX, sobelY)

titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCompained']
images = [img, lap, sobelX, sobelY, sobelCompained]

for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()


