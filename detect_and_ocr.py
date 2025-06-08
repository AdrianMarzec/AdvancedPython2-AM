import cv2
import os
import pandas as pd
import easyocr
import time
import numpy as np

# Parametry detekcji
MIN_AREA = 500
MAX_AREA = 100000
ASPECT_RATIO_RANGE = (1.5, 10.0)

# Dane z adnotacjami
annotations = pd.read_csv("annotations.csv")
annotations_dict = {row.filename: row.plate_number for _, row in annotations.iterrows()}

reader = easyocr.Reader(['en'], gpu=False)

'''def detect_license_plate(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Wygładzenie
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detekcja Krawędzi
    edged = cv2.Canny(blur, 50, 150)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (17, 3))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    plates = []
    for cnt in contours:
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        if len(approx) == 4:
            rect = cv2.minAreaRect(cnt)
            (x, y), (w, h), angle = rect
            if w == 0 or h == 0:
                continue
            aspect_ratio = max(w,h) / min(w,h)
            area = w * h
            if MIN_AREA < area < MAX_AREA and ASPECT_RATIO_RANGE[0] <= aspect_ratio <= ASPECT_RATIO_RANGE[1]:
                box = cv2.boxPoints(rect)
                box = np.int32(box)
                plates.append(box)
    return plates'''

def detect_and_transform_plate(image):
    dim = (640, 480)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    b_filter = cv2.bilateralFilter(gray, 9, 17, 17)
    edged = cv2.Canny(b_filter, 30, 250)
    cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
    plate_contour = None
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.008 * peri, True)
        x, y, w, h = cv2.boundingRect(c)
        if w > 200 and len(approx) == 4:
            plate_contour = approx
            break

    if plate_contour is None:
        return None

    # Perspektywiczna transformacja tablicy
    points = plate_contour.reshape(4, 2)
    rect = np.zeros((4, 2), dtype="float32")

    s = points.sum(axis=1)
    rect[0] = points[np.argmin(s)]  # top-left
    rect[2] = points[np.argmax(s)]  # bottom-right

    diff = np.diff(points, axis=1)
    rect[1] = points[np.argmin(diff)]  # top-right
    rect[3] = points[np.argmax(diff)]  # bottom-left

    widthA = np.linalg.norm(rect[2] - rect[3])
    widthB = np.linalg.norm(rect[1] - rect[0])
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.linalg.norm(rect[1] - rect[2])
    heightB = np.linalg.norm(rect[0] - rect[3])
    maxHeight = max(int(heightA), int(heightB))

    dst_pts = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]
    ], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst_pts)
    warped = cv2.warpPerspective(resized, M, (maxWidth, maxHeight))

    return warped

def preprocess_plate(roi):
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (gray.shape[1], gray.shape[0]), interpolation=cv2.INTER_CUBIC)
    gray = cv2.bilateralFilter(gray, 9, 75, 75)  # filtr wygładzający
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh


def clean_text(text):
    return ''.join(filter(str.isalnum, text.upper()))

'''def main(image_folder="test"):
    correct = 0
    total = 0
    times = []

    for filename in os.listdir(image_folder):
        if not filename.lower().endswith(".jpg"):
            continue

        image_path = os.path.join(image_folder, filename)
        image = cv2.imread(image_path)

        start_time = time.time()

        plates = detect_license_plate(image)
        ocr_result = ""

        height, width = image.shape[:2]

        for box in plates:
            x, y, w, h = cv2.boundingRect(box)
            
            # Granice obrazu
            x, y = max(0, x), max(0, y)
            x2, y2 = min(x + w, width), min(y + h, height)
            roi = image[y:y2, x:x2]

            if roi.size == 0:
                continue
            
            processed_roi = preprocess_plate(roi)

            debug_image = image.copy()
            for box in plates:
                cv2.drawContours(debug_image, [box], -1, (0, 255, 0), 2)

            cv2.imwrite(f"debug_roi/{filename}", debug_image)

            result = reader.readtext(processed_roi, detail=0)

            if result:
                ocr_result = clean_text(result[0])
                break

        end_time = time.time()
        times.append(end_time - start_time)
        total += 1

        expected = clean_text(annotations_dict.get(filename, ""))
        if ocr_result == expected:
            correct += 1

        print(f"{filename} | OCR: {ocr_result} | GT: {expected} | Match: {ocr_result == expected}")

        if total == 100:
            break

    accuracy = correct / total * 100
    total_time = sum(times)
    print("\n=== PODSUMOWANIE ===")
    print(f"Dokładność OCR: {accuracy:.2f}%")
    print(f"Czas przetwarzania 100 obrazów: {total_time:.2f} sekundy")'''

