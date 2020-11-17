import cv2
import numpy as np
from numpy.linalg import norm

img = cv2.imread('t3.jpeg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


avg = np.mean(img[:,:, 2])

per = (avg/255)*100

if per >= 0 and per <=33:
    print('Dark', per)

if per > 33 and per <= 66:
    print('normal', per)

if per > 66:
    print('bright', per)
