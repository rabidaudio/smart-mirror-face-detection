#!/usr/bin/env python2
import cv2
import sys
import subprocess

cap = cv2.VideoCapture(0)

debug = 'debug' in sys.argv

ret, frame = cap.read()

#Load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')

# source: https://github.com/Aravindlivewire/Opencv/tree/master/haarcascade
# palm_cascade = cv2.CascadeClassifier('./palm.xml')
# fist_cascade = cv2.CascadeClassifier('./fist.xml')
# closed_palm_cascase = cv2.CascadeClassifier('./closed_frontal_palm.xml')

while(ret):

    ret, frame = cap.read()

    #Convert to grayscale
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Look for faces in the image using the loaded cascade file
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # palms = palm_cascade.detectMultiScale(gray, 1.5, 3)
    # fists = fist_cascade.detectMultiScale(gray, 1.1, 5)
    # closed_palms = closed_palm_cascase.detectMultiScale(gray, 1.1, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)

    # for (x,y,w,h) in palms:
    #     cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),2)

    # for (x,y,w,h) in fists:
    #     cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)

    # for (x,y,w,h) in closed_palms:
    #     cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)

    if(debug):
        print str(len(faces)) + " faces"
        cv2.imshow('image', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
          break

    if(len(faces) > 0):
        subprocess.Popen(sys.argv[1].split(' '))

cap.release()
if(debug):
    # When everything done, release the captures
    cv2.destroyAllWindows()