# Thresholding is a very popular segmentation technic use for seperating object from its background
# The process of thresholding involves comparing each pixel of an image with a pre defined threshold value
# this type of comparision of each pixel of an image to a threshold value
# divides all the pixel of the input image into two group
# first group involves the pixels having density value lower than the threshold value
# second group involves the pixels having density value grater than the threshold value


# diffrents types of thresholding

import cv2 as cv

img = cv.imread('data/gradient.png')

_, th1 = cv.threshold(img, 120, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 120, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 120, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 120, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 120, 255, cv.THRESH_TOZERO_INV)


cv.imshow('Image', img)
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)
cv.imshow('th4', th4)
cv.imshow('th5', th5)
cv.waitKey(0)
cv.destroyAllWindows()


# ret is a boolean variable that returns true if the frame is available.
# frame is an image array vector captured based on the default frames per second defined explicitly or implicitly
