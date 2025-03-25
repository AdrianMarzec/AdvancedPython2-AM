'''Rekonstrukcja obrazu po manipulacji kanałami
a. Zamień wartości kanałów miejscami, np. wyświetl obraz w kolejności R, B, G.
b. Ustaw wartość jednego z kanałów na zero i zobacz, jak zmienia się wygląd obrazu.'''

import cv2
import numpy as np

image = cv2.imread("flowers.jpg")
(B, G, R) = cv2.split(image)
# show each channel individually
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

G = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Green2", G)

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

cv2.waitKey(0)
