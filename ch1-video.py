import cv2
print("cv2 Imported")
cap = cv2.VideoCapture("train.mp4")

# Since there isn't a built in showVideo function,
# we'll use a while loop to show each frame of the video in succession
while True:
    # img saves a frame into the variable
    # success will return boolean value if it that save was successful
    success, img = cap.read()
    # Show the result from above
    cv2.imshow("Video", img)
    # Displays 1 frame of the video every 1ms
    # and will close the video output if the key 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
