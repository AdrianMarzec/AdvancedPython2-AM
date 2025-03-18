'''Tworzenie własnego "filtra Instagram":
a. Dodaj do kanału czerwonego +30, do zielonego -20, a do niebieskiego +10.
b. Sprawdź, jak zmienia się obraz.'''

import cv2
import numpy as np

image = cv2.imread("wolf.jpg")
image2 = cv2.imread("wolf.jpg")

filtered = cv2.add(image, (10,0,30))
cv2.imshow("CV1", filtered)
filtered = cv2.subtract(image, (0,20,0))
cv2.imshow("CV2", filtered)

numAdd = image + np.uint8((0,0,30))
cv2.imshow("NumPy1", numAdd)
numAdd = image - np.uint8((0,20,0))
cv2.imshow("NumPy2", numAdd)
numAdd = image + np.uint8((10,0,0))
cv2.imshow("NumPy3", numAdd)


cv2.waitKey(0)

