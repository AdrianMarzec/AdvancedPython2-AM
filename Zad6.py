'''Rozpoznawanie koloru skóry w przestrzeni HSV
a. Wybierz zdjęcie przedstawiające osobę (portret lub zdjęcie całej sylwetki).
b. Przekonwertuj obraz do przestrzeni HSV.
c. Ustal zakres wartości HSV odpowiadający odcieniom skóry.
d. Wygeneruj maskę wykrywającą obszary skóry.
e. Wyświetl oryginalny obraz oraz efekt maskowania.'''

import cv2
import numpy as np

image = cv2.imread("man.jpg")
cv2.imshow("Original", image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

lower = np.array([0, 10, 10])
upper = np.array([80, 255, 255])

mask = cv2.inRange(hsv, lower, upper)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Mask", mask)
cv2.imshow("Segmented Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

