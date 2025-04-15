'''Porównanie metod progowania
a. Wczytaj obraz z nierównym oświetleniem (np. kostka brukowa). Zastosuj
trzy metody progowania:
i. proste progowanie (wartość T=100),
ii. Otsu
iii. progowanie adaptacyjne (Mean i Gaussian).
b. Porównaj wyniki. Która metoda najlepiej poradziła sobie z nierównym
światłem?'''


import cv2

#Proste T=100
image = cv2.imread("cobblestone.jpg")
cv2.imshow("Image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
lista = [100]
for T in lista:
    (T, threshInv) = cv2.threshold(image, T, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow(f"Threshold Binary Inverse {T}", threshInv)

#OTSU
image = cv2.imread("cobblestone.jpg")
cv2.imshow("Image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
(T, threshInv) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("OTSU", threshInv)

#Adaptacyjne
image = cv2.imread("cobblestone.jpg")
cv2.imshow("Image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 5, 0.69)
cv2.imshow("Mean Adaptive Thresholding", thresh)

image = cv2.imread("cobblestone.jpg")
gaussian = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 5, 0.69)
cv2.imshow("Gaussian Adaptive Thresholding", thresh)
cv2.waitKey(0)


cv2.waitKey(0)
