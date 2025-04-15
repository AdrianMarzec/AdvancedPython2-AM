'''Różne metody adaptacyjne
a. Zastosuj dwie metody:
i. cv2.ADAPTIVE_THRESH_MEAN_C
ii. cv2.ADAPTIVE_THRESH_GAUSSIAN_C
b. Dla każdej z nich przetestuj różne wartości C (np. 2, 5, 10, 15).
c. Która metoda i jaki parametr C lepiej radzi sobie z szumem i nierównym tłem?'''

import cv2

image = cv2.imread("cobblestone.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

c_values = [2, 5, 10, 15]
block_size = 11

for c in c_values:
    # Adaptive Threshold – Mean
    thresh_mean = cv2.adaptiveThreshold(
        blurred, 255, 
        cv2.ADAPTIVE_THRESH_MEAN_C, 
        cv2.THRESH_BINARY_INV, 
        block_size, c
    )
    cv2.imshow(f"Mean C={c}", thresh_mean)

    # Adaptive Threshold – Gaussian
    thresh_gaussian = cv2.adaptiveThreshold(
        blurred, 255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY_INV, 
        block_size, c
    )
    cv2.imshow(f"Gaussian C={c}", thresh_gaussian)

cv2.waitKey(0)

