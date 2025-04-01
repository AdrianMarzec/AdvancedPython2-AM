'''Rozmycie dwustronne w praktyce
a. Załaduj zdjęcie zawierające zarówno szum, jak i ostre krawędzie.
b. Zastosuj rozmycie dwustronne (cv2.bilateralFilter) z różnymi wartościami
parametrów.
c. Porównaj efekty z innymi metodami rozmycia.
d. Odpowiedz na pytania (w formie komentarza w kodzie):
i. Czy rozmycie dwustronne skutecznie redukuje szum?
ii. Czy zachowuje lepiej krawędzie w porównaniu do innych metod?
iii. Jakie wartości parametrów dają najlepsze rezultaty?'''

import cv2

image = cv2.imread("SamusPepe.jpg")

cv2.imshow("Samus", image)

blurred = cv2.bilateralFilter(image, 15,75,75)
cv2.imshow("Bilateral", blurred)

cv2.waitKey(0)

# Czy rozmycie dwustronne skutecznie redukuje szum?
# Tak, redukuje szum, ale zachowuje szczegóły obrazu.

# Czy zachowuje lepiej krawędzie w porównaniu do innych metod?
# Tak, lepiej zachowuje krawędzie niż tradycyjne filtry, np. Gaussa.

# Jakie wartości parametrów dają najlepsze rezultaty?
# d: 5-25, sigmaColor i sigmaSpace: 50-150. Dają dobrą równowagę między wygładzaniem a zachowaniem krawędzi.
