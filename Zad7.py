'''Wycięcie fragmentu obrazu
a. Podziel obraz na 9 równych części.
b. Pobierz fragment obrazu obejmujący środek.
c. Wyświetl wycięty fragment osobno.'''

import cv2

image = cv2.imread('pies.jpg')
(h,w) = image.shape[:2]
(cX,cY) = (w//3,h//3)
print(cX,cY)
topLeft = image[0:cY, 0:cX]
topCenter = image[0:cY,cX:w-cX]
topRight = image[0:cY, cX+cX:w]

bottomLeft = image[cY+cY:h,0:cX]
bottomCenter = image[cY+cY:h, cX:w-cX]
bottomRight = image[cY+cY:h, cX+cX:w]

center = image[cY:h-cY,cX:w-cX]
left = image[cY:h-cY,0:cX]
right = image[cY:h-cY,cX+cX:w]
#cv2.imshow("Top-Left Corner", topLeft)
#cv2.imshow("Top-Center", topCenter)
#cv2.imshow("Top-Right Corner", topRight)

#cv2.imshow("Bottom-Left Corner", bottomLeft)
#cv2.imshow("Bottom-Center", bottomCenter)
#cv2.imshow("Bottom-Right Corner", bottomRight)

#cv2.imshow("Left", left)
#cv2.imshow("Right", right)


cv2.imshow("Piesel", image)
cv2.imshow("CENTER", center)
cv2.waitKey(0)