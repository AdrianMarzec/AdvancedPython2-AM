#Wczytaj i wyświetl obraz z podanej przez siebie ścieżki. Sprawdź, co się stanie, gdy podasz błędną ścieżkę.

import cv2
# Wczytanie obrazu z pliku
image = cv2.imread("ascii.jpg")
# Sprawdzenie, czy obraz został poprawnie wczytany
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")