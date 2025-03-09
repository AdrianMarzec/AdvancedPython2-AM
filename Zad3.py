'''Znajdowanie środka obrazu
a. Wczytaj obraz i oblicz współrzędne jego środka.
b. Pobierz wartość koloru piksela w tym miejscu i wyświetl ją w konsoli.'''

import cv2

image = cv2.imread('pies.jpg')
(h,w) = image.shape[:2]

(cX, cY) = (w//2,h//2)
(b,g,r) = image[cY,cX]
info = f"Pixel w srodku ({cX},{cY}): - Red {r}, Green {g}, Blue {b}"

print(info)
cv2.imshow(info, image)
cv2.waitKey(0)
