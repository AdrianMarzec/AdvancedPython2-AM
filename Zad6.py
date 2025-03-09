#Zmień rozmiar okna wyświetlania obrazu tak, by dostosować je do różnych
#ekranów, np. cv2.WINDOW_NORMAL - znajdź w dokumentacji odpowiednią funkcję
#do tego.

import cv2
image = cv2.imread("dogGRAY.jpg")
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    cv2.namedWindow("Okno", cv2.WINDOW_NORMAL)
    cv2.imshow("Okno", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Obraz wczytano poprawnie.")