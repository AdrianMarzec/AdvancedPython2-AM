'''Zmiana rozmiaru i zapis pliku
a. Powiększ obraz do szerokości 800 pikseli i zapisz wynik do pliku
resized_output.jpg .'''

import cv2
import imutils
image = cv2.imread("wolf.jpg")
cv2.imshow("Original", image)
resized = imutils.resize(image, width=800, inter=cv2.INTER_CUBIC)
cv2.imshow(f'Resized', resized)
cv2.waitKey(0)
cv2.imwrite("resized_output.jpg", resized)
