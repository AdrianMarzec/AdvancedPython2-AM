'''Wpływ oświetlenia
a. Zwiększ jasność obrazu o wartość 50 (np. dodając +50 do każdego
piksela w skali szarości).
b. Zastosuj podstawowe progowanie (np. T = 100) na obrazie oryginalnym i
rozjaśnionym. Jak zmienia się wynik? Co to mówi o czułości tej metody?'''

import cv2

image = cv2.imread("cobblestone.jpg")
cv2.imshow("Image", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.add(gray,50)
cv2.imshow("Gray", gray)

(T, threshInv) = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow(f"Original {T}", threshInv)

(T, threshInv) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow(f"Lighted {T}", threshInv)

cv2.waitKey(0)
