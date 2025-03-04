#Wczytaj zdjęcie w kolorze i wyświetl liczbę kanałów.
import cv2

image = cv2.imread("example.jpg")
(h, w, c) = image.shape[:3]
print(f'width: {w} pixels')
print(f'height: {h} pixels')
print(f'channels: {c}')