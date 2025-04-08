'''Wstęp do progowania
a. Wczytaj wskazany obraz, przekształć go do skali szarości, a następnie
zastosuj progowanie podstawowe dla wartości progowej:
i. T = 30
ii. T = 100
iii. T = 200
b. Porównaj uzyskane binarne obrazy. Która wartość progowa najlepiej
oddziela pierwszy plan od tła? Jeśli żadna to spróbuj dobrać odpowiednią.'''

import cv2

image = cv2.imread("cobblestone.jpg")
cv2.imshow("Image", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#blurred = cv2.GaussianBlur(gray, (7, 7), 0)

lista = [30,100,200]

for T in lista:
    (T, threshInv) = cv2.threshold(image, T, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow(f"Threshold Binary Inverse {T}", threshInv)

cv2.waitKey(0)

#Najlepiej wygląda T=100