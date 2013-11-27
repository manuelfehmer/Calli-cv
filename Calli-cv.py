from __future__ import division
import sys
import math
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

    thresh1_low = cv2.inRange(hsv,np.array((0, 110, 120)), np.array((6, 255, 255)))
    thresh1_high = cv2.inRange(hsv,np.array((178, 110, 120)), np.array((180, 255, 255)))
    thresh1 = cv2.bitwise_or(thresh1_low, thresh1_high)
    thresh_strawberry = thresh1.copy()
    thresh2 = cv2.inRange(hsv,np.array((154, 100, 70)), np.array((174, 200, 160)))
    thresh_plum = thresh2.copy()
    thresh3 = cv2.inRange(hsv,np.array((40, 80, 140)), np.array((52, 200, 200)))
    thresh_lemon = thresh3.copy()
    thresh4 = cv2.inRange(hsv,np.array((16, 100, 60)), np.array((36, 200, 255)))
    thresh_banana = thresh4.copy()

    # Filter for Fruit-Thresholds 
    strawberry_contours,strawberry_hierarchy = cv2.findContours(thresh1,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    plum_contours,plum_hierarchy = cv2.findContours(thresh2,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    lemon_contours,lemon_hierarchy = cv2.findContours(thresh3,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    banana_contours,banana_hierarchy = cv2.findContours(thresh4,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    # Find Strawberries
    strawberries = []
    if len(strawberry_contours) > 0:
        best_cnt = strawberry_contours[0]
        for cnt in strawberry_contours:

            strawberry_area = cv2.contourArea(cnt)
            strawberry_perimeter = cv2.arcLength(cnt,True)

            (x_c,y_c),radius = cv2.minEnclosingCircle(cnt)
            center = (int(x_c),int(y_c))
            radius = int(radius)

            rect = cv2.minAreaRect(cnt)
            pos, size, theta = rect
            box = cv2.cv.BoxPoints(rect)
            box = np.int0(box)
            x, y = pos
            w, h = size
            
            if 400 < strawberry_area < 3000:
                if 0.7 < h/w < 1.3:
                    strawberries.append(cnt)
                    #cv2.drawContours(frame,[box],0,(0,255,0),2)
                    #cv2.circle(frame,center,radius,(255,255,255),2)
            
    #Find Plums
    plums = []
    if len(plum_contours) > 0:
        best_cnt = plum_contours[0]
        for cnt in plum_contours:

            plum_area = cv2.contourArea(cnt)
            plum_perimeter = cv2.arcLength(cnt,True)

            (x_c,y_c),radius = cv2.minEnclosingCircle(cnt)
            center = (int(x_c),int(y_c))
            radius = int(radius)

            rect = cv2.minAreaRect(cnt)
            pos, size, theta = rect
            box = cv2.cv.BoxPoints(rect)
            box = np.int0(box)
            x, y = pos
            w, h = size
            
            if 600 < plum_area < 4000:
                if 0.7 < h/w < 1.3:
                    plums.append(cnt)
                    #cv2.drawContours(frame,[box],0,(0,255,0),2)
                    #cv2.circle(frame,center,radius,(255,255,255),2)

    #Find Lemons
    lemons = []
    if len(lemon_contours) > 0:
        best_cnt = lemon_contours[0]
        for cnt in lemon_contours:

            lemon_area = cv2.contourArea(cnt)
            lemon_perimeter = cv2.arcLength(cnt,True)

            (x_c,y_c),radius = cv2.minEnclosingCircle(cnt)
            center = (int(x_c),int(y_c))
            radius = int(radius)

            rect = cv2.minAreaRect(cnt)
            pos, size, theta = rect
            box = cv2.cv.BoxPoints(rect)
            box = np.int0(box)
            x, y = pos
            w, h = size
            
            if 400 < lemon_area < 3000:
                if 0.7 < h/w < 1.3:
                    lemons.append(cnt)
                    #cv2.drawContours(frame,[box],0,(0,255,0),2)
                    #cv2.circle(frame,center,radius,(255,255,255),2)
    #Find Bananas
    bananas = []
    if len(banana_contours) > 0:
        best_cnt = banana_contours[0]
        for cnt in banana_contours:

            banana_area = cv2.contourArea(cnt)
            banana_perimeter = cv2.arcLength(cnt,True)

            (x_c,y_c),radius = cv2.minEnclosingCircle(cnt)
            center = (int(x_c),int(y_c))
            radius = int(radius)

            rect = cv2.minAreaRect(cnt)
            pos, size, theta = rect
            box = cv2.cv.BoxPoints(rect)
            box = np.int0(box)
            x, y = pos
            w, h = size
             
            if 400 < banana_area < 3000:
                if 2.2 < h/w < 2.6:
                    bananas.append(cnt)
                if 2.2 < w/h < 2.6:
                    bananas.append(cnt)
                    #cv2.drawContours(frame,[box],0,(0,255,0),2)
                    #cv2.circle(frame,center,radius,(255,255,255),2)
                    print banana_area

    cv2.drawContours(frame, strawberries, -1, (0,0,255), 2)
    cv2.drawContours(frame, plums, -1, (255,0,230), 2)
    cv2.drawContours(frame, lemons, -1, (0,255,0), 2)
    cv2.drawContours(frame, bananas, -1, (0,255,255), 2)

    if len(strawberries) == 5:
        print "Strawberries!"
    cv2.imshow('frame',frame)
    cv2.imshow('Strawberries',thresh_strawberry)
    cv2.imshow('Plums',thresh_plum)
    cv2.imshow('Lemons',thresh_lemon)
    cv2.imshow('Bananas',thresh_banana)

    # Show it, if key pressed is 'Esc', exit the loop
    if cv2.waitKey(33)== 27:
        break

# Clean up everything before leaving
cap.release()
cv2.destroyAllWindows()
