'''Segmentacja kolorów z wieloma maskami
a. Wczytaj obraz zawierający elementy w różnych kolorach (np. niebieski,
czerwony, zielony).
b. Przekonwertuj obraz do przestrzeni HSV.
c. Utwórz oddzielne maski dla każdego koloru.
d. Połącz maski, aby wykryć wiele kolorów jednocześnie.
e. Wyświetl efekt segmentacji.'''

import cv2
import numpy as np

image = cv2.imread("SamusPepe.jpg")
cv2.imshow("Original", image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image = cv2.imshow("HSV", hsv)

lower_blue = np.array([80, 100, 50])
upper_blue = np.array([160, 255, 255])

mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
image = cv2.imshow("BLUE", mask_blue)

lower_red = np.array([160, 100, 50])
upper_red = np.array([180, 255, 255])

mask_red = cv2.inRange(hsv, lower_red, upper_red)
image = cv2.imshow("RED", mask_red)

lower_green = np.array([25, 100, 50])
upper_green = np.array([85, 255, 255])

mask_green = cv2.inRange(hsv, lower_green, upper_green)
image = cv2.imshow("GREEN", mask_green)

merged = cv2.merge((mask_blue,mask_green,mask_red))
image = cv2.imshow("Merged Masks", merged)

cv2.waitKey(0)
