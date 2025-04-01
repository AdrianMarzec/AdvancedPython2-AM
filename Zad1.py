'''Analiza wpływu erozji na obrazy
a. Wczytaj obraz binarny zawierający różne kształty (np. figury
geometryczne lub tekst).
b. Zastosuj operację erozji z różnymi elementami strukturalnymi (np.
kwadratowym i eliptycznym).
c. Opisz, jak zmienia się struktura obiektów w wyniku erozji.'''

import cv2

image = cv2.imread('test.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
for i in range(0, 3):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
    eroded = cv2.erode(gray.copy(), kernel, iterations=i + 1)
    cv2.imshow("Eroded {} times".format(i + 1), eroded)
    cv2.waitKey(0)

print("""Figury się zmniejszają""")
