'''Odczyt wartości piksela
a. Wczytaj obraz i pobierz wartość piksela znajdującego się w lewym górnym
rogu (współrzędne 0,0).
b. Wyświetl wartości składowych koloru (R, G, B).'''

import cv2

image = cv2.imread('pies.jpg')

(b, g, r) = image[0,0]
info = f"Pixel at (0,0) - Red {r}, Green {g}, Blue {b}"

cv2.imshow(info, image)
cv2.waitKey(0)