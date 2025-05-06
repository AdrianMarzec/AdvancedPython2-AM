'''Numeryzacja kostek
a. Zmodyfikuj pętlę iterującą po konturach tak, by na każdej kostce (nad jej
środkiem) narysować numer porządkowy ( cv2.putText ).
b. Dodaj zapisywanie każdej wyciętej kostki do osobnego pliku kostka_01.png ,
kostka_02.png , itd.'''

import cv2
import imutils
import os

image = cv2.imread('cobblestone.jpg')
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

os.makedirs("kostki", exist_ok=True)

for i, c in enumerate(cnts, 1):
    c = c.astype("float") * ratio
    c = c.astype("int")

    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

    M = cv2.moments(c)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0

    cv2.putText(image, str(i), (cX - 10, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    x, y, w, h = cv2.boundingRect(c)
    tile = image[y:y+h, x:x+w]

    filename = f"kostki/kostka_{i:02}.png"
    cv2.imwrite(filename, tile)

cv2.imshow("Kostki ponumerowane", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
