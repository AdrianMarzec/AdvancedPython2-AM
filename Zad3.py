#Wczytaj zdjęcie w odcieniach szarości i wyświetl liczbę kanałów
import cv2

image_gray = cv2.imread("ascii.jpg", cv2.IMREAD_GRAYSCALE)

(h, w, c) = image_gray.shape[:3]
print(f'width: {w} pixels')
print(f'height: {h} pixels')
print(f'channels: {c}')