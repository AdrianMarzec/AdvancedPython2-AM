'''Zastosowanie odbicia na wybranym obszarze
a. Wczytaj obraz i wytnij z niego fragment (np. środek obrazu lub prawą połowę).
b. Odbij tylko wycięty fragment i wklej go z powrotem do obrazu.'''

import cv2

image = cv2.imread("wolf.jpg")
cv2.imshow("Original", image)
(h,w) = image.shape[:2]
cX = w//2
cY = h//2

middle = image[cY-30:cY+30,cX-30:cX+30]

flipped = cv2.flip(middle, 0)

image[cY-30:cY+30,cX-30:cX+30] = flipped

cv2.imshow("Middle", flipped)
cv2.imshow("Original", image)
cv2.waitKey(0)
