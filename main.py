import cv2
import numpy as np

cap = cv2.VideoCapture('https://192.168.254.101:8080/video')

while(True):

    ret, frame = cap.read()
    #convert to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('stream', hsv)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
