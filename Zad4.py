#Wczytaj obraz w skali szarości i zapisz go jako nowy plik - znajdź w dokumentacji odpowiednią funkcję do tego.
import cv2

image = cv2.imread("dog.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("dogGRAY.jpg", image)