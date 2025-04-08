'''Analiza histogramu
a. wygeneruj histogram skali szarości ( cv2.calcHist )
b. zaznacz na nim wartość progową wyliczoną przez Otsu
c. Czy na histogramie można wyraźnie dostrzec dwa zbiory intensywności
(tło vs obiekt)? Jak Otsu wybiera próg?'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Wczytaj obraz
image = cv2.imread("cobblestone.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

plt.figure(figsize=(10, 6))
plt.title("Histogram Skali Szarości")
plt.xlabel("Intensywność Pikseli")
plt.ylabel("Częstotliwość")

plt.plot(hist)
plt.axvline(x=ret, color='r', linestyle='dashed', linewidth=2)
plt.text(ret + 10, max(hist) * 0.9, f"Próg Otsu: {ret:.2f}", color='r')

cv2.imshow("Otsu Threshold", thresh)
plt.show()

cv2.waitKey(0)

'''
Tak, jeśli obraz ma wyraźny kontrast między tłem a obiektem, histogram powinien to wykazywać
Algorytm Otsu wybiera próg, który minimalizuje sumę wariancji wewnątrz dwóch klas (tło i obiekt).
Stara się znaleźć taki punkt, który najlepiej rozdzieli te dwie grupy intensywności, co prowadzi do jak najczystszej segmentacji
'''