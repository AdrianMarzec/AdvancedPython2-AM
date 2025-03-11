'''Obrót i zapis obrazu
a. Obróć obraz o 75 stopni i zapisz wynik do pliku rotated_output.jpg.'''

import cv2
import imutils

image = cv2.imread('wolf.jpg')
rotation = 75

imu = imutils.rotate(image, rotation)

cv2.imwrite('rotated_output.jpg',imu)
