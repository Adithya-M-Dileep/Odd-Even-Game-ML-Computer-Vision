import cv2
import numpy as np

cap = cv2.VideoCapture(0)


def currentFrame(w, h):
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    imgH, imgW, imgC = frame.shape
    frame = frame[:, imgW//4:3*(imgW//4)]
    frame = cv2.resize(frame, (w, h))
    return frame
