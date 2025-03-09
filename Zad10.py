'''Sprawdzenie różnicy wartości pikseli
a. Pobierz wartości pikseli w dwóch różnych miejscach obrazu i porównaj je
(np. (50,50) i (200,200)).
b. Wypisz różnice w wartościach R, G, B.'''

import cv2

image = cv2.imread('pies.jpg')

(b, g, r) = image[50,50]
info = f"Pixel at (50,50) - Red {r}, Green {g}, Blue {b}"

(b2,g2,r2) = image[200,200]
info2 = f"Pixel at (200,200) - Red {r2}, Green {g2}, Blue {b2}"

print(f'{info}\n{info2}')
info3 = f"Roznice: R - {abs(int(r) - int(r2))}, G - {abs(int(g) - int(g2))}, B - {abs(int(b) - int(b2))}"
print(info3)

cv2.imshow(info3, image)
cv2.waitKey(0)