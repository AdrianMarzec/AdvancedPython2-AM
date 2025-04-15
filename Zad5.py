'''Automatyczna maska ROI
a. Na obrazie, na którym znajdują się obiekty (np. elementy produkcyjne),
spróbuj wygenerować maskę pierwszego planu.
b. Z pomocą progowania adaptacyjnego wydziel obiekty i zastosuj
cv2.bitwise_and, aby wyświetlić tylko te regiony z oryginalnego obrazu.'''

import cv2

image = cv2.imread("paczki.jpg")
cv2.imshow("Image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)


thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3)
cv2.imshow(f"Mean Adaptive Thresholding {11}", thresh)

masked = cv2.bitwise_and(image, image, mask=thresh)
cv2.imshow(f"Zamaskowany Mściciel", masked)

cv2.waitKey(0)
