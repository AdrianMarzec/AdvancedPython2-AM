import csv
import cv2
from ultralytics import YOLO
import easyocr
import time
import os
import numpy as np
import re

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

    for result in results:
        for box in result.boxes:
            
            x1, y1, x2, y2 = map(int, box.xyxy[0])


            plate_img = img[y1:y2, x1:x2]

            debug_path = os.path.join("debugOCR", f"{os.path.basename(image_path).split('.')[0]}_plate{plate_idx}START.jpg")
            cv2.imwrite(debug_path, plate_img)

            preprocessed = preprocess_plate(plate_img)

            '''highlighted_plate = highlight_main_characters(plate_img)
            preprocessed = preprocess_plate(highlighted_plate)
            
            bright_mask = cv2.inRange(preprocessed, 200, 255)
            isolated = cv2.bitwise_and(preprocessed, preprocessed, mask=bright_mask)
            isolated = cv2.bitwise_not(isolated)'''

            height, width = preprocessed.shape[:2]
            left_margin = int(width * 0.1)
            bottom_margin = int(height*0.05)
            cropped = preprocessed[bottom_margin:, left_margin:]

            debug_path = os.path.join("debugOCR", f"{os.path.basename(image_path).split('.')[0]}_plate{plate_idx}.jpg")
            cv2.imwrite(debug_path, cropped)
            plate_idx += 1
            
            ocr_result = reader.readtext(cropped, allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

            if ocr_result:
                text = ocr_result[0][1]
                text = clean_text(text)
                texts.append(text)
    return texts

def clean_text(text):
    # Duże Litery
    text = text.upper()
    # Usuń spacje i znaki niealfanumeryczne
    text = re.sub(r'[^A-Z0-9]', '', text)
    return text

'''def highlight_main_characters(plate_img):
    gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
    
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    if np.mean(gray) > 127:
        binary = 255 - binary

    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        return plate_img  # nic nie znaleziono, zwróć oryginał
    
        # Lista bounding boxów znaków o sensownym rozmiarze
    boxes = []
    h_img, w_img = plate_img.shape[:2]
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if h > 0.3 * h_img and w > 0.02 * w_img:  # pomijaj małe kropki/szumy
            boxes.append((x, y, x + w, y + h))

    if not boxes:
        return plate_img  # nie znaleziono nic sensownego

    # Oblicz zbiorczy bounding box
    x1 = min(b[0] for b in boxes)
    y1 = min(b[1] for b in boxes)
    x2 = max(b[2] for b in boxes)
    y2 = max(b[3] for b in boxes)

    # Dodaj mały margines
    margin = 5
    x1 = max(x1 - margin, 0)
    y1 = max(y1 - margin, 0)
    x2 = min(x2 + margin, w_img)
    y2 = min(y2 + margin, h_img)

    cropped = plate_img[y1:y2, x1:x2]
    # Konwersja do szarości
    gray_crop = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    # Binaryzacja Otsu
    _, binary_crop = cv2.threshold(gray_crop, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    

    # Dylacja (pogrubienie)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    thickened = cv2.dilate(binary_crop, kernel, iterations=1)

    # Konwersja do BGR, bo dalej prawdopodobnie potrzebujesz kolorowy obraz
    thickened_bgr = cv2.cvtColor(thickened, cv2.COLOR_GRAY2BGR)

    return thickened_bgr'''


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
    '''binary = cv2.adaptiveThreshold(
    blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 11, 2)'''
    median = cv2.medianBlur(binary, 3)
    inverted = cv2.bitwise_not(median)

    # Wyostrzanie
    '''sharp_kernel = np.array([[0, -1, 0],
                             [-1, 5, -1],
                             [0, -1, 0]])
    sharp = cv2.filter2D(gray, -1, sharp_kernel)'''
    
    
    
    # Dodatkowe wygładzanie do redukcji szumu (np. filtr medianowy)
    #denoised = cv2.medianBlur(blurred, 3)  # kernel 3x3 - można eksperymentować

    
    
    # Binaryzacja (Otsu)
    #_, thresh = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    
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

start = time.time()

for img_file in images:
    img_path = os.path.join(image_folder, img_file)
    texts = detect_and_ocr(img_path)
    gt_text = ground_truth.get(img_file, "").upper()
    ocr_text = texts[0].upper() if texts else ""
    ocr_text = clean_text(ocr_text)
    gt_text = clean_text(gt_text)
    
    if ocr_text == gt_text:
        correct_count += 1
    elif gt_text == ocr_text[1:] or gt_text==ocr_text[:-1] or gt_text==ocr_text[1:-1]:
        correct_count += 1
        ocr_text=gt_text
        
    
    print(f"Image: {img_file}, OCR Text: {ocr_text}, Ground Truth: {gt_text}")

end = time.time()
processing_time_sec = end - start

accuracy_percent = (correct_count / total) * 100
final_grade = calculate_final_grade(accuracy_percent, processing_time_sec)

print(f"\nDokładność OCR: {accuracy_percent:.2f}%")
print(f"Czas przetwarzania {total} zdjęć: {processing_time_sec:.2f} sekund")
print(f"Ostateczna ocena: {final_grade}")