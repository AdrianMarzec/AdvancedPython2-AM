'''Odbicie pionowe
a. Wykonaj odbicie lustrzane w pionie.
b. Porównaj wynik z obrazem oryginalnym.'''

import cv2

image = cv2.imread("wolf.jpg")
cv2.imshow("Original", image)
print("[INFO] flipping image vertically...")
flipped = cv2.flip(image, 0)
for x in range(20):
    cv2.imshow("Flipped vertically", flipped)
    flipped = cv2.flip(flipped, 0)
    cv2.waitKey(200)
