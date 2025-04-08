'''Wpływ rozmycia
a. Do jednego z obrazów z Zadania 1 zastosuj rozmycie Gaussa
(cv2.GaussianBlur) przed progowaniem.
b. Porównaj wynik progowania z i bez rozmycia. Jak rozmycie wpływa na
jakość binarnego obrazu?'''

import cv2

image = cv2.imread("cobblestone.jpg")
cv2.imshow("Image", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

lista = [30,100,200]

for T in lista:
    (T, threshInv) = cv2.threshold(blurred, T, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow(f"Threshold Binary Inverse {T}", threshInv)

cv2.waitKey(0)
