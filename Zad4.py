'''Segmentacja tekstu w dokumencie
a. Wczytaj obraz dokumentu (np. zdjęcie notatki z telefonu). Zastosuj
progowanie adaptacyjne, aby wyodrębnić tekst.
b. Wyświetl binarny obraz, na którym tekst będzie dobrze widoczny, nawet
jeśli oryginał jest nierówno doświetlony.'''

import cv2

image = cv2.imread("paragon.jpg")
cv2.imshow("Image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)


thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 0.69)
cv2.imshow(f"Mean Adaptive Thresholding {11}", thresh)

cv2.waitKey(0)
