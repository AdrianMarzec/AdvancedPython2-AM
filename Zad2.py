'''Analiza cech uwidaczniających się w poszczególnych kanałach
a. Wybierz obraz, na którym znajdują się obiekty o różnych kolorach.
b. Porównaj, jak różne elementy obrazu są widoczne w poszczególnych
kanałach B, G, R.
c. Spróbuj znaleźć taki obiekt, który jest wyraźnie widoczny tylko na jednym
z kanałów.'''

import cv2

image = cv2.imread("flowers.jpg")
(B, G, R) = cv2.split(image)
# show each channel individually
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)
