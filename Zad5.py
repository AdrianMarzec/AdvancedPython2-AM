'''Pomiar wymiarów kostek
a. Dla każdej wykrytej kostki:
i. Oblicz jej szerokość i wysokość w pikselach.
ii. Na oryginalnym obrazie narysuj prostokąt oraz opisz go wymiarami,
np. „40x40 px”.'''

import cv2
import imutils
import os

image = cv2.imread('cobblestone.jpg')
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

os.makedirs("kostki2", exist_ok=True)

for i, c in enumerate(cnts, 1):
    c = c.astype("float") * ratio
    c = c.astype("int")

    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

    M = cv2.moments(c)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0
    
    x, y, w, h = cv2.boundingRect(c)
    label = f"{cX}x{cY} px"
    cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 1)

    tile = image[y:y+h, x:x+w]

    filename = f"kostki2/kostka_{i:02}.png"
    cv2.imwrite(filename, tile)

cv2.imshow("Kostki ponumerowane", image)
cv2.waitKey(0)
cv2.destroyAllWindows()