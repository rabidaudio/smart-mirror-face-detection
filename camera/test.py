import numpy as np
import cv2

bg = cv2.imread('scan.jpg')

one = cv2.imread('scan2.jpg')

two = cv2.imread('scan3.jpg')

diffOne = one - bg

diffTwo = two - bg


thresh = 100

diffOneGrey = cv2.cvtColor(diffOne,cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(diffOneGrey, thresh, 255, cv2.THRESH_TOZERO)
th1 = diffOneGrey & mask


corner = cv2.cornerHarris(diffOneGrey, 2, 3, 0.04)
corner = cv2.dilate(corner,None)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',corner)
cv2.waitKey(0)

cv2.destroyAllWindows()



cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()