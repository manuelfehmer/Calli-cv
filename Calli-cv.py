from __future__ import division
from common import nothing, draw_str
import sys
import math
import cv2
import numpy as np

# convert to hsv and find range of colors =>(0,0,0)-(180,255,255)   #

# Strawberry    HSV(3,73%,70%) =>(0, 160, 160) (6, 200, 200)        #
# hue
delta_h_s = 5
# saturation
lower_s_s = 142
upper_s_s = 255
# value
lower_v_s = 0
upper_v_s = 255

# Plum          HSV(329,68%,45%) =>(154, 100, 70) (174, 200, 160)   #
# hue
delta_h_p = 10
# saturation
lower_s_p = 79
upper_s_p = 255
# value
lower_v_p = 0
upper_v_p = 255

# Lemon         HSV(93,64%,57%) =>(40, 150, 160) (52, 190, 200)     #
# hue
delta_h_l = 7
# saturation
lower_s_l = 101
upper_s_l = 255
# value
lower_v_l = 0
upper_v_l = 206

# Banana        HSV(53,72%,69%) =>(16, 120, 60) (36, 200, 255)      #
# hue
delta_h_b = 10
# saturation
lower_s_b = 103
upper_s_b = 255
# value
lower_v_b = 101
upper_v_b = 255

# create video capture
# try external Webcam
try: cap = cv2.VideoCapture(1)
# except internal Webcam
except:  cap = cv2.VideoCapture(0)

cv2.namedWindow('Controls')
# Strawberry-Color-Control
cv2.createTrackbar('delta_H_s','Controls',0,30,nothing)     # hue
cv2.setTrackbarPos('delta_H_s','Controls',delta_h_s)
cv2.createTrackbar('lower_S_s','Controls',0,255,nothing)    # saturation
cv2.setTrackbarPos('lower_S_s','Controls',lower_s_s)
cv2.createTrackbar('upper_S_s','Controls',0,255,nothing)
cv2.setTrackbarPos('upper_S_s','Controls',upper_s_s)
cv2.createTrackbar('lower_V_s','Controls',0,255,nothing)    # value
cv2.setTrackbarPos('lower_V_s','Controls',lower_v_s)
cv2.createTrackbar('upper_V_s','Controls',0,255,nothing)
cv2.setTrackbarPos('upper_V_s','Controls',upper_v_s)
# Plum-Color-Control
cv2.createTrackbar('delta_H_p','Controls',0,30,nothing)     # hue
cv2.setTrackbarPos('delta_H_p','Controls',delta_h_p)
cv2.createTrackbar('lower_S_p','Controls',0,255,nothing)    # saturation
cv2.setTrackbarPos('lower_S_p','Controls',lower_s_p)
cv2.createTrackbar('upper_S_p','Controls',0,255,nothing)
cv2.setTrackbarPos('upper_S_p','Controls',upper_s_p)
cv2.createTrackbar('lower_V_p','Controls',0,255,nothing)    # value
cv2.setTrackbarPos('lower_V_p','Controls',lower_v_p)
cv2.createTrackbar('upper_V_p','Controls',0,255,nothing)
cv2.setTrackbarPos('upper_V_p','Controls',upper_v_p)
# Lemon-Color-Control
cv2.createTrackbar('delta_H_l','Controls',0,30,nothing)     # hue
cv2.setTrackbarPos('delta_H_l','Controls',delta_h_l)
cv2.createTrackbar('lower_S_l','Controls',0,255,nothing)    # saturation
cv2.setTrackbarPos('lower_S_l','Controls',lower_s_l)
cv2.createTrackbar('upper_S_l','Controls',0,255,nothing)
cv2.setTrackbarPos('upper_S_l','Controls',upper_s_l)
cv2.createTrackbar('lower_V_l','Controls',0,255,nothing)    # value
cv2.setTrackbarPos('lower_V_l','Controls',lower_v_l)
cv2.createTrackbar('upper_V_l','Controls',0,255,nothing)
cv2.setTrackbarPos('upper_V_l','Controls',upper_v_l)
# Banana-Color-Control
cv2.createTrackbar('delta_H_b','Controls',0,30,nothing)     # hue
cv2.setTrackbarPos('delta_H_b','Controls',delta_h_b)
cv2.createTrackbar('lower_S_b','Controls',0,255,nothing)    # saturation
cv2.setTrackbarPos('lower_S_b','Controls',lower_s_b)
cv2.createTrackbar('upper_S_b','Controls',0,255,nothing)
cv2.setTrackbarPos('upper_S_b','Controls',upper_s_b)
cv2.createTrackbar('lower_V_b','Controls',0,255,nothing)    # value
cv2.setTrackbarPos('lower_V_b','Controls',lower_v_b)
cv2.createTrackbar('upper_V_b','Controls',0,255,nothing)
cv2.setTrackbarPos('upper_V_b','Controls',upper_v_b)
cv2.namedWindow("Controls", cv2.CV_WINDOW_AUTOSIZE)

