# Import OpenCV and print to be sure there are no issues
import cv2
print("Package imported")

'''
Chapter 1:  Reading images, videos, and webcams
'''

# Read an image into OpenCV with the function cv2.imread
image = cv2.imread("/home/jack/Desktop/jrp.png")
# Output the image with cv2.imshow
cv2.imshow("Output", image)
# cv2.waitKey adds a timer as to how long we want the image to appear
# Setting cv2.waitKey to 0 makes the image appear indefinitely
# Setting cv2.waitKey to 1 would be 1ms and 1000 would be 1 second
cv2.waitKey(0)
