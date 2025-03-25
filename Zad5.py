'''Zastosowanie maski do selektywnej modyfikacji kanałów
a. czytaj obraz i stwórz maskę obejmującą tylko wybrany obiekt (np.
czerwony samochód).
b. Wykorzystując maskę, zwiększ nasycenie koloru czerwonego tylko w tej
części obrazu.'''

import cv2
import numpy as np

image = cv2.imread("flowers.jpg")
cv2.imshow("Original", image)
(B, G, R) = cv2.split(image)

mask = np.full(image.shape[:2], 255, dtype="uint8")
cv2.rectangle(mask, (100, 200), (1000, 500), 0, -1)

R_masked  = cv2.add(R, 50)
R_masked  = cv2.bitwise_and(R, R, mask=mask)
merged = cv2.merge([B,G,R_masked])
cv2.imshow("FINAL", merged)

cv2.waitKey(0)
