'''Interaktywna analiza parametrów
a. Zbuduj prosty interfejs przy użyciu cv2.createTrackbar, który pozwoli:
i. zmieniać blockSize (wartości nieparzyste: 3–51),
ii. zmieniać C w zakresie -20 do 20.
b. Umożliw interaktywną eksplorację wpływu tych parametrów na wynik
segmentacji.
c. Przetestuj zbudowany algorytm na przykładowym zdjęciu, dla którego
dobierzesz optymalne parametry C oraz blockSize.'''

import cv2
import numpy as np

image = cv2.imread("paczki.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

def update(val=0):
    block_size = cv2.getTrackbarPos("blockSize", "Segmentacja")
    c_val = cv2.getTrackbarPos("C", "Segmentacja") - 20  
    if block_size % 2 == 0:
        block_size += 1
    if block_size < 3:
        block_size = 3

    thresh = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY_INV,
        block_size,
        c_val
    )

    masked = cv2.bitwise_and(image, image, mask=thresh)

    cv2.imshow("Maska progowania", thresh)
    cv2.imshow("Obraz zamaskowany", masked)

cv2.namedWindow("Segmentacja")
cv2.createTrackbar("blockSize", "Segmentacja", 11, 51, update)  
cv2.createTrackbar("C", "Segmentacja", 20, 40, update)

update()

cv2.waitKey(0)
cv2.destroyAllWindows()

