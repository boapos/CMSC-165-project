import cv2
import numpy as np

cap = cv2.VideoCapture('https://192.168.254.101:8080/video')

while(True):

    ret, frame = cap.read()
    #convert frame to hsv
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #binarize image
    #define thresholds
    lower_threshold = np.array([0,48,80], dtype=np.uint8)
    upper_threshold = np.array([20,255,255], dtype=np.uint8)
    #single channel mask
    skinMask = cv2.inRange(frame, lower_threshold, upper_threshold)
    #cleaning up mask using gaussian filter
    skinMask = cv2.GaussianBlur(skinMask,(3,3),0)
    #extract skin from threshold mask
    #skin = cv2.bitwise_and(frame, frame, mask=skinMask)
    #skin = cv2.cvtColor(skin, cv2.COLOR_HSV2BGR)

    cv2.imshow('stream', skinMask)

    #interrupt
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
