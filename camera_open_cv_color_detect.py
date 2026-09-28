import cv2 as cv
import numpy as np
from pathlib import Path

cap = cv.VideoCapture(0)
color = [0, 128, 0] #green

def get_limit(color):
    c = np.uint8([[color]])
    hsvc = cv.cvtColor(c, cv.COLOR_BGR2HSV)
    hue = hsvc[0][0][0]
    range = 10

    upper_hue = min( 179, hue + range)
    lower_hue = max( 0, hue - range)

    lowerLimit = np.array([lower_hue, 40, 40], dtype=np.uint8)
    upperLimit = np.array([upper_hue, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit

def colour_filter(hsvImage):
    mask = cv.inRange(hsvImage, lowerLimit, upperLimit)
    return mask

lowerLimit, upperLimit = get_limit(color)

while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        break

    hsvImage = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    mask =  colour_filter(hsvImage)
    
    cv.imshow("live feed", frame)
    cv.imshow("mask", mask)

    if cv.waitKey(1) & 0xff == ord("q"):
            break


cap.release()
cv.destroyAllWindows()    