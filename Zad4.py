'''Wzmocnienie jednego z kanałów
a. Zwiększ intensywność jednego z kanałów (np. kanału czerwonego) i
zaobserwuj, jak wpływa to na końcowy wygląd obrazu.
b. Możesz to zrobić poprzez dodanie stałej wartości do danego kanału, np. R = cv2.add(R, 50) .'''

import cv2

image = cv2.imread("flowers.jpg")
(B, G, R) = cv2.split(image)
# show each channel individually
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

R = cv2.add(R, 50)
cv2.imshow("Red2", R)

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

cv2.waitKey(0)
