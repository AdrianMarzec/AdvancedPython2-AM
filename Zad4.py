'''Obrót o dowolny kąt
a. Pobierz od użytkownika kąt obrotu i wykonaj rotację wokół środka obrazu.
b. Wyświetl wynik.'''

import cv2

image = cv2.imread("wolf.jpg")

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

rotate = int(input("Podaj rotację "))

M = cv2.getRotationMatrix2D((cX, cY), rotate, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Original", image)
cv2.imshow(f"Rotated by {rotate} Degrees", rotated)

cv2.waitKey(0)