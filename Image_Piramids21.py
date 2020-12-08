# Gaussian pyramid and Laplacian pyramid help us to blend and reconstruction of images
#Gaussian pyramid is taking the image to high reselution to low
# a level in the laplacian pyramid is formed by the diffrence b/w the level in the gaussion pyramid and extended version
# of it's upper level in the gaussian pyramid

import cv2 as cv

img = cv.imread("data/lena.jpg")
layer = img.copy()
# Gussion pyramid

gp = [layer]

for i in range(5):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    # cv.imshow(str(i), layer)

# Laplacian piramids
layer = gp[-1]
cv.imshow('upper level Gaussian pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussion_extended = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1], gaussion_extended)
    cv.imshow(str(i), laplacian)

cv.imshow('Orginal image', img)
cv.waitKey(0)
cv.destroyWindow()
