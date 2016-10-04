#!/usr/bin/env python2
import numpy as np
import cv2
import time

threshold = 100
sleep = 2

cap = cv2.VideoCapture(0)

bg = cv2.imread('bg.jpg')
ret = True
if(bg is None):
  ret, bg = cap.read()
  cv2.imwrite('bg.jpg', bg)

bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)

while(ret):
  ret, frame = cap.read()
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  diff = frame - bg

  mean = cv2.mean(diff)[0]

  print mean

  if(mean < threshold):
    print "detected!"
    bg = frame

  time.sleep(sleep)

cap.release()