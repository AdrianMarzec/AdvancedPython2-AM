#Wczytaj zdjęcie w odcieniach szarości i wyświetl liczbę kanałów
import cv2

image_gray = cv2.imread("dog.jpg", cv2.IMREAD_GRAYSCALE)


(h, w) = image_gray.shape[:2]
if len(image_gray.shape) == 2:
    c = 1
else:
    c = image_gray.shape[2]
    
cv2.imshow(f'WIDTH: {w} pixels, HEIGHT: {h} pixels, CHANNELS: {c}', image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()