import cv2
print("cv2 Imported")

# Setting VideoCapture to 0 selects the default webcam
cap = cv2.VideoCapture(0)

# Sets webcam dimensions
# 3 is the width key (below sets width to 640px)
cap.set(3, 640)
# 4 is the height key (below sets height to 480px)
cap.set(4, 480)
# 10 is the brightness key (below sets brightness to 100)
cap.set(10, 100)

# Since there isn't a built in showWebcam function,
# we'll use a while loop to show each frame from the webcam in succession
while True:
    # img saves a frame into the variable
    # success will return boolean value if it that save was successful
    success, img = cap.read()
    # Show the result from above
    cv2.imshow("Video", img)
    # Displays 1 frame from webcam every 1ms
    # and will close the video output if the key q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break