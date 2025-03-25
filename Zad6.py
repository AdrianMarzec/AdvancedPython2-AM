'''Eksperymentowanie z logiem OpenCV
a. Pobierz logo OpenCV i rozdziel jego kanały.
b. Spróbuj zamienić kolory tak, aby wyglądało inaczej, np. zamienić niebieski
z czerwonym.
c. Spróbuj usunąć jeden kanał całkowicie i sprawdź, jak wpłynie to na wygląd loga.'''

import cv2
import numpy as np

image = cv2.imread("logo.jpg")
cv2.imshow("Original", image)
(B, G, R) = cv2.split(image)
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

merged = cv2.merge([R,G,B])
cv2.imshow("Merged", merged)

G = np.zeros(image.shape[:2], dtype="uint8")
merged = cv2.merge([B,G,R])
cv2.imshow("Merged", merged)

cv2.waitKey(0)