def detect_license_plate(image, scale=1.0):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blur, 50, 150)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (17, 3))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    plates = []
    # Dopasuj progi do skali
    MIN_AREA_SCALED = MIN_AREA * (scale ** 2)
    MAX_AREA_SCALED = MAX_AREA * (scale ** 2)
    ASPECT_RATIO_MIN, ASPECT_RATIO_MAX = ASPECT_RATIO_RANGE

    for cnt in contours:
        rect = cv2.minAreaRect(cnt)
        (x, y), (w, h), angle = rect
        if w == 0 or h == 0:
            continue
        aspect_ratio = max(w, h) / min(w, h)
        area = w * h
        if MIN_AREA_SCALED < area < MAX_AREA_SCALED and ASPECT_RATIO_MIN <= aspect_ratio <= ASPECT_RATIO_MAX:
            box = cv2.boxPoints(rect)
            box = np.int32(box)
            plates.append(box)
    return plates

def resize_image(image, max_width=800, max_height=600):
    height, width = image.shape[:2]
    if width > max_width or height > max_height:
        scale = min(max_width / width, max_height / height)
        new_size = (int(width * scale), int(height * scale))
        return cv2.resize(image, new_size, interpolation=cv2.INTER_AREA), scale
    else:
        return image, 1.0

def main(image_folder="test"):
    correct = 0
    total = 0
    times = []

    for filename in os.listdir(image_folder):
        if not filename.lower().endswith(".jpg"):
            continue

        image_path = os.path.join(image_folder, filename)
        image = cv2.imread(image_path)
        image, scale = resize_image(image, max_width=800, max_height=600)

        start_time = time.time()

        plates = detect_license_plate(image, scale)
        ocr_result = ""

        height, width = image.shape[:2]

        for box in plates:
            x, y, w, h = cv2.boundingRect(box)
            x, y = max(0, x), max(0, y)
            x2, y2 = min(x + w, width), min(y + h, height)
            roi = image[y:y2, x:x2]

            if roi.size == 0:
                continue

            processed_roi = preprocess_plate(roi)

            debug_image = image.copy()
            for box in plates:
                cv2.drawContours(debug_image, [box], -1, (0, 255, 0), 2)

            os.makedirs("debug_roi", exist_ok=True)
            cv2.imwrite(f"debug_roi/{filename}", debug_image)

            result = reader.readtext(processed_roi, detail=0)

            if result:
                ocr_result = clean_text(result[0])
                break

        end_time = time.time()
        times.append(end_time - start_time)
        total += 1

        expected = clean_text(annotations_dict.get(filename, ""))
        if ocr_result == expected:
            correct += 1

        print(f"{filename} | OCR: {ocr_result} | GT: {expected} | Match: {ocr_result == expected}")

        if total == 100:
            break

    accuracy = correct / total * 100
    total_time = sum(times)
    print("\n=== PODSUMOWANIE ===")
    print(f"Dokładność OCR: {accuracy:.2f}%")
    print(f"Czas przetwarzania 100 obrazów: {total_time:.2f} sekundy")

if __name__ == "__main__":
    main()