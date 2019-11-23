import cv2
import numpy as np

cap = cv2.VideoCapture('https://192.168.254.101:8080/video')

while(True):

    ret, frame = cap.read()
    cv2.imshow('stream',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