kernel = np.ones((5,5),np.uint8)

while(1):

    # read the frames
    _,frame = cap.read()

    # transform frame to HSV 
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # read Strawberry-Trackbars 
    h_s = cv2.getTrackbarPos('delta_H_s','Controls')
    lower_s_s = cv2.getTrackbarPos('lower_S_s','Controls')
    upper_s_s = cv2.getTrackbarPos('upper_S_s','Controls')
    lower_v_s = cv2.getTrackbarPos('lower_V_s','Controls')
    upper_v_s = cv2.getTrackbarPos('upper_V_s','Controls')
    # use Threshold for Strawberries
    thresh1_low = cv2.inRange(hsv,np.array((0, lower_s_s, lower_v_s)), np.array((0+h_s, upper_s_s, upper_v_s)))
    thresh1_high = cv2.inRange(hsv,np.array((180-h_s, lower_s_s, lower_v_s)), np.array((180, upper_s_s, upper_v_s)))
    # 
    thresh1 = cv2.bitwise_or(thresh1_low, thresh1_high)
    # Closing
    thresh1 = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)
    # create Binary-Frame
    thresh_strawberry = thresh1.copy()

    # read Plum-Trackbars
    h_p = cv2.getTrackbarPos('delta_H_p','Controls')
    lower_s_p = cv2.getTrackbarPos('lower_S_p','Controls')
    upper_s_p = cv2.getTrackbarPos('upper_S_p','Controls')
    lower_v_p = cv2.getTrackbarPos('lower_V_p','Controls')
    upper_v_p = cv2.getTrackbarPos('upper_V_p','Controls')
    #use Threshold for Plums
    thresh2 = cv2.inRange(hsv,np.array((164-h_p, lower_s_p, lower_v_p)), np.array((164+h_p, upper_s_p, upper_v_p)))
    # Closing
    thresh2 = cv2.morphologyEx(thresh2, cv2.MORPH_CLOSE, kernel)
    # Opening
    thresh2 = cv2.morphologyEx(thresh2, cv2.MORPH_OPEN, kernel)
    # create Binary-Frame
    thresh_plum = thresh2.copy()

    # read Lemon-Trackbars
    h_l = cv2.getTrackbarPos('delta_H_l','Controls')
    lower_s_l = cv2.getTrackbarPos('lower_S_l','Controls')
    upper_s_l = cv2.getTrackbarPos('upper_S_l','Controls')
    lower_v_l = cv2.getTrackbarPos('lower_V_l','Controls')
    upper_v_l = cv2.getTrackbarPos('upper_V_l','Controls')
    # Threshold for Lemons
    thresh3 = cv2.inRange(hsv,np.array((46-h_l, lower_s_l, lower_v_l)), np.array((46+h_l, upper_s_l, upper_v_l)))
    # Opening
    thresh3 = cv2.morphologyEx(thresh3, cv2.MORPH_OPEN, kernel)
    # Closing
    thresh3 = cv2.morphologyEx(thresh3, cv2.MORPH_CLOSE, kernel)
    # create Binary-Frame
    thresh_lemon = thresh3.copy()

    # read Banana-Trackbars
    h_b = cv2.getTrackbarPos('delta_H_b','Controls')
    lower_s_b = cv2.getTrackbarPos('lower_S_b','Controls')
    upper_s_b = cv2.getTrackbarPos('upper_S_b','Controls')
    lower_v_b = cv2.getTrackbarPos('lower_V_b','Controls')
    upper_v_b = cv2.getTrackbarPos('upper_V_b','Controls')
    # use Threshold for Bananas
    thresh4 = cv2.inRange(hsv,np.array((8+h_b, lower_s_b, lower_v_b)), np.array((28+h_b, upper_s_b, upper_v_b)))
    # Opening
    thresh4 = cv2.morphologyEx(thresh4, cv2.MORPH_OPEN, kernel)    
    # Closing
    thresh4 = cv2.morphologyEx(thresh4, cv2.MORPH_CLOSE, kernel)

    # create Binary-Frame
    thresh_banana = thresh4.copy()

    # Filter for Fruit-Thresholds 
    strawberry_contours,strawberry_hierarchy = cv2.findContours(thresh1,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    plum_contours,plum_hierarchy = cv2.findContours(thresh2,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    lemon_contours,lemon_hierarchy = cv2.findContours(thresh3,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    banana_contours,banana_hierarchy = cv2.findContours(thresh4,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    # Find Strawberries
    strawberries = []
    if len(strawberry_contours) > 0:
        for cnt in strawberry_contours:

            strawberry_area = cv2.contourArea(cnt)
            (x_c,y_c),radius = cv2.minEnclosingCircle(cnt)

            center = (int(x_c),int(y_c))
            radius = int(radius)
            rect = cv2.minAreaRect(cnt)
            pos, size, theta = rect
            box = cv2.cv.BoxPoints(rect)
            box = np.int0(box)
            x, y = pos
            w, h = size
            
            if 600 < strawberry_area < 1300:
                if 0.7 < h/w < 1.4:
                    area_rate = w*h/strawberry_area # 1.6
                    if 1.3 < area_rate < 1.8:
                        strawberries.append(cnt)
                        #draw_str(frame, (int(x)+radius, int(y)+12), str(h/w))
                        #draw_str(frame, (int(x)+radius, int(y)+24), str(strawberry_area))
                        #draw_str(frame, (int(x)+radius, int(y)), str(area_rate))
                        #cv2.drawContours(frame,[box],0,(0,255,0),2)
       
    #Find Plums
    plums = []
    if len(plum_contours) > 0:
        for cnt in plum_contours:

            plum_area = cv2.contourArea(cnt)
            (x_c,y_c),radius = cv2.minEnclosingCircle(cnt)

            center = (int(x_c),int(y_c))
            radius = int(radius)
            rect = cv2.minAreaRect(cnt)
            pos, size, theta = rect
            box = cv2.cv.BoxPoints(rect)
            box = np.int0(box)
            x, y = pos
            w, h = size

            if 1000 < plum_area < 1700:
                if 0.6 < h/w < 1.6:
                    area_rate = w*h/plum_area # 1.3
                    if 0.9 < area_rate < 1.6:
                        plums.append(cnt)
                        
                        #draw_str(frame, (int(x)+radius, int(y)+12), str(h/w))
                        #draw_str(frame, (int(x)+radius, int(y)+24), str(plum_area))
                        #draw_str(frame, (int(x)+radius, int(y)), str(area_rate))
                        #cv2.drawContours(frame,[box],0,(0,255,0),2)

    #Find Lemons
    lemons = []
    if len(lemon_contours) > 0:
        for cnt in lemon_contours:

            lemon_area = cv2.contourArea(cnt)
            (x_c,y_c),radius = cv2.minEnclosingCircle(cnt)
 
            center = (int(x_c),int(y_c))
            radius = int(radius)
            rect = cv2.minAreaRect(cnt)
            pos, size, theta = rect
            box = cv2.cv.BoxPoints(rect)
            box = np.int0(box)
            x, y = pos
            w, h = size

            if 600 < lemon_area < 1400:             
                if 0.6 < h/w < 1.6:
                    area_rate = w*h/lemon_area # 1.2
                    if 0.9 < area_rate < 1.6:
                        lemons.append(cnt)
                        #draw_str(frame, (int(x)+radius, int(y)+12), str(h/w))
                        #draw_str(frame, (int(x)+radius, int(y)), str(area_rate))
                        #draw_str(frame, (int(x)+radius, int(y)+24), str(lemon_area))
                        #cv2.drawContours(frame,[box],0,(0,255,0),2)

    #Find Bananas
    bananas = []
    if len(banana_contours) > 0:
        for cnt in banana_contours:

            banana_area = cv2.contourArea(cnt)
            (x_c,y_c),radius = cv2.minEnclosingCircle(cnt)

            center = (int(x_c),int(y_c))
            radius = int(radius)
            rect = cv2.minAreaRect(cnt)
            pos, size, theta = rect
            box = cv2.cv.BoxPoints(rect)
            box = np.int0(box)
            x, y = pos
            w, h = size

            if 300 < banana_area < 900:
                if h < w:
                    w, h = h, w
                if 2.0 < h/w < 3.9:
                    area_rate = w*h/banana_area # 1.7
                    if 1.2 < area_rate < 2.9:
                        bananas.append(cnt)
                        #draw_str(frame, (int(x)+radius, int(y)), str(h/w))
                        #draw_str(frame, (int(x)+radius, int(y)+24), str(banana_area))
                        #draw_str(frame, (int(x)+radius, int(y)+12), str(area_rate)) 
                        # cv2.drawContours(frame,[box],0,(0,255,0),2)         

    cv2.namedWindow('Frame')
    cv2.drawContours(frame, strawberries, -1, (0,0,255), 2)
    cv2.drawContours(frame, plums, -1, (255,0,230), 2)
    cv2.drawContours(frame, lemons, -1, (0,255,0), 2)
    cv2.drawContours(frame, bananas, -1, (0,255,255), 2)

    if len(strawberries) == 5:
        #print "Strawberries!"
        draw_str(frame, (20, 20), "Strawberries!!!!!")
    if len(plums) == 5:
        #print "Plums!"
        draw_str(frame, (20, 40), "Plums!!!!!")
    if len(lemons) == 5:
        #print "Lemons!"
        draw_str(frame, (20, 60), "Lemons!!!!!")
    if len(bananas) == 5:
        #print "Bananas!"
        draw_str(frame, (20, 80), "Bananas!!!!!")

    cv2.imshow('Frame',frame) 

    #show Thresholdwindow for Fruits
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
