'''Przyciemnianie obrazu
a. Zmniejsz jasność obrazu o 80 jednostek.
b. Porównaj, jak NumPy i OpenCV traktują wartości poniżej 0.'''

import cv2
import numpy as np

image = cv2.imread("wolf.jpg")
image2 = cv2.imread("wolf.jpg")
M = np.ones(image.shape, dtype="uint8") * (80)
added = cv2.subtract(image, M)
cv2.imshow("CV", added)

#M = np.ones(image2.shape, dtype="uint8")
numAdd = image - np.uint8([80])
cv2.imshow("NumPy", numAdd)

cv2.waitKey(0)
