'''Automatyczne skalowanie na podstawie szerokości
a. Zmień szerokość obrazu na 500 pikseli, zachowując proporcje.
b. Użyj imutils.resize() .'''

import cv2
import imutils
image = cv2.imread("wolf.jpg")
cv2.imshow("Original", image)
(h,w) = image.shape[:2]
resized = imutils.resize(image, width=500)
cv2.imshow("Resized via imutils", resized)
cv2.waitKey(0)
