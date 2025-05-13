'''Połącz wiedzę z poprzednich zajęć o konturach i template matchingu.
a. Najpierw znajdź obiekty za pomocą konturów ( cv2.findContours ).
b. Dla każdego z wyciętych fragmentów wykonaj template matching –
porównaj z szablonem.
c. Zidentyfikuj, które obiekty są podobne do wzorca.'''

import cv2
import numpy as np

# Wczytaj obraz i szablon
image = cv2.imread('cobblestone.jpg')
template = cv2.imread('brick.png', 0)
template_h, template_w = template.shape

# Przekształcenie obrazu do skali szarości i binaryzacja
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Znajdź kontury
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Próg podobieństwa
threshold = 0.7

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)

    # Wytnij ROI (region of interest)
    roi = gray[y:y+h, x:x+w]

    # Dopasuj rozmiar do szablonu
    roi_resized = cv2.resize(roi, (template_w, template_h))

    # Dopasowanie szablonu (Template Matching)
    result = cv2.matchTemplate(roi_resized, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, _, _ = cv2.minMaxLoc(result)

    # Jeśli podobieństwo przekracza próg – oznacz na obrazie
    if max_val > threshold:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, f'{max_val:.2f}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

# Pokaż wynik
cv2.imshow('Dopasowane obiekty', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
