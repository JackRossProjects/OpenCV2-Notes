import cv2
import numpy as np

# Create an image of size 512x512 with color functionality but initialize to 0 (black)
img = np.zeros((512,512,3), np.uint8)
# (512, 512) = grayscale || (512, 512, 3) = color functionality

# If we want to make the entire ([:]) image (img) blue (255, 0, 0)
# img[:] = 255, 0, 0

# Adding a line
# cv2.line(image, start point, end point, color, thickness)
cv2.line(img,(0,0), (300,300), (0, 255, 0), 3)

# Drawing a rectangle (same convention as above)
# cv2.FILLED will fill in any shape i.e. this rectangle
cv2.rectangle(img, (0,0), (250, 350), (0,0,255), 2, cv2.FILLED)

# Drawing a circle
# cv2.circle(image, center, radius, color, thickness)
cv2.circle(img, (400, 200), 30, (255, 255, 0), 2)

# Adding text
# cv2.putText(image, text, start, font, font scale, color, thickness)
cv2.putText(img, "OpenCV ROCKS!", (200, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 150, 0), 1)

cv2.imshow("image", img)
cv2.waitKey(0)