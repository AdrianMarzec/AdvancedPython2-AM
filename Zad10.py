'''Obrót w pętli
a. Wykonaj pętlę, która obraca obraz co 15 stopni od 0 do 360 i wyświetla
każdą wersję na ekranie.
b. Dodaj opóźnienie cv2.waitKey(500) , aby obserwować zmiany.'''

import cv2
import imutils

image = cv2.imread('wolf.jpg')

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

for x in range(0,361,15):
    #image = imutils.rotate(image, x)
    M = cv2.getRotationMatrix2D((cX, cY), x, 1.0)
    image = cv2.warpAffine(image, M, (w, h))
    cv2.imshow(f"{x} Stopni",image)
    cv2.waitKey(500)

cv2.waitKey(0)
