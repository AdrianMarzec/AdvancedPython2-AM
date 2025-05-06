import cv2
import imutils

thresh_value = 140

for width in (200, 300, 400):
    image = cv2.imread('cobblestone.jpg')
    resized = imutils.resize(image, width=width)
    ratio = image.shape[0] / float(resized.shape[0])

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, thresh_value, 255, cv2.THRESH_BINARY)[1]

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    output = image.copy()

    for c in cnts:
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        cv2.drawContours(output, [c], -1, (0, 255, 0), 2)

    # Wyświetlanie
    cv2.imshow(f"Contours @ width={width}", output)
    cv2.imshow(f"Threshold @ width={width}", thresh)
    cv2.waitKey(0)

cv2.destroyAllWindows()
