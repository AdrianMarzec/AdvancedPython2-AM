'''Wykrywanie niebieskich obiektów w przestrzeni HSV
a. Znajdź i wczytaj obraz zawierający wyraźny niebieski element.
b. Przekonwertuj obraz do przestrzeni HSV.
c. Zdefiniuj zakres wartości H, S i V odpowiadających kolorowi niebieskiemu.
d. Stwórz maskę, która zaznaczy obiekty w tym zakresie kolorów.
e. Nałóż maskę na oryginalny obraz i wyświetl efekt segmentacji.'''

import cv2
import numpy as np

image = cv2.imread("blue.jpg")
cv2.imshow("Original", image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

lower_blue = np.array([100, 100, 50])
upper_blue = np.array([140, 255, 255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Segmented Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()