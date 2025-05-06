'''Liczenie i raportowanie kostek
a. Na końcu całego procesu wyświetl w terminalu:
i. liczbę wykrytych kostek
ii. ich średnią szerokość i wysokość
iii. minimalny i maksymalny rozmiar'''


import cv2
import imutils
import numpy as np

image = cv2.imread('cobblestone.jpg')
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

widths = []
heights = []

for i, c in enumerate(cnts, 1):
    c = c.astype("float") * ratio
    c = c.astype("int")

    x, y, w, h = cv2.boundingRect(c)

    widths.append(w)
    heights.append(h)

    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

    M = cv2.moments(c)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0

    label = f"{cX}x{cY} px"
    cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 1)

if widths and heights:
    num_tiles = len(widths)
    avg_width = np.mean(widths)
    avg_height = np.mean(heights)
    min_size = (min(widths), min(heights))
    max_size = (max(widths), max(heights))

    print("== RAPORT KOSTEK ==")
    print(f"Liczba wykrytych kostek: {num_tiles}")
    print(f"Średnia szerokość: {avg_width:.2f} px")
    print(f"Średnia wysokość: {avg_height:.2f} px")
    print(f"Minimalny rozmiar: {min_size[0]} x {min_size[1]} px")
    print(f"Maksymalny rozmiar: {max_size[0]} x {max_size[1]} px")
else:
    print("Nie wykryto żadnych kostek.")

cv2.imshow("Kostki ponumerowane", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
