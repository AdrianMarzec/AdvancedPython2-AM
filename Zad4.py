'''Porównanie różnych metod interpolacji
a. Powiększ obraz 3× przy użyciu różnych metod interpolacji (INTER_NEAREST,
INTER_LINEAR, INTER_CUBIC, INTER_LANCZOS4).
b. Wyświetl i porównaj wyniki.'''

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
    resized = imutils.resize(image, width=image.shape[1] * 3,
                             inter=method)
    cv2.imshow("Method: {}".format(name), resized)
    cv2.waitKey(0)
