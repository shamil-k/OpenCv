


#Bitwise Operations(AND , OR, NOT, XOR)

import cv2 as cv
import numpy as np

img = np.zeros((300, 400, 3), np.uint8)
img = cv.rectangle(img, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv.imread('data/pic1.png')

print(img2.shape)
# Bitwise and
bitAnd = cv.bitwise_and(img, img2)

# Bitwise or
bitOR = cv.bitwise_or(img, img2)

# Bitwise Xor
bitXOR = cv.bitwise_xor(img, img2)


# Bitwise Not
bitNot1 = cv.bitwise_not(img)
bitNot2 = cv.bitwise_not(img2)





cv.imshow('img', img)
cv.imshow('img2', img2)
cv.imshow('bitAnd', bitAnd)
cv.imshow('bitOR', bitOR)
cv.imshow('bitXOR', bitXOR)

cv.imshow('bitNot1', bitNot1)
cv.imshow('bitNot2', bitNot2)

cv.waitKey(0)
cv.destroyAllWindows()
