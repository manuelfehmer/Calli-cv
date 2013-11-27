from __future__ import division
from common import nothing
import sys
import math
import cv2
import numpy as np

# convert to hsv and find range of colors =>(0,0,0)-(180,255,255)   #
# Strawberry    HSV(3,73%,70%) =>(0, 160, 160) (6, 200, 200)        #
# Plum          HSV(329,68%,45%) =>(154, 100, 70) (174, 200, 160)   #
# Lemon         HSV(93,64%,57%) =>(40, 150, 160) (52, 190, 200)     #
# Banana        HSV(53,72%,69%) =>(16, 120, 60) (36, 200, 255)      #

lower_s_s = 160
upper_s_s = 200
lower_v_s = 160
upper_v_s = 200

lower_s_p = 100
upper_s_p = 200
lower_v_p = 70
upper_v_p = 160

lower_s_l = 150
upper_s_l = 190
lower_v_l = 160
upper_v_l = 200

lower_s_b = 120
upper_s_b = 200
lower_v_b = 60
upper_v_b = 255

# create video capture
cap = cv2.VideoCapture(0)

cv2.namedWindow('Controls')
# Strawberry-Color-Control
cv2.createTrackbar('delta_H_s','Controls',0,30,nothing)
cv2.createTrackbar('lower_S_s','Controls',0,255,nothing)
cv2.setTrackbarPos('lower_S_s','Controls',lower_s_s)
cv2.createTrackbar('upper_S_s','Controls',0,255,nothing)
cv2.setTrackbarPos('upper_S_s','Controls',upper_s_s)
cv2.createTrackbar('lower_V_s','Controls',0,255,nothing)
cv2.setTrackbarPos('lower_V_s','Controls',lower_v_s)
cv2.createTrackbar('upper_V_s','Controls',0,255,nothing)
cv2.setTrackbarPos('upper_V_s','Controls',upper_v_s)
# Plum-Color-Control
cv2.createTrackbar('delta_H_p','Controls',0,30,nothing)
cv2.createTrackbar('lower_S_p','Controls',0,255,nothing)
cv2.setTrackbarPos('lower_S_p','Controls',lower_s_p)
cv2.createTrackbar('upper_S_p','Controls',0,255,nothing)
cv2.setTrackbarPos('upper_S_p','Controls',upper_s_p)
cv2.createTrackbar('lower_V_p','Controls',0,255,nothing)
cv2.setTrackbarPos('lower_V_p','Controls',lower_v_p)
cv2.createTrackbar('upper_V_p','Controls',0,255,nothing)
cv2.setTrackbarPos('upper_V_p','Controls',upper_v_p)
# Lemon-Color-Control
cv2.createTrackbar('delta_H_l','Controls',0,30,nothing)
cv2.createTrackbar('lower_S_l','Controls',0,255,nothing)
cv2.setTrackbarPos('lower_S_l','Controls',lower_s_l)
cv2.createTrackbar('upper_S_l','Controls',0,255,nothing)
cv2.setTrackbarPos('upper_S_l','Controls',upper_s_l)
cv2.createTrackbar('lower_V_l','Controls',0,255,nothing)
cv2.setTrackbarPos('lower_V_l','Controls',lower_v_l)
cv2.createTrackbar('upper_V_l','Controls',0,255,nothing)
cv2.setTrackbarPos('upper_V_l','Controls',upper_v_l)
# Banana-Color-Control
cv2.createTrackbar('delta_H_b','Controls',0,30,nothing)
cv2.createTrackbar('lower_S_b','Controls',0,255,nothing)
cv2.setTrackbarPos('lower_S_b','Controls',lower_s_b)
cv2.createTrackbar('upper_S_b','Controls',0,255,nothing)
cv2.setTrackbarPos('upper_S_b','Controls',upper_s_b)
cv2.createTrackbar('lower_V_b','Controls',0,255,nothing)
cv2.setTrackbarPos('lower_V_b','Controls',lower_v_b)
cv2.createTrackbar('upper_V_b','Controls',0,255,nothing)
cv2.setTrackbarPos('upper_V_b','Controls',upper_v_b)
cv2.resize

