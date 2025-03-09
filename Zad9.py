'''Zmiana wartości pikseli w określonym zakresie
a. Wypełnij obszar od (50,50) do (100,100) kolorem białym (255, 255, 255).
b. Wyświetl obraz przed i po zmianie.'''

import cv2
start = (50,50)
end = (100,100)
image = cv2.imread('pies.jpg')
image2 = cv2.imread('pies.jpg')
(h,w) = image2.shape[:2]

image2[start[0]:end[0],start[1]:end[1]] = (255,255,255)


cv2.imshow("Przed", image)
cv2.imshow("Po",image2)
cv2.waitKey(0)