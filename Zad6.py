'''Zamazywanie szczegółów na zdjęciu
a. Znajdź w Internecie profilowe zdjęcie osoby.
b. Czerwonymi kołami “zasłoń” osobie na zdjęciu oczy.
c. Zielonym prostokątem “zasłoń” osobie na zdjęciu usta.
d. Niebieskim okręgiem obejmij dookoła twarz osoby.'''

import cv2
import numpy as np

image = cv2.imread('wolf.jpg')
cv2.imshow("Zadanie 6 Przed", image)

px = 50
blue = (255,0,0)
red = (0,0,255)
green = (0,255,0)
(h,w) = image.shape[:2]


cv2.circle(image, (80, 80), 20, red, -1)
cv2.circle(image, (150, 70), 20, red, -1)

cv2.rectangle(image, (90,120), (150, 170), green, -1)

cv2.circle(image, (h//2+px//2, w//2-px//2), 100, blue)



cv2.imshow("Zadanie 6 Po", image)
cv2.waitKey(0)