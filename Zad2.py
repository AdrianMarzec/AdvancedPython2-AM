'''Eksperymentuj z metodą cv2.findContours
a. Na progowanym obrazie znajdź kontury przy użyciu funkcji cv2.findContours .
Narysuj wszystkie wykryte kontury na oryginalnym obrazie w kolorze
czerwonym o grubości 2px.
b. Zmieniaj tryby (parametr mode w funkcji findContours ), przetestuj
cv2.RETR_EXTERNAL , cv2.RETR_TREE i cv2.RETR_LIST i opisz różnice w komentarzu.'''

import cv2
import imutils

image = cv2.imread('cobblestone.jpg')
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(resized, 140, 255, cv2.THRESH_BINARY)[1]
cv2.imshow(f'thresh', thresh)
cv2.imshow('gray', resized)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts2 = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts3 = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts2 = imutils.grab_contours(cnts2)
cnts3 = imutils.grab_contours(cnts3)

for i, c in enumerate(cnts):
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    cv2.drawContours(image, [c], -1, (0, 0, 255), 2)
cv2.imshow(f"Image1", image)
cv2.waitKey(0)

for i, c in enumerate(cnts2):
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    cv2.drawContours(image, [c], -1, (0, 0, 255), 2)
cv2.imshow(f"Image2", image)
cv2.waitKey(0)

for i, c in enumerate(cnts3):
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    cv2.drawContours(image, [c], -1, (0, 0, 255), 2)
cv2.imshow(f"Image3", image)
cv2.waitKey(0)

# Różnice między trybami:
# RETR_EXTERNAL – wykrywa tylko zewnętrzne kontury (najmniej konturów).
# RETR_LIST – wykrywa wszystkie kontury bez hierarchii.
# RETR_TREE – wykrywa wszystkie kontury i tworzy pełną hierarchię zależności (kontury wewnątrz innych).
