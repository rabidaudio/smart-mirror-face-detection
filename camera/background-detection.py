#!/usr/bin/env python2
import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

frameCount = 20

ret, frame = cap.read()
lastFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# frames = np.repeat(lastFrame, frameCount)
frames = []
for i in range(0, frameCount):
  frames.append(lastFrame)

# lastFrame = cv2.medianBlur(lastFrame, 5)
# lastFrame = cv2.adaptiveThreshold(lastFrame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,5)

lastMean = cv2.mean(lastFrame)[0]

if(not ret):
  print "Unable to read camera!"

# fgbg = cv2.BackgroundSubtractorMOG()

x = 0

while(ret):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # fgmask = fgbg.apply(frame)

    # Our operations on the frame come here
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # frame = cv2.medianBlur(frame, 5)
    # frame = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,5)

    # diff = frame - lastFrame

    # frame = cv2.medianBlur(frame, 15)
    # diff = cv2.bilateralFilter(diff, 25, 150, 150)
    # diff = frame - bg

    diff = 0*frame
    for i in range(0, frameCount):
      # diff = cv2.addWeighted(diff, i/frameCount, frames[((x+i) % frameCount)], 1-(i/frameCount), 0)
      diff = diff + (frames[((x+i) % frameCount)]/frameCount)

    diff = diff - lastFrame

    mean = cv2.mean(diff)[0]
    diffMean = abs(mean - lastMean)
    if(diffMean > 20):
      print diffMean

    lastFrame = frame
    lastMean = mean
    x = (x+1) % frameCount

    frames[x] = frame

    # out = np.dstack([diff, 0*diff, edge])

    # Display the resulting frame
    cv2.imshow('image', diff)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
    # time.sleep(1)

cap.release()
# When everything done, release the captures
cv2.destroyAllWindows()