#dec 10 - 7:15 progress
import cv2
import numpy as np

cap = cv2.VideoCapture('https://192.168.254.106:8080/video')

while(True):

    ret, frame = cap.read()
    #step 1 - convert frame to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #step 2 - binarize image
    #define thresholds - skin color
    lower_threshold = np.array([0,58,50])
    upper_threshold = np.array([30,255,255])
    #single channel mask
    skin = cv2.inRange(hsv, lower_threshold, upper_threshold)
    #cleaning up mask using gaussian filter & dilation
    gaussian = cv2.GaussianBlur(skin,(3,3),0)
    dilated = cv2.dilate(gaussian, None, iterations=11)
    #extract skin from threshold mask
    #skin = cv2.bitwise_and(frame, frame, mask=binary_skin)
    #skin = cv2.cvtColor(skin, cv2.COLOR_HSV2BGR)

    #step 3 - differentiate faces - findcontours
    _, contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

    #step 4 - draw bounding box
    for c in contours:
        rect = cv2.boundingRect(c)
        if rect[2]<100 or rect[3]<100: continue
        x,y,w,h = rect
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('stream', frame)

    #interrupt
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
