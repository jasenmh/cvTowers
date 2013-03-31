#!/usr/bin/env python2.7

import numpy as np
import cv2
import cv2.cv as cv

HMIN = 121
SMIN = 33
VMIN = 108
HMAX = 149
SMAX = 114
VMAX = 255
erodeElement = cv.CreateStructuringElementEx(3, 3, 1, 1, cv2.MORPH_RECT)
dilateElement = cv.CreateStructuringElementEx(8, 8, 1, 1, cv2.MORPH_RECT)

def update_hmin(val):
  global HMIN
  HMIN = val

def update_hmax(val):
  global HMAX
  HMAX = val

def update_smin(val):
  global SMIN
  SMIN = val

def update_smax(val):
  global SMAX
  SMAX = val

def update_vmin(val):
  global VMIN
  VMIN = val

def update_vmax(val):
  global VMAX
  VMAX = val

def cleanFilteredImage(thresh):
  global erodeElement
  global dilateElement

  cv.Erode(thresh, thresh)#, erodeElement)
  cv.Erode(thresh, thresh)#, erodeElement)

  cv.Dilate(thresh, thresh)#, dilateElement)
  cv.Dilate(thresh, thresh)#, dilateElement)

  return thresh

def createTrackbarWindow():
  winName = "Trackbars"
  cv.NamedWindow(winName, 1)
  cv.CreateTrackbar("HMIN", winName, HMIN, 255, update_hmin)
  cv.CreateTrackbar("HMAX", winName, HMAX, 255, update_hmax)
  cv.CreateTrackbar("SMIN", winName, SMIN, 255, update_smin)
  cv.CreateTrackbar("SMAX", winName, SMAX, 255, update_smax)
  cv.CreateTrackbar("VMIN", winName, VMIN, 255, update_vmin)
  cv.CreateTrackbar("VMAX", winName, VMAX, 255, update_vmax)

def setupCamera(camera=0):
  capture = cv.CaptureFromCAM(camera)
  return capture

def setupWindows():
  cv.NamedWindow("CVTowers", 1)
  #cv.NamedWindow("HSVImage", 1)
  cv.NamedWindow("Thresholded", 1)

def main():
  capture = setupCamera()
  setupWindows()
  createTrackbarWindow()

  # main loop
  while True:
    img = cv.QueryFrame(capture)
    cv.Smooth(img, img, cv.CV_BLUR, 3)

    hsvimg = cv.CreateImage(cv.GetSize(img), 8, 3)
    cv.CvtColor(img, hsvimg, cv.CV_BGR2HSV)
    thresholdimg = cv.CreateImage(cv.GetSize(hsvimg), 8, 1)
    lowerBound = cv.Scalar(HMIN, SMIN, VMIN)
    upperBound = cv.Scalar(HMAX, SMAX, VMAX)
    #print HMIN, HMAX, SMIN, SMAX, VMIN, VMAX
    cv.InRangeS(hsvimg, lowerBound, upperBound, thresholdimg)
 
    threshholdimg = cleanFilteredImage(thresholdimg)
 
    cv.ShowImage("CVTowers", img)
    #cv.ShowImage("HSVImage", hsvimg)
    cv.ShowImage("Thresholded", thresholdimg)

    currKey=cv.WaitKey(10)
    if currKey  == 27:
      break

  cv.DestroyAllWindows()

if __name__ == "__main__":
  main()
