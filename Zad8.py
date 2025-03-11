'''Obrót sekwencyjny
a. Wykonaj trzy obroty po 30 stopni wokół środka obrazu i wyświetl wynik
końcowy.
b. Sprawdź, czy wynik różni się od pojedynczego obrotu o 90 stopni.'''

import cv2
import imutils

image = cv2.imread('wolf.jpg')
imageB = cv2.imread('wolf.jpg')

rotation = 30
angle = 90

imu = imutils.rotate(image, angle)
for x in range(3):
    image = imutils.rotate(image, rotation)


cv2.imshow("three",image)
cv2.imshow("one",imu)
cv2.waitKey(0)
