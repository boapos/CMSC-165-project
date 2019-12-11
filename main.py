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
    dilated = cv2.dilate(gaussian, None, iterations=10)
    eroded = cv2.erode(dilated, None, iterations=5)

    #step 3 - differentiate faces - findcontours
    _, contours, _ = cv2.findContours(eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    #step 4 - draw bounding box
    i = 0
    for c in contours:
        rect = cv2.boundingRect(c)
        if rect[2]<100 or rect[2]>800 or rect[3]<100 or rect[3]>800: continue
        i = i+1
        x,y,w,h = rect
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.putText(frame, 'person count:'+str(i),(50,100), cv2.FONT_HERSHEY_SIMPLEX, 2,(255,255,0),2,cv2.LINE_AA)
    cv2.imshow('binary', eroded)
    cv2.imshow('detection', frame)

    #interrupt
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
