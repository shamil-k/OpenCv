import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('data/opencv-logo.png')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernal = np.ones((5, 5), np.float32) /25

dst = cv.filter2D(img, -1, kernal) # homo geneous filter , each o/p filter is the mean of it's kernel neighbours

titles = ['images', '2D convolution']
images = [img, dst]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()



