'''Progowanie metodą Otsu
a. Zastosuj progowanie metodą Otsu do rozjaśnionego obrazu z Zadania 4.
b. Jak wygląda wynik? Porównaj go z wynikami z poprzedniego zadania. Co
mówi to o zaletach Otsu?'''

import cv2

image = cv2.imread("cobblestone.jpg")
cv2.imshow("Image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(T, threshInv) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold", threshInv)
print("[INFO] otsu's thresholding value: {}".format(T))
masked = cv2.bitwise_and(image, image, mask=threshInv)

cv2.imshow("Output", masked)

image = cv2.imread("cobblestone.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.add(gray,50)
(T, threshInv) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
masked = cv2.bitwise_and(image, image, mask=threshInv)
cv2.imshow("Output Light", masked)

cv2.waitKey(0)
