'''Wpływ rozmiaru sąsiedztwa
a. Na tym samym obrazie zastosuj cv2.adaptiveThreshold z różnymi wartościami
parametru blockSize : 11, 21, 31, 41
b. Który rozmiar najlepiej radzi sobie z detekcją konturów przy silnych
różnicach w oświetleniu?'''

import cv2

image = cv2.imread("cobblestone.jpg")
cv2.imshow("Image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)


lista = [11, 21, 31, 41]
for size in lista:
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, size, 0.69)
    cv2.imshow(f"Mean Adaptive Thresholding {size}", thresh)

cv2.waitKey(0)

#11
