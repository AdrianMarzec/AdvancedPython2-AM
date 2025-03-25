'''Ukrywanie określonego obszaru twarzy
a. Wczytaj zdjęcie osoby.
b. Stwórz maskę zasłaniającą oczy (np. prostokąt lub elipsa).
c. Zastosuj maskę na obrazie i wyświetl wynik.'''

import cv2
import numpy as np

'''60,50 : 190,145'''

image = cv2.imread("wolf.jpg")
cv2.imshow("Original", image)

mask = np.full(image.shape[:2], 255, dtype="uint8")
cv2.rectangle(mask, (55, 55), (175, 85), 0, -1)
cv2.imshow("Rectangular Mask", mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)

cv2.waitKey(0)
