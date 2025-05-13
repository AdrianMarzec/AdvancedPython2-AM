'''Przetestuj kilka metod z cv2.matchTemplate i porównaj wyniki.
a. Użyj wszystkich sześciu metod:
cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED.
b. Narysuj wykryty prostokąt.
c. Wypisz wartości dopasowania.
d. Która metoda działa najlepiej w Twoim przypadku?'''

import cv2

methods = [
    ("TM_CCOEFF", cv2.TM_CCOEFF),
    ("TM_CCOEFF_NORMED", cv2.TM_CCOEFF_NORMED),
    ("TM_CCORR", cv2.TM_CCORR),
    ("TM_CCORR_NORMED", cv2.TM_CCORR_NORMED),
    ("TM_SQDIFF", cv2.TM_SQDIFF),
    ("TM_SQDIFF_NORMED", cv2.TM_SQDIFF_NORMED)
]


image_orig = cv2.imread('fanta.jpg')
template = cv2.imread('logo.png')


templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

for name, method in methods:
    image = image_orig.copy()
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    result = cv2.matchTemplate(imageGray, templateGray, method)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)


    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        topLeft = minLoc
        bestVal = minVal
    else:
        topLeft = maxLoc
        bestVal = maxVal


    bottomRight = (topLeft[0] + template.shape[1], topLeft[1] + template.shape[0])

    cv2.rectangle(image, topLeft, bottomRight, (255, 0, 0), 3)


    cv2.imshow(f"Metoda: {name}", image)
    print(f"{name}: Dopasowanie = {bestVal:.4f}")

cv2.waitKey(0)
cv2.destroyAllWindows()



