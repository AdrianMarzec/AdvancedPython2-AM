'''Symulacja efektu głębi ostrości (dobrze znana fraza w fotografii, jeśli jej nie
znasz, to zrób research)
a. Wybierz zdjęcie z obiektami w różnych odległościach od aparatu.
b. Spróbuj zasymulować efekt głębi ostrości, rozmywając tylko tło, a
pozostawiając główny obiekt wyraźny.
c. Możesz zrobić to, ręcznie maskując obszar tła i stosując cv2.GaussianBlur
tylko na nim.'''

import cv2
import numpy as np

image = cv2.imread("SamusPepe.jpg")

mask = np.zeros(image.shape[:2], dtype=np.uint8)

radius = 100
cv2.circle(mask, (385,95), radius, 255, -1)  #obszar ostrości

blurred = cv2.GaussianBlur(image, (21, 21), 0)

sharp = cv2.bitwise_and(image, image, mask=mask)
mask_back = cv2.bitwise_not(mask)
background = cv2.bitwise_and(blurred, blurred, mask=mask_back)
final = cv2.add(sharp, background)

# Wyświetlamy wynik
cv2.imshow("Simulated Depth of Field", final)
cv2.waitKey(0)
