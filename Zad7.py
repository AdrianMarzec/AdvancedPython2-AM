'''Porównanie warpAffine i imutils.rotate
a. Wykonaj obrót o 60 stopni dwoma sposobami: za pomocą cv2.warpAffine i
imutils.rotate .
b. Porównaj wyniki i zwróć uwagę na różnice.'''

import cv2
import imutils

image = cv2.imread('wolf.jpg')

rotation = 60

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), rotation, 1.0)
warp = cv2.warpAffine(image, M, (w, h))

imu = imutils.rotate(image, rotation)

cv2.imshow("warp",warp)
cv2.imshow("imutils",imu)
cv2.waitKey(0)
