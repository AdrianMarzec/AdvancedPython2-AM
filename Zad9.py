'''Dynamiczna zmiana rozmiaru w pętli
a. Stopniowo zwiększaj rozmiar obrazu od 100% do 300% w krokach co 20%.
b. Wyświetl każdą wersję na ekranie z krótkim opóźnieniem (cv2.waitKey(500)).'''

import cv2
import imutils
image = cv2.imread("wolf.jpg")
cv2.imshow("Original", image)
(h,w) = image.shape[:2]
for x in range(100,301,20):
    resized = imutils.resize(image, width=image.shape[1] * (x//10),
                             inter=cv2.INTER_CUBIC)
    cv2.imshow(f'{x}%', resized)
    cv2.waitKey(500)