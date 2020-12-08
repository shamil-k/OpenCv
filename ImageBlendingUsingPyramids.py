import cv2 as cv
import numpy as np

# 1- load two images
apple = cv.imread('data/apple.jpg')
orange = cv.imread('data/orange.jpg')

print(np.shape(apple))
print(np.shape(orange))

# 2- Find the Gaussian Pyramids for apple and orange
# (in this particular example ,number of level is 6)

# Gaussian pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_layer = cv.pyrDown(apple_copy)
    gp_apple.append(apple_layer)

# Gaussion pyramid for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]

# creating Gaussion layers hr to low reselution
for i in range(6):
    orange_layers = cv.pyrDown(orange_copy)
    gp_orange.append(orange_layers)

# 3- generate laplacian pyramid for apple and orange
# a level in the laplacian pyramid is formed by the difference b/w the level in the gaussion pyramid and extended version
# of it's upper level in the gaussian pyramid

# laplacian for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]

for i in range(5, 0, -1):
    guassian_expanded = cv.pyrUp(gp_apple[i])
    laplacian = cv.subtract(gp_apple[i-1], guassian_expanded)
    lp_apple.append(laplacian)

# laplacian for orange

orange_copy = gp_orange[5]
lp_orange = [orange_copy]

for i in range(5, 0, -1):
    guassian_expanded = cv.pyrUp(gp_orange[i])
    laplacian = cv.subtract(gp_orange[i-1], guassian_expanded)
    lp_orange.append(laplacian)

# 4- Now add left and right halves of images in each levels
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, raw, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols / 2)], orange_lap[:, int(cols / 2):]))
    apple_orange_pyramid.append(laplacian)

# 5 - Finally from this joint image pyramids , reconstruct the original image

apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv.imshow('apple', apple)
cv.imshow('orange', orange)
cv.imshow('apple_orange_reconstruct', apple_orange_reconstruct)
cv.waitKey(0)
cv.destroyAllWindows()
