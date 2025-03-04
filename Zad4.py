import cv2

image = cv2.imread('pies.jpg')
(h,w) = image.shape[:2]

x = input("Podaj x ")
y = input("Podaj y ")

if x<=w and x>=0 and y<=h and y>=0:
    pass
else:
    print("Współrzędne wychodzą poza wymiar zdjęcia")