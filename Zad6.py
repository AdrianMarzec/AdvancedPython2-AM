'''Odbicie na podstawie wyboru użytkownika
a. Napisz skrypt, który wczytuje obraz i pyta użytkownika o sposób odbicia
( 0 – pionowe, 1 – poziome, -1 – oba).
b. Na podstawie wyboru wykonuje operację i wyświetla wynik.'''

import cv2

image = cv2.imread("wolf.jpg")
print("[INFO] flipping images...")
n = int(input("Podaj flipa (0, 1 lub -1): "))
flipped = cv2.flip(image, n)

cv2.imshow("Original", image)
cv2.imshow("Flipped", flipped)
cv2.waitKey(0)
