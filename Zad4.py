'''Zamiana wartości piksela na czarny
a. Pobierz od użytkownika współrzędne (x, y).
b. Stwórz walidację, która zweryfikuje czy podane współrzędne nie
wychodzą poza wymiar zdjęcia.
c. Ustaw piksel w tym miejscu na czarny (0, 0, 0).'''

import cv2

image = cv2.imread('pies.jpg')
(h,w) = image.shape[:2]

try:
    x = int(input("Podaj x "))
    y = int(input("Podaj y "))

    if x<=w and x>=0 and y<=h and y>=0:
        image[y,x] = (0,0,0)
        cv2.imshow(f"Zmiana Pixela {x},{y} na czarny", image)
        cv2.waitKey(0)
    else:
        print("Współrzędne wychodzą poza wymiar zdjęcia")

except (ValueError, TypeError):
    print("Podano błędną wartość!")