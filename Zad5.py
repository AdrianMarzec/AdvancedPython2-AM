'''Porównanie skuteczności redukcji szumów
a. Dodaj do obrazu sztuczny szum (np. cv2.randn() do dodania szumu Gaussa
lub cv2.randu() do szumu soli i pieprzu)
b. Następnie zastosuj różne metody rozmycia i oceń, która najlepiej usuwa
szum, zachowując detale obrazu.'''

import cv2

kernelSize = [(7,7)]
image = cv2.imread("SamusPepe.jpg")
cv2.imshow("Original", image)
cv2.randn(image,0,150)
cv2.imshow("Szum Gaussa", image)
cv2.randu(image,0,150)
cv2.imshow("Szum Soli i Pieprzu", image)
cv2.waitKey(0)

for size in kernelSize:
    blurred = cv2.blur(image.copy(), size)
    cv2.imshow("Average", blurred)

    blurred = cv2.GaussianBlur(image.copy(), size, 0)
    cv2.imshow("Gaussian", blurred)

    blurred = cv2.medianBlur(image.copy(),size[0])
    cv2.imshow("Median", blurred)

    blurred = cv2.bilateralFilter(image.copy(), 70,70,70)
    cv2.imshow("Bilateral", blurred)

    cv2.waitKey(0)
