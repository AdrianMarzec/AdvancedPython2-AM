'''Efekty przy skalowaniu w górę
a. Powiększ obraz 4× używając INTER_CUBIC i INTER_LANCZOS4 .
b. Porównaj ostrość obrazu w obu przypadkach.'''

import cv2
import imutils

image = cv2.imread("wolf.jpg")
cv2.imshow("Original", image)
(h,w) = image.shape[:2]
methods = [
("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]
for (name, method) in methods:
    print("[INFO] {}".format(name))
    resized = imutils.resize(image, width=image.shape[1] * 4,
                             inter=method)
    cv2.imshow("Method: {}".format(name), resized)
    cv2.waitKey(0)
