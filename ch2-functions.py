import cv2
import numpy as np

# Read in the original image
img = cv2.imread("/home/jack/Desktop/port1.jpg")

# Numpy kernel: 5x5 matrix initialized of ones
# New values in kernel can range from 0 to 255
kernel = np.ones((5,5), np.uint8)

# RGB to grayscale image conversion
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Grayscale to blurred
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)

# Canny edge detection
imgCanny = cv2.Canny(img, 100, 100) # 100s are threshold values

# Dilation increases thickness of image edges
# Iteration: How much the kernel will move around
#            i.e. how thick do we want the edges
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)

# Erosion is the opposite of dilation (Makes edges thinner)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

# Show images
cv2.imshow("Original", img)
cv2.imshow("Gray image", imgGray)
cv2.imshow("Gray blur", imgBlur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Dilation", imgDilation)
cv2.imshow("Erosion", imgEroded)

cv2.waitKey(0)