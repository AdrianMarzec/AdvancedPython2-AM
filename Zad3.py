'''Zmiana rozmiaru na konkretną wartość
a. Zmień rozmiar obrazu na dokładnie 200×300 pikseli.
b. Użyj cv2.resize().'''

import cv2

image = cv2.imread("wolf.jpg")
cv2.imshow("Original", image)
resized = cv2.resize(image, (200,300), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Resized", resized)
cv2.waitKey(0)
