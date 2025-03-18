'''Odbicie względem obu osi
a. Odbij obraz zarówno poziomo, jak i pionowo (czyli względem obu osi).'''

import cv2

image = cv2.imread("wolf.jpg")
cv2.imshow("Original", image)
print("[INFO] flipping image...")
flipped = cv2.flip(image, -1)
for x in range(20):
    cv2.imshow("Flipped", flipped)
    flipped = cv2.flip(flipped, -1)
    cv2.waitKey(200)
