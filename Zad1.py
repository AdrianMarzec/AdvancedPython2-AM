'''Wybór ROI na podstawie współrzędnych
a. Zdefiniuj ROI, który obejmuje lewy górny róg obrazu o wymiarach 100x100 pikseli.
b. Wyświetl wynik.'''

import cv2

image = cv2.imread("wolf.jpg")
print("[INFO] flipping images...")
roi = image[:100, :100]
cv2.imshow("Original", image)
cv2.imshow("ROI", roi)
cv2.waitKey(0)
