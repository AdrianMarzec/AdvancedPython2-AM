'''Efekty erozji
a. Do jednego z uzyskanych obrazów binarnych z Zadania 2 zastosuj
operację erozji (cv2.erode).
b. Opisz, jak zmienił się obraz po tej operacji. Czy zauważyłeś redukcję
szumów lub niechcianych pikseli?'''

import cv2
import numpy as np

image = cv2.imread("cobblestone.jpg")
cv2.imshow("Image", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

lista = [30,100,200]

(T, threshInv) = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow(f"Threshold Binary Inverse {T}", threshInv)


kernel = np.ones((3, 3), np.uint8)

eroded = cv2.erode(threshInv, kernel, iterations=1)
cv2.imshow("Eroded Image", eroded)

cv2.waitKey(0)
