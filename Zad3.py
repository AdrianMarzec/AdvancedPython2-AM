'''Eksperymentowanie z dużymi wartościami przesunięcia
a. Przesuń obraz o więcej niż połowę jego szerokości i wysokości.
b. Sprawdź, co dzieje się z pikselami, które wychodzą poza zakres
oryginalnego obrazu.'''

import cv2
import numpy as np

image = cv2.imread('wolf.jpg')
cv2.imshow("Original", image)
(h,w) = image.shape[:2]

M = np.float32([[1, 0, -(h//2-5)], [0, 1, -(w//2-5)]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Transformed", shifted)
cv2.waitKey(0)
