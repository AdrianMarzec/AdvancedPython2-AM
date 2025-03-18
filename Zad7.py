'''Efekty przy skalowaniu w dół
a. Zmniejsz obraz 5× przy użyciu INTER_AREA.
b. Sprawdź, jak zmienia się jakość w porównaniu do innych metod.'''

import cv2
import imutils

image = cv2.imread("wolf.jpg")
cv2.imshow("Original", image)
(h,w) = image.shape[:2]
methods = [
("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
("cv2.INTER_AREA", cv2.INTER_AREA),
("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]
for (name, method) in methods:
    print("[INFO] {}".format(name))
    resized = imutils.resize(image, width=image.shape[1] // 5,
                             inter=method)
    cv2.imshow("Method: {}".format(name), resized)
    cv2.waitKey(0)

