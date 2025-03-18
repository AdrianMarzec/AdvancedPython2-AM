'''Zastosowanie arytmetyki do detekcji zmian w obrazach
a. Wczytaj dwa obrazy tej samej sceny, ale z niewielkimi różnicami (np. obiekt przesunięty).
b. Oblicz ich różnicę (cv2.absdiff(image1, image2)).
c. Zinterpretuj wynik - jakie zmiany są widoczne?'''

import cv2
import imutils

image = cv2.imread("wolf.jpg")
image2 = cv2.imread("wolf.jpg")
shifted = imutils.translate(image, 0, 150)

cv2.imshow("Image", image)
cv2.imshow("Image2", shifted)


cv2.imshow("Roznica", cv2.absdiff(image, shifted))
cv2.waitKey(0)

print("""Różnica między obrazami wskazuje na zmiany w tych miejscach, 
    które zostały przesunięte, podczas gdy reszta obrazu pozostaje 
    niezmieniona. Wartości pikseli różniące się między dwoma obrazami są pokazane""")