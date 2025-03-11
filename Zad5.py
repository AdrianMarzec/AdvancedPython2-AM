'''Eksperymentowanie z pętlą
a. Zmodyfikuj kod pętli rysującej okręgi, aby zamiast okręgów rysowała
kwadraty. Każdy kolejny kwadrat powinien być większy o 20 pikseli od
poprzedniego i mieć środek w tym samym miejscu.'''

import cv2
import numpy as np

px = 100
blue = (255,0,0)
red = (0,0,255)
green = (0,255,0)
canvas = np.zeros((300,300,3), dtype='uint8') 
(h,w) = canvas.shape[:2]



for px in range(0, h, 20):
    cv2.rectangle(canvas, (h//2-(px//2), w//2-(px//2)), (h//2+(px//2), w//2+(px//2)), green)


cv2.imshow("Zadanie 5", canvas)
cv2.waitKey(0)