'''Sprawdź wrażliwość na zmianę rozmiaru szablonu.
a. Zmniejsz lub powiększ oryginalny obraz Fanty.
b. Wykonaj dopasowanie tym samym szablonem.
c. Zaobserwuj, czy detekcja zadziałała poprawnie.'''

import cv2
import imutils

original_width = 768

widths = (400, 900)

for width in widths:
    image = cv2.imread('fanta.jpg')
    image = imutils.resize(image, width=width)

    scale = width / original_width

    template = cv2.imread('logo.png')
    new_template_width = int(template.shape[1] * scale)
    template = imutils.resize(template, width=new_template_width)

    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

    (startX, startY) = maxLoc
    endX = startX + template.shape[1]
    endY = startY + template.shape[0]

    cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 3)

    cv2.imshow(f"Image {width}px", image)
    print(f"Szerokość obrazu: {width}px, Dopasowanie: {maxVal:.4f}")

cv2.waitKey(0)
cv2.destroyAllWindows()
