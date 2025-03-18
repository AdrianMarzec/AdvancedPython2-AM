'''Kopiowanie i wklejanie fragmentu obrazu
a. Przytnij określony fragment obrazu (np. o wymiarach 100x100 pikseli).
b. Wklej ten fragment w inne miejsce na obrazie.'''

import cv2

image = cv2.imread("wolf.jpg")
print("[INFO] flipping images...")
startX = 40
endX = 140
startY = 20
endY = 120
roi = image[startY:endY, startX:endX]
image[0:100,0:100] = roi
cv2.imshow("Original", image)
cv2.imshow("ROI", roi)
cv2.waitKey(0)
