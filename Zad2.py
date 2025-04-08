'''Modyfikacja jednego kanału i wpływ na obraz
a. Wczytaj obraz do programu i przekonwertuj go do przestrzeni HSV.
b. Rozdziel obraz na kanały H, S, V.
c. Wybierz jeden kanał (np. S – nasycenie) i zwiększ jego wartości o
określoną liczbę (np. +30).
d. Połącz kanały z powrotem i przekonwertuj obraz do przestrzeni RGB.
e. Wyświetl zmodyfikowany obraz i porównaj go z oryginałem.'''

import cv2

image = cv2.imread("SamusPepe.jpg")

cv2.imshow("Original", image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image = cv2.imshow("HSV", hsv)
h,s,v  = cv2.split(hsv)
s = cv2.add(s, 100)
added = cv2.merge((h,s,v))
cv2.imshow("Added", added)
cv2.waitKey(0)
