'''Przesunięcie w przeciwnym kierunku
a. Wykorzystaj ten sam obraz co wcześniej.
b. Przesuń go o 20 pikseli w lewo i 50 pikseli w górę.
c. Wyświetl wynik.'''

import cv2
import numpy as np

image = cv2.imread('wolf.jpg')
cv2.imshow("Original", image)

M = np.float32([[1, 0, -20], [0, 1, -50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Transformed", shifted)
cv2.waitKey(0)
