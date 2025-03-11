'''Obrót o 45 stopni
a. Wczytaj obraz i wykonaj obrót o 45 stopni wokół jego środka.
b. Wyświetl obraz przed i po rotacji.'''

import cv2

image = cv2.imread("wolf.jpg")
cv2.imshow("Original", image)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)

cv2.waitKey(0)
