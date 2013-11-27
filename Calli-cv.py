import cv2
import numpy as np

# create video capture
cap = cv2.VideoCapture(0)

while(1):

    # read the frames
    _,frame = cap.read()

    # smooth it
    frame = cv2.blur(frame,(3,3))

    # convert to hsv and find range of colors =>(0,0,0)-(180,255,255)   #
    # Strawberry    HSV(3,73%,70%) =>(0, 160, 160) (6, 200, 200)        #
    # Plum          HSV(329,68%,45%) =>(154, 160, 100) (174, 200, 130)  #
    # Lemon         HSV(93,64%,57%) =>(36, 140, 160) (56, 180, 200)     #
    # Banana        HSV(53,72%,69%) =>(16, 160, 160) (36, 200, 200)     #

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv,np.array((36, 150, 100)), np.array((56, 190, 200)))
    thresh2 = thresh.copy()

    # find contours in the threshold image
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    # finding contour with maximum area and store it as best_cnt
    if len(contours) > 0:
        max_area = 0
        best_cnt = contours[0]
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > max_area:
                max_area = area
                best_cnt = cnt
        print best_cnt


    # Show it, if key pressed is 'Esc', exit the loop
    cv2.imshow('frame',frame)
    cv2.imshow('thresh',thresh2)
    if cv2.waitKey(33)== 27:
        break

# Clean up everything before leaving
cap.release()
cv2.destroyAllWindows()