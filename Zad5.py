'''Detekcja małych ikon interfejsu
a. Wybierz zrzut ekranu aplikacji (np. ikonę kosza, lupy, itp.).
b. Wyodrębnij mały fragment jako szablon.
c. Wykonaj dopasowanie na pełnym zrzucie.
d. Zaznacz wynik i porównaj z oczekiwanym.'''

import cv2

image = cv2.imread('5full.png')
#image = imutils.rotate(image, 45)
template = cv2.imread('5star.jpg')
cv2.imshow("Image", image)
cv2.imshow("Template", template)
# convert both the image and template to grayscale
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
# perform template matching
result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
# determine the starting and ending (x, y)-coordinates of the bounding box
(startX, startY) = maxLoc
endX = startX + template.shape[1]
endY = startY + template.shape[0]
# draw the bounding box on the image
cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 3)
# show the output image
cv2.imshow("Output", image)
print(maxVal)
cv2.waitKey(0)
