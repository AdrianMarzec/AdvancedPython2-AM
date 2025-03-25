'''Kombinacja różnych kształtów i operacji bitowych
a. Narysuj trójkąt i porównaj go z okręgiem, wykorzystując różne operacje
bitowe ( AND , OR , XOR , NOT ).
b. Sprawdź, jak zmieniają się wyniki w zależności od pozycji kształtów.'''

import numpy as np
import cv2

triangle = np.zeros((300, 300), dtype = "uint8")
points = np.array([(0,300),(150,0),(300,300)])
cv2.drawContours(triangle, [points],0, (255,255,255),-1)
cv2.imshow("Triangle", triangle)

circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)


bitwiseAnd = cv2.bitwise_and(triangle, circle)
cv2.imshow("AND", bitwiseAnd)

bitwiseOr = cv2.bitwise_or(triangle, circle)
cv2.imshow("OR", bitwiseOr)

bitwiseOr = cv2.bitwise_xor(triangle, circle)
cv2.imshow("XOR", bitwiseOr)

bitwiseOr = cv2.bitwise_not(triangle, circle)
cv2.imshow("NOT", bitwiseOr)

cv2.waitKey(0)

