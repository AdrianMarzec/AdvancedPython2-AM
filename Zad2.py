import cv2

image = cv2.imread('pies.jpg')
(h,w) = image.shape[:2]
cv2.imshow("Original", image)

(b,g,r) = image[h,w]
print(f"Pixel przed zmianą: - Red {r}, Green {g}, Blue {b}")

image[h,w] = (0,0,255)
(b,g,r) = image[h,w]
print(f"Pixel po zmianie - Red {r}, Green {g}, Blue {b}")
cv2.imshow("Changed", image)