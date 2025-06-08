import csv
import cv2
from ultralytics import YOLO
import easyocr
import time
import os

# Wczytaj ground truth z CSV
def load_ground_truth(csv_path):
    gt = {}
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            filename = row['filename']
            plate_number = row['plate_number'].upper()
            gt[filename] = plate_number
    return gt

# Załaduj model YOLO (najlepszy wytrenowany)
model = YOLO('runs/detect/train/weights/best.pt')

# Inicjalizuj OCR
reader = easyocr.Reader(['en'])

def detect_and_ocr(image_path):
    img = cv2.imread(image_path)
    results = model(img)

    texts = []
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            plate_img = img[y1:y2, x1:x2]

            ocr_result = reader.readtext(plate_img)
            if ocr_result:
                text = ocr_result[0][1]
                texts.append(text)
    return texts

def calculate_final_grade(accuracy_percent: float, processing_time_sec: float) -> float:
    if accuracy_percent < 60 or processing_time_sec > 60:
        return 2.0
    accuracy_norm = (accuracy_percent - 60) / 40
    time_norm = (60 - processing_time_sec) / 50
    score = 0.7 * accuracy_norm + 0.3 * time_norm
    grade = 2.0 + 3.0 * score
    return round(grade * 2) / 2

# Ścieżka do pliku CSV
csv_path = "annotations.csv"

ground_truth = load_ground_truth(csv_path)

image_folder = "testowe100"
images = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]

correct_count = 0
total = len(images)

start = time.time()

for img_file in images:
    img_path = os.path.join(image_folder, img_file)
    texts = detect_and_ocr(img_path)
    gt_text = ground_truth.get(img_file, "").upper()
    ocr_text = texts[0].upper() if texts else ""
    
    if ocr_text == gt_text:
        correct_count += 1
    
    print(f"Image: {img_file}, OCR Text: {ocr_text}, Ground Truth: {gt_text}")

end = time.time()
processing_time_sec = end - start

accuracy_percent = (correct_count / total) * 100
final_grade = calculate_final_grade(accuracy_percent, processing_time_sec)

print(f"\nDokładność OCR: {accuracy_percent:.2f}%")
print(f"Czas przetwarzania {total} zdjęć: {processing_time_sec:.2f} sekund")
print(f"Ostateczna ocena: {final_grade}")