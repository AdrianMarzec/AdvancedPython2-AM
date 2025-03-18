'''Zmniejszenie obrazu o połowę
a. Wczytaj obraz i zmniejsz jego szerokość oraz wysokość o 50%.
b. Wyświetl wynik.'''

import cv2

image = cv2.imread("wolf.jpg")
cv2.imshow("Original", image)
(h,w) = image.shape[:2]
h = h//2
w = w//2
resized = cv2.resize(image, (w,h), interpolation=cv2.INTER_AREA)
cv2.imshow("Resized", resized)
cv2.waitKey(0)