while(1):

    # read the frames
    _,frame = cap.read()

    # smooth it
    frame = cv2.blur(frame,(3,3))

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # read Strawberry-Trackbars
    h_s = cv2.getTrackbarPos('delta_H_s','Controls')
    lower_s_s = cv2.getTrackbarPos('lower_S_s','Controls')
    upper_s_s = cv2.getTrackbarPos('upper_S_s','Controls')
    lower_v_s = cv2.getTrackbarPos('lower_V_s','Controls')
    upper_v_s = cv2.getTrackbarPos('upper_V_s','Controls')
    thresh1_low = cv2.inRange(hsv,np.array((0, lower_s_s, lower_v_s)), np.array((0+h_s, upper_s_s, upper_v_s)))
    thresh1_high = cv2.inRange(hsv,np.array((180-h_s, lower_s_s, lower_v_s)), np.array((180, upper_s_s, upper_v_s)))
    thresh1 = cv2.bitwise_or(thresh1_low, thresh1_high)
    thresh_strawberry = thresh1.copy()

    # read Plum-Trackbars
    h_p = cv2.getTrackbarPos('delta_H_p','Controls')
    lower_s_p = cv2.getTrackbarPos('lower_S_p','Controls')
    upper_s_p = cv2.getTrackbarPos('upper_S_p','Controls')
    lower_v_p = cv2.getTrackbarPos('lower_V_p','Controls')
    upper_v_p = cv2.getTrackbarPos('upper_V_p','Controls')
    thresh2 = cv2.inRange(hsv,np.array((164-h_p, lower_s_p, lower_v_p)), np.array((164+h_p, upper_s_p, upper_v_p)))
    thresh_plum = thresh2.copy()

    # read Plum-Trackbars
    h_l = cv2.getTrackbarPos('delta_H_l','Controls')
    lower_s_l = cv2.getTrackbarPos('lower_S_l','Controls')
    upper_s_l = cv2.getTrackbarPos('upper_S_l','Controls')
    lower_v_l = cv2.getTrackbarPos('lower_V_l','Controls')
    upper_v_l = cv2.getTrackbarPos('upper_V_l','Controls')
    thresh3 = cv2.inRange(hsv,np.array((46-h_l, lower_s_l, lower_v_l)), np.array((46+h_l, upper_s_l, upper_v_l)))
    thresh_lemon = thresh3.copy()

    # read Plum-Trackbars
    h_b = cv2.getTrackbarPos('delta_H_b','Controls')
    lower_s_b = cv2.getTrackbarPos('lower_S_b','Controls')
    upper_s_b = cv2.getTrackbarPos('upper_S_b','Controls')
    lower_v_b = cv2.getTrackbarPos('lower_V_b','Controls')
    upper_v_b = cv2.getTrackbarPos('upper_V_b','Controls')
    thresh4 = cv2.inRange(hsv,np.array((26-h_b, lower_s_b, lower_v_b)), np.array((26+h_b, upper_s_b, upper_v_b)))
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
                    #print banana_area

    cv2.namedWindow('Frame')
    cv2.drawContours(frame, strawberries, -1, (0,0,255), 2)
    cv2.drawContours(frame, plums, -1, (255,0,230), 2)
    cv2.drawContours(frame, lemons, -1, (0,255,0), 2)
    cv2.drawContours(frame, bananas, -1, (0,255,255), 2)
    cv2.imshow('Frame',frame)

    if len(strawberries) == 5:
        print "Strawberries!"
    if len(plums) == 5:
        print "Plums!"
    if len(lemons) == 5:
        print "Lemons!"
    if len(bananas) == 5:
        print "Bananas!"
    

    cv2.namedWindow('Strawberries')
    cv2.imshow('Strawberries',thresh_strawberry)
    cv2.namedWindow('Plums')   
    cv2.imshow('Plums',thresh_plum)
    cv2.namedWindow('Lemons')
    cv2.imshow('Lemons',thresh_lemon)
    cv2.namedWindow('Bananas')
    cv2.imshow('Bananas',thresh_banana)

    # Show it, if key pressed is 'Esc', exit the loop
    if cv2.waitKey(33)== 27:
        break

# Clean up everything before leaving
cap.release()
cv2.destroyAllWindows()
