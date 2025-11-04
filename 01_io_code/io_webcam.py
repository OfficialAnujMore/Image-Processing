import os
import cv2

# read webcam

webcam = cv2.VideoCapture(1)

# visualize webcam

while True:
    ret, frame = webcam.read()
    cv2.imshow('frame', frame)
    # Press q to quit
    if cv2.waitKey(40) & 0xFF == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()
