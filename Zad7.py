'''Maska i segmentacja
a. Zastosuj metodę Otsu, a następnie wykorzystaj uzyskaną binarną maskę
do „wycięcia” obiektu z oryginalnego obrazu ( cv2.bitwise_and ).
b. Czy obiekt został skutecznie oddzielony od tła? Jakie ograniczenia tej
metody można zauważyć?'''

import cv2

image = cv2.imread("cobblestone.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

cv2.imshow("Otsu Threshold", thresh)

masked = cv2.bitwise_and(image, image, mask=thresh)

cv2.imshow("Output", masked)

cv2.waitKey(0)
