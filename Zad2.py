'''Przycięcie dolnej połowy obrazu
a. Podziel obraz na dwie równe części (górną i dolną).
b. Wyświetl tylko dolną połowę.'''

import cv2

image = cv2.imread("wolf.jpg")
print("[INFO] flipping images...")
h = image.shape[0]
h = h//2
roiUp = image[:h, :]
roiDown = image[h:, :]
cv2.imshow("Original", image)
cv2.imshow("DownHalf", roiDown)
#cv2.imshow("UpHalf", roiUp)
cv2.waitKey(0)
