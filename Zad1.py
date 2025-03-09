#Wczytaj i wyświetl obraz z podanej przez siebie ścieżki. Sprawdź, co się stanie, gdy podasz błędną ścieżkę.

import cv2
image = cv2.imread("ascii.jpg")
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    cv2.imshow("Obraz", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Obraz wczytano poprawnie.")
