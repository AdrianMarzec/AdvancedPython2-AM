'''Wykorzystanie maski do ekstrakcji koloru
a. Wczytaj kolorowy obraz (np. kwiaty, samochód).
b. Stwórz maskę w taki sposób, aby pozostawić tylko jeden wybrany kolor, a
resztę obrazu zaciemnić.
c. Wskazówka: użyj konwersji obrazu do przestrzeni barw HSV i maskowania
na podstawie zakresu kolorów.'''

import cv2
import numpy as np

image = cv2.imread('flowers.jpg')
cv2.imshow("Kwiaty", image)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([(140,10,10)])
upper = np.array((255,255,255))
mask = cv2.inRange(hsv,lower,upper)

cv2.imshow("Rectangular Mask", mask)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)

cv2.waitKey(0)
