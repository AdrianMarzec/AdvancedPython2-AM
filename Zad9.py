'''Zapis przyciętego obrazu
a. Przytnij obraz do obszaru o wymiarach 300x300 pikseli.
b. Zapisz wynik jako nowy plik cropped_image.jpg.'''

import cv2
import imutils

image = cv2.imread("wolf.jpg")
resized = imutils.resize(image, width=500)
cv2.imshow("Resized",resized)
roi = resized[0:300,0:300]

cv2.imshow("ROI",roi)
cv2.waitKey(0)

cv2.imwrite("cropped_image.jpg", roi)