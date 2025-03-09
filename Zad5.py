#Otwórz dwa obrazy jednocześnie w osobnych oknach. Upewnij się, że można je zamknąć niezależnie.
import cv2

obrazy = list()

imageA = cv2.imread("dog.jpg")
imageB = cv2.imread("ascii.jpg")

obrazy.append(imageA)
obrazy.append(imageB)

if any(img is None for img in obrazy):
    print("Błąd: nie można wczytać obrazu!")
else:
    i = 1
    for x in obrazy:
        cv2.imshow(f"Obraz{i}", x)
        i+=1

    n = len(obrazy)
    while n!=0:
        key = cv2.waitKey(0)

        cv2.destroyWindow(f"Obraz{n}")
        n-=1
