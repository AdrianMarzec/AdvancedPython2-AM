'''Znajdowanie najjaśniejszego piksela w obrazie
a. Przeszukaj cały obraz i znajdź piksel o najwyższej wartości jasności.
b. Wyświetl jego współrzędne i wartość.'''

import cv2

image = cv2.imread('pies.jpg')
(h,w) = image.shape[:2]
max = 0
k = 0
l = 0

for i in range(h):
    for j in range(w):
        (b, g, r) = image[i,j]
        bright = (int(r)+int(g)+int(b))/3
        if bright > max:
            max = bright
            k = i
            l = j

print(f"Najjaśniejszy jest Pixel {k},{l} - ma jasność {max}")
