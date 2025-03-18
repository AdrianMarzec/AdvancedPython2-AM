'''Symulacja efektu "przepalenia" obrazu
a. Dodaj do każdego piksela wartość 150, ale używając NumPy.
b. Porównaj wynik z operacją cv2.add() .'''

import cv2
import numpy as np

image = cv2.imread("wolf.jpg")
image2 = cv2.imread("wolf.jpg")
M = np.ones(image.shape, dtype="uint8") * 150
added = cv2.add(image, M)
cv2.imshow("CV", added)

#M = np.ones(image2.shape, dtype="uint8")
numAdd = image + np.uint8([150])
cv2.imshow("NumPy", numAdd)

cv2.waitKey(0)
