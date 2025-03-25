'''Wyświetlenie pojedynczych kanałów na obrazie
a. Wczytaj dowolny obraz.
b. Rozdziel kanały B, G, R i wyświetl je osobno.
c. Zapisz te kanały jako osobne obrazy.'''

import cv2

image = cv2.imread("flowers.jpg")
(B, G, R) = cv2.split(image)
# show each channel individually
cv2.imshow("Red", R)
cv2.imwrite("RED.jpg",R)
cv2.imshow("Green", G)
cv2.imwrite("GREEN.jpg",G)
cv2.imshow("Blue", B)
cv2.imwrite("BLUE.jpg",B)
cv2.waitKey(0)
