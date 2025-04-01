'''Analiza wpływu rozmycia na tekst na obrazie
a. Znajdź lub przygotuj obraz zawierający tekst (np. logo, znak drogowy,
nagłówek gazety).
b. Zastosuj różne metody rozmycia (cv2.blur, cv2.GaussianBlur,
cv2.medianBlur, cv2.bilateralFilter) z różnymi parametrami.
c. Odpowiedz na pytania:
i. Które metody najmocniej rozmywają tekst?
ii. Które pozwalają zachować jego czytelność?'''

import cv2

kernelSize = [(3,3), (5,5), (7,7), (9,9)]

for size in kernelSize:
    image = cv2.imread("ascii.jpg")
    cv2.imshow("Original", image)
    blurred = cv2.blur(image.copy(), size)
    cv2.imshow("Average", blurred)

    blurred = cv2.GaussianBlur(image.copy(), size, 0)
    cv2.imshow("Gaussian", blurred)

    blurred = cv2.medianBlur(image.copy(),size[0])
    cv2.imshow("Median", blurred)

    blurred = cv2.bilateralFilter(image.copy(), 77,77,77)
    cv2.imshow("Bilateral", blurred)

    cv2.waitKey(0)

# Które metody najmocniej rozmywają tekst?
# Najgorzej do Najlepiej: Median -> Average -> Gaussian -> Bilateral

# Które pozwalają zachować jego czytelność?
# Bilateral zachowuje czytelność
