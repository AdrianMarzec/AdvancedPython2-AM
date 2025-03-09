'''Wypełnienie konkretnego obszaru obrazu jednolitym kolorem
Pobierz współrzędne środka obrazu.
Wypełnij kwadrat o wymiarach 100x100 px, którego środek pokrywa się ze
środkiem obrazu, kolorem czerwonym (0, 0, 255).
Wyświetl obraz po zmianach.'''

import cv2
px = 100
image = cv2.imread('pies.jpg')
(h,w) = image.shape[:2]
(cX,cY) = (w//2,h//2)
print(cX,cY)

tl = (cY-px//2, cX-px//2)
br = (cY+px//2, cX+px//2)

image[tl[0]:br[0],tl[1]:br[1]] = (0,0,255)

cv2.imshow("Piesel", image)
cv2.waitKey(0)