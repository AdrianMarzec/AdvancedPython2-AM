#Wczytaj zdjęcie w kolorze i wyświetl liczbę kanałów.
import cv2

image = cv2.imread("dog.jpg")
(h, w, c) = image.shape[:3]

cv2.imshow(f'WIDTH: {w} pixels, HEIGHT: {h} pixels, CHANNELS: {c}', image)
cv2.waitKey(0)
cv2.destroyAllWindows()