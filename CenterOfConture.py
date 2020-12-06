# Compute the center of a contour/shape region.
# Recognize various shapes, such as circles, squares, rectangles, triangles, and pentagons using only contour properties
# Label the color of a shape.


# import the necessary packages
import argparse
import imutils
import cv2

# load the image convert it to grayscale,blure it slightly,thresh it

img = cv2.imread('data/shapes_and_colors.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# loop over the contours
for c in cnts:
    # compute the center of the contour
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    # draw the contour and center of the shape on the image
    cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
    cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(img, "center", (cX - 20, cY - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    # show the image
    cv2.imshow("Conture Image", img)
    cv2.waitKey(0)

cv2.imshow('image', img)
cv2.imshow('thresh', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()




