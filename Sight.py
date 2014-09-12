import cv2, math
import numpy as np
from cv2 import *
f = 'test2.jpg'
img = imread(f)
gray = cvtColor(img, COLOR_BGR2GRAY)
hsv = cvtColor(img, COLOR_BGR2HSV)

def a(img, gray):

    circles = 5
    blur = GaussianBlur(gray, (9,9), 2, 2)
    ret,thresh = threshold(blur, 100, 255, THRESH_BINARY)
    #thresh = medianBlur(gray, 19)
    circles = HoughCircles(thresh, cv.CV_HOUGH_GRADIENT, 5, 75, circles, 50, 150, 20, 140)
    circles = np.round(circles[0, :]).astype("int")
    print(circles)
    #HCirc not work
    for (x, y, r) in circles:
        circle(img, (x, y), r, (0, 255, 0), 1)
        circle(img, (x, y), 3, (255, 0, 0), 1)
    imshow('img', img)
    waitKey(0)
    destroyAllWindows()

def b(img, gray):
    ret,thresh = threshold(gray, 200, 1, THRESH_BINARY)
    contours,h = findContours(thresh, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        approx = approxPolyDP(cnt,0.01*arcLength(cnt,False),False)
        #approx = approxPolyDP(cnt,0.01*arcLength(cnt,True),True)
        print(len(approx))
        if len(approx) < 20:
            drawContours(img, [cnt], 0, 255, 1)
    imshow('img', thresh)
    imshow('img2', img)
    waitKey(0)
    destroyAllWindows()

a(img, gray)
