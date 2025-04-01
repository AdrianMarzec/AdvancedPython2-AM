'''Eksperymentowanie z dylatacją
a. Pobierz obraz zawierający cienkie linie lub przerwy między obiektami.
b. Zastosuj dylatację z różnymi rozmiarami elementów strukturalnych.
c. Przedstaw wykres lub tabelę pokazującą, jak zmienia się grubość
obiektów w zależności od liczby iteracji dylatacji.'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('test.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

iter = list()
thickness = list()

for i in range(0, 3):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
    dilated = cv2.dilate(gray.copy(), kernel, iterations=i + 1)
    cv2.imshow("Dilated {} times".format(i + 1), dilated)
    thickness.append(np.sum(dilated==255))
    iter.append(i+1)
    cv2.waitKey(0)

print("Grubość: ",thickness)
print("Iteracja: ",iter)
plt.plot(iter, thickness, marker='o')
plt.xlabel('Iteracja')
plt.ylabel('Grubość')
plt.title('Zmiana grubości obiektów w wyniku dylatacji')
plt.grid(True)
plt.show()