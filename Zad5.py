'''Eksperymentowanie z różnymi elementami strukturalnymi
a. Wybierz jeden obraz testowy i wykonaj na nim wszystkie podstawowe
operacje morfologiczne (erozja, dylatacja, otwarcie, zamknięcie, gradient).
b. Powtórz eksperyment, zmieniając kształt elementu strukturalnego (np.
kwadrat, krzyż, elipsa).
c. Porównaj wyniki i opisz, jakie różnice zauważasz w przetworzonych
obrazach.'''

import cv2

image = cv2.imread('wolf.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (7,7))


eroded = cv2.erode(gray.copy(), kernel)
cv2.imshow("Eroded: ({}, {})".format(7,7), eroded)
dilated = cv2.dilate(eroded, kernel)
cv2.imshow("Dilated: ({}, {})".format(7,7), eroded)
opening = cv2.morphologyEx(dilated, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening: ({}, {})".format(7,7), opening)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing: ({}, {})".format(7,7), closing)
cv2.waitKey(0)


kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))

eroded = cv2.erode(gray.copy(), kernel)
cv2.imshow("Eroded: ({}, {})".format(7,7), eroded)
dilated = cv2.erode(eroded, kernel)
cv2.imshow("Dilated: ({}, {})".format(7,7), eroded)
opening = cv2.morphologyEx(dilated, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening: ({}, {})".format(7,7), opening)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing: ({}, {})".format(7,7), closing)
cv2.waitKey(0)


kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))

eroded = cv2.erode(gray.copy(), kernel)
cv2.imshow("Eroded: ({}, {})".format(7,7), eroded)
dilated = cv2.erode(eroded, kernel)
cv2.imshow("Dilated: ({}, {})".format(7,7), eroded)
opening = cv2.morphologyEx(dilated, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening: ({}, {})".format(7,7), opening)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing: ({}, {})".format(7,7), closing)
cv2.waitKey(0)
