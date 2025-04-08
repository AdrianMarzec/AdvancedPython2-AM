'''Analiza nasycenia w obrazie
a. Wczytaj dowolny obraz i przekonwertuj go do przestrzeni HSV.
b. Rozdziel obraz na kanały H, S i V.
c. Obniż poziom nasycenia (S) w całym obrazie.
d. Podwyższ poziom nasycenia (S) w całym obrazie.
e. Porównaj zmodyfikowane obrazy z oryginałem.'''

import cv2

image = cv2.imread("SamusPepe.jpg")

cv2.imshow("Original", image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image = cv2.imshow("HSV", hsv)
h,s,v  = cv2.split(hsv)
s = cv2.add(s, 100)
added = cv2.merge((h,s,v))
cv2.imshow("Added", added)
s = cv2.subtract(s, 200)
subtract = cv2.merge((h,s,v))
cv2.imshow("Subtract", subtract)
cv2.waitKey(0)
