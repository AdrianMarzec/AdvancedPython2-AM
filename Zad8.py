'''Animacja przesuwającego się ROI
a. Wczytaj obraz i dynamicznie przesuwaj ROI w poziomie (np. przesunięcie
co 10 pikseli), aby stworzyć efekt „przesuwania kamery”.
b. Wyświetlaj na ekranie kolejne wycinki ROI po kliknięciu w klawiature.'''

import cv2

image = cv2.imread("wolf.jpg")
cv2.imshow("Original", image)
(h,w) = image.shape[:2]
cv2.waitKey(0)
print(h,w)
start = 0
end = 40

while end < w:
    roi = image[0:h, start:end]
    cv2.imshow("ROI", roi)
    if cv2.waitKey(0):
        start+=20
        end+=20

print("Koniec")
cv2.waitKey(0)