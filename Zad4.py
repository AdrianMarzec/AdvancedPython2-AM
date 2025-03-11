'''Złożona figura
a. Narysuj na obrazie figurę składającą się z kwadratu o wymiarach 100x100
px, wewnątrz którego znajduje się mniejszy okrąg o promieniu 30 px.
Wszystko powinno być wycentrowane na obrazie.'''

import cv2
import numpy as np

px = 100
blue = (255,0,0)
red = (0,0,255)
green = (0,255,0)
canvas = np.zeros((300,300,3), dtype='uint8') 
(h,w) = canvas.shape[:2]

cv2.rectangle(canvas, (h//2-(px//2),w//2-(px//2)), (h//2+(px//2),w//2+(px//2)), red, -1)
cv2.circle(canvas, (h//2,w//2),30, green, -1)


cv2.imshow("Zadanie 4", canvas)
cv2.waitKey(0)