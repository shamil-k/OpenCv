import cv2
import numpy as np



##img = cv2.imread('Photos/cat.jpg', 1)

img = np.zeros([512, 512, 3], np.uint8)


img = cv2.line(img, (0, 0), (255, 255), (0, 255, 0), 10)
img = cv2.arrowedLine(img, (0, 255), (255, 255), (0, 255, 0), 10)

img = cv2.rectangle(img, (350, 0), (510, 400), (0, 0, 255), 10)
img = cv2.circle(img, (300, 63), 63, (0, 255, 0), 5)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,  'OpenCv', (10, 300), font, 4, (255, 255, 255), 10, cv2.LINE_AA)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
