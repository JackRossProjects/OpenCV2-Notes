import cv2
import numpy as np

# Read in the original image
img = cv2.imread("/home/jack/Desktop/port1.jpg")
# Result: (250, 500, 3)
print(img.shape)

# New size: width = 300, height = 200
imgResize = cv2.resize(img, (300, 200))
# Result: (200, 300, 3)
print(imgResize.shape)

# Opposed to above: [0:100] = height, [200:500] = width
imgCropped = img[0:100,200:500]

cv2.imshow("Image", img)
cv2.imshow("Resized", imgResize)
cv2.imshow("Cropped", imgCropped)
cv2.waitKey(0)