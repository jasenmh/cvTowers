#!/usr/bin/env python2.7

import numpy as np
import cv2
import cv2.cv as cv

def main():
  currCam = 0
  #cv.NamedWindow("Camera0", 1)
  cv.NamedWindow("Camera1", 1)

  #capture0 = cv.CaptureFromCAM(0)
  capture1 = cv.CaptureFromCAM(currCam)

  while True:
    #img0 = cv.QueryFrame(capture0)
    img1 = cv.QueryFrame(capture1)
    #cv.ShowImage("Camera0", img0)
    cv.ShowImage("Camera1", img1)

    currKey=cv.WaitKey(10)
    if currKey  == 27:
      break
    elif currKey == 43:
      currCam = (currCam + 1) % 10
      capture1 = cv.CaptureFromCAM(currCam)

  cv.DestroyAllWindows()

if __name__ == "__main__":
  main()
