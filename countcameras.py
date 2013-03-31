#!/usr/bin/env python2.7

import numpy as np
import cv2
import cv2.cv as cv

def countcameras():
  for i in range(10):
    temp_camera = cv.CreateCameraCapture(i-1)
    temp_frame = cv.QueryFrame(temp_camera)
    del(temp_camera)
    if temp_frame == None:
      del(temp_frame)
      return i-1
    else:
      print "Camera at ", i
  return -2

def main():
  num_cams = countcameras()
  print num_cams

if __name__ == "__main__":
  main()
