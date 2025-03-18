'''Automatyczne skalowanie na podstawie wysokości
a. Zmień wysokość obrazu na 400 pikseli, zachowując proporcje.
b. Wyświetl wynik.'''

import cv2
import imutils
image = cv2.imread("wolf.jpg")
cv2.imshow("Original", image)
(h,w) = image.shape[:2]
resized = imutils.resize(image, height=400)
cv2.imshow("Resized via imutils", resized)
cv2.waitKey(0)
