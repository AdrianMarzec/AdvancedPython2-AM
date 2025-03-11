'''Obrót wokół narożnika
a. Obróć obraz o 30 stopni względem lewego górnego narożnika (0,0).
b. Wyświetl wynik.'''

import cv2

image = cv2.imread("wolf.jpg")
cv2.imshow("Original", image)

(h, w) = image.shape[:2]

M = cv2.getRotationMatrix2D((0, 0), 30, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 30 Degrees", rotated)

cv2.waitKey(0)