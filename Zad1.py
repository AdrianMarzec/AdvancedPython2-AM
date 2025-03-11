'''Podstawowe przesunięcie
a. Załaduj dowolny obraz i wyświetl go w oryginalnej postaci.
b. Przesuń obraz o 30 pikseli w prawo i 40 pikseli w dół za pomocą macierzy
transformacji M oraz cv2.warpAffine.
c. Wyświetl wynik.'''

import cv2
import numpy as np

image = cv2.imread('wolf.jpg')
cv2.imshow("Original", image)

M = np.float32([[1, 0, 30], [0, 1, 40]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Transformed", shifted)
cv2.waitKey(0)

