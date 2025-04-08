'''Wizualizacja składowych RGB i HSV
a. Wybierz dowolny obraz (najlepiej z wyraźnymi kolorami) i wczytaj go do
programu.
b. Przekonwertuj obraz do przestrzeni RGB i wyświetl go.
c. Rozdziel obraz na trzy kanały (R, G, B) i wyświetl je osobno.
d. Przekonwertuj obraz do przestrzeni HSV i wyświetl go.
e. Rozdziel obraz na trzy kanały (H, S, V) i wyświetl je osobno.
f. Porównaj wpływ poszczególnych kanałów na wygląd obrazu.'''

import cv2

image = cv2.imread("SamusPepe.jpg")

for (name, chan) in zip(("B", "G", "R"), cv2.split(image)):
    cv2.imshow(name, chan)

cv2.imshow("Original", image)
cv2.waitKey(0)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
for (name, chan) in zip(("H", "S", "V"), cv2.split(hsv)):
    cv2.imshow(name, chan)

cv2.waitKey(0)