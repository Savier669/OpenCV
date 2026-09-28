import cv2 as cv
import numpy as np
from pathlib import Path

cap = cv.VideoCapture(0)

while cap.isOpened():
    ret,frame = cap.read()

    if not ret:
        break

    if cv.waitKey(1) & 0xff == ord("q")
        break
    cv.imshow("live feed", frame)


cv.release()
cv.destroyAllWindows()    