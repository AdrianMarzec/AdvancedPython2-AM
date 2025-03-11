'''Rysowanie okręgów, utwórz czarny obraz o wymiarach 300x300 pikseli i
narysuj na nim:
a. Niebieski okrąg o promieniu 40 px w lewym górnym rogu.
b. Czerwony okrąg o promieniu 60 px w środku obrazu.'''


import cv2
import numpy as np

blue = (255,0,0)
red = (0,0,255)
canvas = np.zeros((300,300,3), dtype='uint8') 
(h,w) = canvas.shape[:2]

cv2.circle(canvas, (h//2,w//2),60, red, -1)
cv2.circle(canvas, (0,0), 40, blue, -1)


cv2.imshow("Zadanie 2", canvas)
cv2.waitKey(0)