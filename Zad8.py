'''Modyfikacja całego wiersza pikseli
a. Wczytaj obraz i zmień kolor wszystkich pikseli w 100. wierszu na zielony
(0, 255, 0) .
b. Wyświetl obraz przed i po zmianie.'''

import cv2
wiersz = 100
image = cv2.imread('pies.jpg')
image2 = cv2.imread('pies.jpg')
(h,w) = image2.shape[:2]

image2[wiersz,0:w] = (0,255,0)


cv2.imshow("Przed", image)
cv2.imshow("Po",image2)
cv2.waitKey(0)
