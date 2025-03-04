import cv2

image = cv2.imread('pies.jpg')
(h,w) = image.shape[:2]
cv2.imshow("Original", image)

(b, g, r) = image[0,0]
print(f"Pixel at (0,0) - Red {r}, Green {g}, Blue {b}")