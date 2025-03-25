'''Zastosowanie operacji XOR do wykrywania różnic między obrazami
a. Wczytaj dwa podobne obrazy z drobnymi różnicami.
b. Użyj cv2.bitwise_xor , aby uwidocznić różnice między nimi.'''


import cv2
img = cv2.imread('wolf.jpg')
img2 = cv2.imread('wolf2.jpg')

cv2.imshow("Wolf", img)
cv2.imshow("Wolf2", img2)

bitwiseOr = cv2.bitwise_xor(img, img2)
cv2.imshow("XOR", bitwiseOr)

cv2.imwrite('XORedWolf.jpg', bitwiseOr)


cv2.waitKey(0)

