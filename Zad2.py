'''Modyfikacja pojedynczego piksela
a. Zmień kolor piksela w prawym dolnym rogu obrazu na czerwony (0, 0, 255) .
b. Wyświetl obraz przed i po zmianie.'''

import cv2

obrazy = list()

przed = cv2.imread("pies.jpg")
po = cv2.imread("pies.jpg")


(h,w) = po.shape[:2]
print(f"{h}\n{w}")
(b,g,r) = po[h-1,w-1]
print(f"Pixel przed zmianą: - Red {r}, Green {g}, Blue {b}")
po[h-1,w-1] = (0,0,255)

obrazy.append(przed)
obrazy.append(po)


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
