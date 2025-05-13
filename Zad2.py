'''Zobacz, jak bardzo dopasowywanie szablonu jest wrażliwe na obrót
a. Obróć obraz Fanty o 30° i 45° ( imutils.rotate() ).
b. Powtórz detekcję logo.
c. Zinterpretuj wynik: czy detekcja zadziałała? Jaki jest maxVal ?'''


import cv2
import imutils

tupelek = (0,30,45)
for x in tupelek:
    image = cv2.imread('fanta.jpg')
    image = imutils.rotate(image, x)
    template = cv2.imread('logo.png')
    cv2.imshow("Image", image)
    cv2.imshow("Template", template)
    # convert both the image and template to grayscale
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    # perform template matching
    result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
    # determine the starting and ending (x, y)-coordinates of the bounding box
    (startX, startY) = maxLoc
    endX = startX + template.shape[1]
    endY = startY + template.shape[0]
    # draw the bounding box on the image
    cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 3)
    # show the output image
    cv2.imshow(f"Output{x}", image)
    print(maxVal)
cv2.waitKey(0)

