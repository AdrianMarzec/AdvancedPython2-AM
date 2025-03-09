'''Kolorowanie fragmentu obrazu
a. Podziel obraz na 4 równe części (ćwiartki).
b. Wypełnij lewą górną ćwiartkę kolorem niebieskim (255, 0, 0) .
c. Wyświetl obraz po zmianach.'''

import cv2

image = cv2.imread('pies.jpg')
(h,w) = image.shape[:2]
(cX,cY) = (w//2,h//2)
print(cX,cY)
topLeft = image[0:cY, 0:cX]
topRight = image[0:cY, cX:w]
bottomRight = image[cY:h, cX:w]
bottomLeft = image[cY:h, 0:cX]
cv2.imshow("Top-Left Corner", topLeft)
cv2.imshow("Top-Right Corner", topRight)
cv2.imshow("Bottom-Right Corner", bottomRight)
cv2.imshow("Bottom-Left Corner", bottomLeft)

image[0:cY, 0:cX] = (255,0,0)

cv2.imshow("Piesel", image)
cv2.waitKey(0)