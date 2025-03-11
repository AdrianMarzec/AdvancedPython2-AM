'''Obrót bez przycinania (rotate_bound)
a. Wykorzystaj imutils.rotate_bound, aby obrócić obraz o -33 stopnie i uniknąć
przycięcia.
b. Wyświetl wynik.'''


import cv2
import imutils

image = cv2.imread("wolf.jpg")

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

rotate = int(input("Podaj rotację "))

M = cv2.getRotationMatrix2D((cX, cY), rotate, 1.0)
rotated = imutils.rotate_bound(image, -33)
cv2.imshow("Rotated by 180 Degrees", rotated)


cv2.waitKey(0)