import cv2 as cv
import numpy as np

img = cv.imread('Photos/hand.jpg')
# first_layer = cv.pyrDown(img)
# second_layer = cv.pyrDown(first_layer)
# third_layer = cv.pyrDown(second_layer)
# forth_layer = cv.pyrDown(third_layer)
# fifth_layer = cv.pyrDown(forth_layer)

cv.imshow('original', img)
# cv.imshow('first_layer', first_layer)
# cv.imshow('second_layer', second_layer)
# cv.imshow('third_layer', third_layer)
# cv.imshow('forth_layer', forth_layer)
# cv.imshow('fifth_layer', fifth_layer)
#

cv.waitKey(0)
cv.destroyAllWindows()
