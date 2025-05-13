'''Przetestuj odporność algorytmu na "fałszywe trafienia".
a. Wczytaj obraz z wieloma podobnymi obiektami (np. klocki LEGO,
opakowania).
b. Wytnij jeden jako szablon.
c. Spróbuj wykryć jego wystąpienia.
d. Czy pojawiły się błędne detekcje? Jak to wyeliminować?'''

import cv2
import numpy as np

# Wczytaj obrazy
image = cv2.imread('5full.png')
template = cv2.imread('6music.png')

imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Dopasowanie szablonu
result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)

# Próg dopasowania – im wyższy, tym mniej fałszywych trafień
threshold = 0.9

#Wszystkie dopasowania powyżej progu
(yCoords, xCoords) = np.where(result >= threshold)

# Współrzędne zaznaczonych obszarów
for (x, y) in zip(xCoords, yCoords):
    cv2.rectangle(
        image,
        (x, y),
        (x + template.shape[1], y + template.shape[0]),
        (0, 255, 0),
        2
    )

cv2.imshow("Detected", image)
cv2.imshow("Template", template)
cv2.waitKey(0)
cv2.destroyAllWindows()

