'''Przygotowanie własnego przykładu zastosowania operacji morfologicznych
a. Wybierz realny przypadek użycia (np. poprawa czytelności tablic
rejestracyjnych, usuwanie szumu z dokumentów zeskanowanych, analiza obrazów medycznych).
b. Zastosuj odpowiednie operacje morfologiczne i zaprezentuj ich wpływ na
poprawę jakości analizy obrazu.'''

import cv2

image = cv2.imread('auto.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (7,7))

cv2.waitKey(0)

dilated = cv2.erode(gray, kernel)
dilated = cv2.erode(dilated, kernel)
dilated = cv2.erode(dilated, kernel)
cv2.imshow("Dilated: ({}, {})".format(7,7), dilated)

gradient = cv2.morphologyEx(dilated, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Gradient: ({}, {})".format(7,7), gradient)
cv2.waitKey(0)