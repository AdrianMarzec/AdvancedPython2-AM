'''Rysowanie linii
a. Narysuj niebieską linię od środka obrazu do jego prawego dolnego rogu.
Grubość linii: 2 px.'''

import cv2
import numpy as np

blue = (255,0,0)
canvas = np.zeros((300,300,3), dtype='uint8') 
(h,w) = canvas.shape[:2]
cv2.line(canvas, (canvas.shape[1]//2, canvas.shape[0]//2), (h,w), blue, 2)

cv2.imshow("Zadanie 1", canvas)
cv2.waitKey(0)