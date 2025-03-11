'''Rysowanie prostokątów, utwórz czarny obraz o wymiarach 400x400 pikseli i
narysuj na nim:
a. Zielony prostokąt o wymiarach 100x50 pikseli w lewym górnym rogu.
b. Czerwony prostokąt o grubości 3 px w prawym dolnym rogu.'''

import cv2
import numpy as np

green = (0,255,0)
red = (0,0,255)
canvas = np.zeros((400,400,3), dtype='uint8') 
(h,w) = canvas.shape[:2]

cv2.rectangle(canvas, (0,0), (50,100), green,-1)
cv2.rectangle(canvas, (h-50,w-100), (h-1,w-1), red,3)


cv2.imshow("Zadanie 2", canvas)
cv2.waitKey(0)