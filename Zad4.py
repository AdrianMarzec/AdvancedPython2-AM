'''Dynamiczny wybór ROI
a. Napisz skrypt, który pozwala użytkownikowi podać wartości startX , endX ,
startY , endY z klawiatury.
b. Przytnij obraz zgodnie z wprowadzonymi wartościami i wyświetl wynik.'''

import cv2

image = cv2.imread("wolf.jpg")
print("[INFO] flipping images...")
startX = int(input("startX "))
endX = int(input("endX "))
startY = int(input("startY "))
endY = int(input("endY "))
roi = image[startY:endY, startX:endX]
cv2.imshow("Original", image)
cv2.imshow("ROI", roi)
cv2.waitKey(0)