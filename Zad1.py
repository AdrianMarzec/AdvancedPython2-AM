'''Porównanie metod dodawania
a. Wczytaj obraz i zwiększ jego jasność o 50 przy użyciu zarówno NumPy,
jak i OpenCV.
b. Sprawdź, jak różnią się wyniki.'''

import cv2
import numpy as np

image = cv2.imread("wolf.jpg")
image2 = cv2.imread("wolf.jpg")
M = np.ones(image.shape, dtype="uint8") * 50
added = cv2.add(image, M)
cv2.imshow("CV", added)

#M = np.ones(image2.shape, dtype="uint8")
numAdd = image + np.uint8([50])
cv2.imshow("NumPy", numAdd)

cv2.waitKey(0)