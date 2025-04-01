'''Eksploracja różnych metod rozmycia
a. Załaduj dowolny obraz i zastosuj do niego cztery różne metody rozmycia
i. proste rozmycie cv2.blur
ii. rozmycie Gaussa cv2.GaussianBlur
iii. rozmycie medianowe cv2.medianBlur
iv. rozmycie dwustronne cv2.bilateralFilter
b. Dla każdej metody porównaj efekty wizualne przy różnych wartościach
parametrów kernela. Odpowiedz na pytania (w formie komentarza w
kodzie):
i. Która metoda najlepiej usuwa szum?
ii. Która metoda zachowuje najwięcej szczegółów?
iii. Jakie są zalety i wady każdej metody?'''

import cv2

image = cv2.imread("SamusPepe.jpg")
cv2.imshow("Original", image)
blurred = cv2.blur(image.copy(), (7,7))
cv2.imshow("Average ({}, {})".format(7,7), blurred)

blurred = cv2.GaussianBlur(image.copy(), (7,7), 0)
cv2.imshow("Gaussian ({}, {})".format(7,7), blurred)

blurred = cv2.medianBlur(image.copy(),7)
cv2.imshow("Median ({}, {})".format(7,7), blurred)

blurred = cv2.bilateralFilter(image.copy(), 77, 77, 77)
cv2.imshow("Bilateral({}, {})".format(7,7), blurred)

cv2.waitKey(0)

# Odpowiedzi na pytania:

# Która metoda najlepiej usuwa szum?
# Rozmycie dwustronne najlepiej usuwa szum, zachowując szczegóły.

# Która metoda zachowuje najwięcej szczegółów?
# Rozmycie dwustronne zachowuje najwięcej szczegółów.

# Jakie są zalety i wady każdej metody?
# - Proste rozmycie (cv2.blur): Zaleta - szybkie, wada - nie zachowuje szczegółów, może zniekształcać obraz.
# - Rozmycie Gaussa (cv2.GaussianBlur): Zaleta - łagodne rozmycie, wada - może zniekształcać krawędzie przy dużych kernelach.
# - Rozmycie medianowe (cv2.medianBlur): Zaleta - świetne do usuwania soli i pieprzu, wada - nie zawsze zachowuje szczegóły.
# - Rozmycie dwustronne (cv2.bilateralFilter): Zaleta - doskonałe do zachowania szczegółów, wada - wolniejsze obliczenia.
