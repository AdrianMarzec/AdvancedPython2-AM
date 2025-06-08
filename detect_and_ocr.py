import cv2
import os
import pandas as pd
import easyocr
import time

# Parametry detekcji
MIN_AREA = 2000
MAX_AREA = 30000
ASPECT_RATIO_RANGE = (2.0, 6.0)

# Ładujemy dane z adnotacjami
annotations = pd.read_csv("annotations.csv")
annotations_dict = {row.filename: row.plate_number for _, row in annotations.iterrows()}

reader = easyocr.Reader(['en'], gpu=False)

def detect_license_plate(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Wygładzenie
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detekcja Krawędzi
    edged = cv2.Canny(blur, 50, 150)

    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    plates = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        area = w * h
        if area < MIN_AREA or area > MAX_AREA:
            continue
        aspect_ratio = w / h
        if ASPECT_RATIO_RANGE[0] <= aspect_ratio <= ASPECT_RATIO_RANGE[1]:
            plates.append((x, y, w, h))
    return plates

def clean_text(text):
    return ''.join(filter(str.isalnum, text.upper()))

def main(image_folder="test"):
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

        for (x, y, w, h) in plates:
            roi = image[y:y+h, x:x+w]
            result = reader.readtext(roi, detail=0)
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