import cv2

image = cv2.imread('pies.jpg')
(h,w) = image.shape[:2]
cv2.imshow("Original", image)

(cX, cY) = (w//2,h//2)
(b,g,r) = image[cY,cX]
print(f"Pixel w środku ({cX},{cY}): - Red {r}, Green {g}, Blue {b}")
