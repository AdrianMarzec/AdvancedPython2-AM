import csv
import cv2
from ultralytics import YOLO
import easyocr
import time
import os
import numpy as np
import re



# Funkcja IoU (dodana)
def iou(boxA, boxB):
    # box: [xmin, ymin, xmax, ymax]
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    interArea = max(0, xB - xA) * max(0, yB - yA)
    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])
    iou_val = interArea / float(boxAArea + boxBArea - interArea) if (boxAArea + boxBArea - interArea) > 0 else 0
    return iou_val

def load_ground_truth_boxes(csv_path):
    gt_boxes = {}
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            filename = row['filename']
            xmin = float(row['xmin'])
            ymin = float(row['ymin'])
            xmax = float(row['xmax'])
            ymax = float(row['ymax'])
            if filename not in gt_boxes:
                gt_boxes[filename] = []
            gt_boxes[filename].append([xmin, ymin, xmax, ymax])
    return gt_boxes

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

# Załadowanie modelu YOLO (najlepszy wytrenowany)
model = YOLO('runs/detect/train/weights/best.pt')

# Inicjalizuj OCR
reader = easyocr.Reader(['en'])

def detect_and_ocr(image_path):
    img = cv2.imread(image_path)
    results = model(img)

    texts = []
    plate_idx = 0
    detected_boxes = []

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            detected_boxes.append([x1, y1, x2, y2])

            plate_img = img[y1:y2, x1:x2]

            debug_path = os.path.join("debugOCR", f"{os.path.basename(image_path).split('.')[0]}_plate{plate_idx}START.jpg")
            cv2.imwrite(debug_path, plate_img)

            preprocessed = preprocess_plate(plate_img)

            height, width = preprocessed.shape[:2]
            left_margin = int(width * 0.1)
            bottom_margin = int(height*0.07)
            cropped = preprocessed[bottom_margin:, left_margin:]

            debug_path = os.path.join("debugOCR", f"{os.path.basename(image_path).split('.')[0]}_plate{plate_idx}.jpg")
            cv2.imwrite(debug_path, cropped)
            plate_idx += 1
            
            # Po wycięciu i wstępnym przetworzeniu tablicy
            height, width = cropped.shape[:2]

            # Zwiększenie rozmiaru 2x
            #plate_resized = cv2.resize(cropped, (width*2, height*2), interpolation=cv2.INTER_CUBIC)


            ocr_result = reader.readtext(cropped, allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

            if ocr_result:
                text = ocr_result[0][1]
                text = clean_text(text)
                texts.append(text)

    return texts, detected_boxes


def clean_text(text):
    # Duże Litery
    text = text.upper()
    # Usuń spacje i znaki niealfanumeryczne
    text = re.sub(r'[^A-Z0-9]', '', text)
    return text


def preprocess_plate(plate_img):

    # Konwersja do szarości
    gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)

    
    # Rozciąganie kontrastu (CLAHE)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)

    
    blurred = cv2.bilateralFilter(enhanced,9,9,1.5)

    # Usuwanie szumu (morfologia)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    clean = cv2.morphologyEx(blurred, cv2.MORPH_CLOSE, kernel)


    _, binary = cv2.threshold(clean, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    #median = cv2.medianBlur(binary, 3)
    bilateral = cv2.bilateralFilter(binary, 15, 100, 100)
    inverted = cv2.bitwise_not(bilateral)
    
    return inverted


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

ground_truth_boxes = load_ground_truth_boxes(csv_path)

ious_per_image = []


start = time.time()

for img_file in images:
    img_path = os.path.join(image_folder, img_file)
    texts, detected_boxes = detect_and_ocr(img_path)
    gt_text = ground_truth.get(img_file, "").upper()
    ocr_text_candidates = [clean_text(t) for t in texts]
    ocr_text = ocr_text_candidates[0].upper() if texts else ""
    #ocr_text = clean_text(ocr_text)
    gt_text = clean_text(gt_text)

    # --- LICZENIE IoU ---
    gt_boxes_img = ground_truth_boxes.get(img_file, [])
    for gt_box in gt_boxes_img:
        max_iou = 0
        for det_box in detected_boxes:
            current_iou = iou(gt_box, det_box)
            if current_iou > max_iou:
                max_iou = current_iou
        ious_per_image.append(max_iou)
    # --- --- --- --- ---
    
    if ocr_text == gt_text:
        correct_count += 1
    elif gt_text == ocr_text[1:] or gt_text==ocr_text[:-1] or gt_text==ocr_text[1:-1]:
        correct_count += 1
        ocr_text=gt_text
    else:
        for x in texts:
            print(x)

        
    print(f"Image: {img_file}, OCR Text: {ocr_text}, Ground Truth: {gt_text}")

average_iou = sum(ious_per_image) / len(ious_per_image) if ious_per_image else 0
print(f"\nŚrednia wartość IoU dla detekcji: {average_iou:.3f}")

end = time.time()
processing_time_sec = end - start

accuracy_percent = (correct_count / total) * 100
final_grade = calculate_final_grade(accuracy_percent, processing_time_sec)

print(f"\nDokładność OCR: {accuracy_percent:.2f}%")
print(f"Czas przetwarzania {total} zdjęć: {processing_time_sec:.2f} sekund")
print(f"Ostateczna ocena: {final_grade}")