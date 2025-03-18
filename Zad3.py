'''Przycięcie prawej połowy obrazu
a. Przycięcie prawej połowy obrazu
b. Wyświetl tylko prawą połowę.'''

import cv2

image = cv2.imread("wolf.jpg")
print("[INFO] flipping images...")
w = image.shape[1]
w = w//2

roiLeft = image[:, :w]
roiRight = image[:, w:]
cv2.imshow("Original", image)
cv2.imshow("roiRight", roiRight)
#cv2.imshow("roiLeft", roiLeft)
cv2.waitKey(0)
