'''Obrót o 180 stopni za pomocą imutils.rotate
a. Skorzystaj z imutils.rotate, aby obrócić obraz o 180 stopni.
b. Wyświetl wynik.'''

import cv2
import imutils

image = cv2.imread("wolf.jpg")

rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)


cv2.waitKey(0)
