'''Klasyczne progowanie
a. Wczytaj obraz z kostką brukową, przeskaluj go do szerokości 300 px i
zastosuj progowanie klasyczne ( cv2.threshold ) dla różnych wartości
progowania (np. 100, 140, 180).
b. Zaobserwuj, jak zmienia się jakość segmentacji kostek. Która wartość
progowania najlepiej rozdziela kostki od tła?'''

import cv2
import imutils

image = cv2.imread('cobblestone.jpg')
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)


for x in (100,140,180):
    thresh = cv2.threshold(resized, x, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow(f'thresh {x}', thresh)
    cv2.imshow('gray', resized)

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for i, c in enumerate(cnts):
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.imshow(f"Image {x}", image)
    cv2.waitKey(0)
