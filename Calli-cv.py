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
    # Plum          HSV(329,68%,45%) =>(154, 100, 70) (174, 200, 160)   #
    # Lemon         HSV(93,64%,57%) =>(40, 150, 160) (52, 190, 200)     #
    # Banana        HSV(53,72%,69%) =>(16, 120, 60) (36, 200, 255)      #

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    thresh1_low = cv2.inRange(hsv,np.array((0, 120, 80)), np.array((5, 240, 255)))
    thresh1_high = cv2.inRange(hsv,np.array((175, 120, 80)), np.array((180, 240, 255)))
    thresh1 = cv2.bitwise_or(thresh1_low, thresh1_high)
    thresh = thresh1.copy()
    thresh2 = cv2.inRange(hsv,np.array((154, 100, 70)), np.array((174, 200, 160)))
    thresh3 = cv2.inRange(hsv,np.array((40, 150, 160)), np.array((52, 190, 200)))
    thresh4 = cv2.inRange(hsv,np.array((16, 120, 60)), np.array((36, 200, 255)))

    # find contours in the threshold image
    contours,hierarchy = cv2.findContours(thresh1,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

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

    # finding centroids of best_cnt and draw a circle there
    M = cv2.moments(best_cnt)
    cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    cv2.circle(frame,(cx,cy),5,255,-1)

    # Show it, if key pressed is 'Esc', exit the loop
    cv2.imshow('frame',frame)
    cv2.imshow('thresh',thresh)
    if cv2.waitKey(33)== 27:
        break

# Clean up everything before leaving
cap.release()
cv2.destroyAllWindows()
