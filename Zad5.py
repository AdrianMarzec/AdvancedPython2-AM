'''Kadrowanie twarzy
a. Znajdź zdjęcie z twarzą.
b. Znajdź obszar, w którym się znajduje, i przytnij obraz tak, aby pozostała tylko twarz.'''

import cv2

image = cv2.imread("wolf.jpg")
print("[INFO] flipping images...")
startX = 40
endX = 190
startY = 20
endY = 160
roi = image[startY:endY, startX:endX]
cv2.imshow("Original", image)
cv2.imshow("ROI", roi)
cv2.waitKey(0)