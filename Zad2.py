'''Analiza wpływu rozmiaru kernela na efekt rozmycia
a. Zastosuj każdą z metod rozmycia do obrazu, używając różnych wartości
kernela: (3x3), (5x5), (9x9), (15x15).
b. Porównaj wyniki i odpowiedz na pytania (w formie komentarza w kodzie):
i. Jak zmienia się efekt rozmycia w zależności od wielkości kernela?
ii. Jaki rozmiar kernela jest optymalny dla redukcji szumu bez utraty
istotnych detali?'''

import cv2

kernelSize = [(3,3), (5,5), (9,9), (15,15)]

for size in kernelSize:
    image = cv2.imread("SamusPepe.jpg")
    cv2.imshow("Original", image)
    blurred = cv2.blur(image.copy(), size)
    cv2.imshow("Average", blurred)

    blurred = cv2.GaussianBlur(image.copy(), size, 0)
    cv2.imshow("Gaussian", blurred)

    blurred = cv2.medianBlur(image.copy(),size[0])
    cv2.imshow("Median", blurred)

    blurred = cv2.bilateralFilter(image.copy(), size[0],size[0],size[0])
    cv2.imshow("Bilateral", blurred)

    cv2.waitKey(0)

# Im większy kernel tym większe rozmycie
# 5x5 do 7x7 zdaje się być najbardziej optymalne
