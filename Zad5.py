'''Wykrywanie zielonych obiektów w przestrzeni HSV
a. Wczytaj obraz, który zawiera zarówno zielone obiekty, jak i inne kolory.
b. Przekonwertuj obraz do przestrzeni HSV.
c. Ustaw przedział wartości dla koloru zielonego w HSV.
d. Wygeneruj maskę zaznaczającą tylko zielone elementy.
e. Nałóż maskę na oryginalny obraz i wyświetl wynik.'''

import cv2
import numpy as np

image = cv2.imread("SamusPepe.jpg")
cv2.imshow("Original", image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

lower = np.array([25, 100, 50])
upper = np.array([85, 255, 255])

mask = cv2.inRange(hsv, lower, upper)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Segmented Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
