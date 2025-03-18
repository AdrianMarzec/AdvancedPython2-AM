'''Porównanie efektów
a. Wyświetl cztery wersje obrazu:
i. Oryginał
ii. Odbicie poziome
iii. Odbicie pionowe
iv. Odbicie względem obu osi'''

import cv2

image = cv2.imread("wolf.jpg")
cv2.imshow("Original", image)
print("[INFO] flipping images...")
flipped = cv2.flip(image, 1)
flipped2 = cv2.flip(image, 0)
flipped3 = cv2.flip(image, -1)
for x in range(10):
    cv2.imshow("Flipped Horizontally", flipped)
    cv2.imshow("Flipped Vertically", flipped2)
    cv2.imshow("Flipped", flipped3)
    flipped = cv2.flip(flipped, 1)
    flipped2 = cv2.flip(flipped, 0)
    flipped3 = cv2.flip(flipped, -1)
    cv2.waitKey(200)