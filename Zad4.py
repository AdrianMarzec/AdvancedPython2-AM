'''Manipulacja barwy obrazu (zmiana odcienia H)
a. Wczytaj obraz i przekonwertuj go do przestrzeni HSV.
b. Zwiększ wartość kanału H o określoną liczbę (np. +30), aby przesunąć
odcień kolorów.
c. Połącz zmodyfikowany obraz i przekonwertuj go z powrotem do
przestrzeni RGB.
d. Wyświetl obraz przed i po zmianie odcienia.'''

import cv2

image = cv2.imread("SamusPepe.jpg")

cv2.imshow("Original", image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image = cv2.imshow("HSV", hsv)
h,s,v  = cv2.split(hsv)
h = cv2.add(h, 100)
added = cv2.merge((h,s,v))
cv2.imshow("Added", added)
cv2.waitKey(0)

