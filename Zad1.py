'''Odbicie poziome
a. Wczytaj obraz i wykonaj odbicie lustrzane w poziomie.
b. Wyświetl wynik.'''

import cv2

image = cv2.imread("wolf.jpg")
cv2.imshow("Original", image)
print("[INFO] flipping image horizontally...")
flipped = cv2.flip(image, 1)
for x in range(10):
    cv2.imshow("Flipped Horizontally", flipped)
    flipped = cv2.flip(flipped, 1)
    cv2.waitKey(200)
