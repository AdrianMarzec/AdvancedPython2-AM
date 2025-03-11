'''Dynamiczne przesunięcie na podstawie parametrów użytkownika
a. Zmodyfikuj kod, aby użytkownik mógł podać wartości przesunięcia tx i ty
poprzez wprowadzenie ich z klawiatury (np. przy użyciu input())
b. Sprawdź, jak działa przesunięcie dla różnych wartości.'''

import cv2
import numpy as np

tx = int(input("Horyzontalnie "))
ty = int(input("Wertykalnie "))

image = cv2.imread('wolf.jpg')
cv2.imshow("Original", image)

M = np.float32([[1, 0, tx], [0, 1, ty]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Transformed", shifted)
cv2.waitKey(0)