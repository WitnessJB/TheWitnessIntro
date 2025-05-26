import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

cap = cv2.VideoCapture(0)
time.sleep(1.000) #for Windows to initialize camera

while True: #while loop not needed if image is used instead
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #hsv has more range in hues. than rgb/hsl.
    
    #array here goes red, green, blue values
    lower_green = np.array([40,45,30])
    upper_green = np.array([220,255,200])
    
    mask = cv2.inRange(hsv, lower_green, upper_green)
    res = cv2.bitwise_and(frame, frame, mask = mask) #where things are within the range of the mask, the color will be shown.
    
    kernel = np.ones((15,15), np.float32)/225 #225 comes from 15 x 15.
    smoothed = cv2.filter2D(res, -1, kernel)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('res', res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27: #Escape is this key
        break

cap.release()
cv2.destroyAllWindows()
