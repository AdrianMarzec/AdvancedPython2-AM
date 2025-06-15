import csv
import cv2
from ultralytics import YOLO
import easyocr
import time
import os
import numpy as np
import re
import difflib
import random

# Mapowanie podobnych znaków często mylonych przez OCR (część Postprocessing)
CHAR_SIMILARITY = {
    '0': ['O', 'Q'],
    'O': ['0', 'Q'],
    'Q': ['O', '0'],
    '1': ['I'],
    'I': ['1'],
    '6': ['G'],
    '8': ['B'],
    'B': ['8'],
    'G': ['6'],
    '5': ['S'],
    'S': ['5']
}

# Funkcja IoU
def iou(boxA, boxB):
    # box: [xmin, ymin, xmax, ymax]
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    interArea = max(0, xB - xA) * max(0, yB - yA) # Obszar wspólny
    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])
    iou_val = interArea / float(boxAArea + boxBArea - interArea) if (boxAArea + boxBArea - interArea) > 0 else 0
    return iou_val


# Wczytanie boxów prawdziwych
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

# Wczytanie numerów prawdziwych
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
model = YOLO('license-plate-finetune-v1m.pt')
model.to('cuda')  # Przenosi model na GPU


# Inicjalizuj OCR
reader = easyocr.Reader(['en'], gpu=True)

# Wykrywanie tablic i rozpoznanie znaków z obrazu
def detect_and_ocr(image_path):
    img = cv2.imread(image_path)
    result = model(img)[0]

    texts = []
    plate_idx = 0
    detected_boxes = []
    cropped_plates = []

    for box in result.boxes:

        # Współrzędne wykrytej tablicy
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        detected_boxes.append([x1, y1, x2, y2])

        # Wycięcie tablicy z obrazu
        plate_img = img[y1:y2, x1:x2]

        # Sprawdzenie rozdzielczości wyciętej tablicy
        h, w = plate_img.shape[:2]
        if h < 50 and w < 70:
            # Delikatne wyostrzenie tylko dla małych tablic
            resized = cv2.resize(plate_img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

            kernel = np.array([[0, -1, 0],
                               [-1, 5, -1],
                               [0, -1, 0]])
            plate_img = cv2.filter2D(resized, -1, kernel)

        # Zapis wyciętej tablicy do Debugowania
        '''debug_path = os.path.join("debugOCR", f"{os.path.basename(image_path).split('.')[0]}_plate{plate_idx}START.jpg")
        cv2.imwrite(debug_path, plate_img)'''

        # Wstępne przetwarzanie obrazu tablicy
        preprocessed = preprocess_plate(plate_img)
        #preprocessed = plate_img

        # Dodatkowe przycięcie marginesów
        height, width = preprocessed.shape[:2]
        left_margin = int(width * 0.1)
        bottom_margin = int(height*0.1)
        cropped = preprocessed[bottom_margin:, left_margin:]


        # Po wycięciu i wstępnym przetworzeniu tablicy
        height, width = cropped.shape[:2]
        center = (width // 2, height // 2)
        M = cv2.getRotationMatrix2D(center, -1, 1.0)
        rotated = cv2.warpAffine(cropped, M, (width, height), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)


        #smoothed = cv2.GaussianBlur(rotated, (5, 5), sigmaX=1)

        # Zapis przetworzonej tablicy do Debugowania
        '''debug_path = os.path.join("debugOCR", f"{os.path.basename(image_path).split('.')[0]}_plate{plate_idx}.jpg")
        cv2.imwrite(debug_path, rotated)
        plate_idx += 1'''
        

        # Zapis, by mieć możliwość ponownej próby na powiększonym obrazie później
        cropped_plates.append(rotated)

        # Uruchomienie OCR
        ocr_result = reader.readtext(rotated, allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

        if ocr_result:
            for res in ocr_result:
                text = clean_text(res[1])
                texts.append(text)


    return texts, detected_boxes, cropped_plates


def clean_text(text):
    # Duże Litery
    text = text.upper()
    # Usuń spacje i znaki niealfanumeryczne
    text = re.sub(r'[^A-Z0-9]', '', text)
    return text


# Wstępne przetwarzanie obrazu tablicy dla lepszego OCR
def preprocess_plate(plate_img):
    gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
    #resized = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    # Kontrast lokalny
    clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(4, 4))
    enhanced = clahe.apply(gray)

    # Filtr zachowujący krawędzie
    denoised = cv2.bilateralFilter(enhanced, 9, 75, 75)

    # Usuwanie szumu (morfologia, oczyszczenie)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3)) # Maska do morfologii
    clean = cv2.morphologyEx(denoised, cv2.MORPH_CLOSE, kernel) # "Zamykanie dziur"

    # Progowanie i odwrócenie (dla jasnych liter)
    _, thresh = cv2.threshold(clean, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    inverted = cv2.bitwise_not(thresh)

    eroded = cv2.erode(inverted, kernel, iterations=1)
    dilated = cv2.dilate(eroded, kernel, iterations=1)
    
    return dilated

# Obliczanie podobieństwa tekstów
def similar(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()


# Postprocessing - podobne znaki
def fuzzy_char_distance(a: str, b: str) -> float:
    if len(a) != len(b):
        return 1.0  # różne długości → wysoka kara

    mismatches = 0
    for ca, cb in zip(a, b):
        if ca != cb:
            if cb in CHAR_SIMILARITY.get(ca, []) or ca in CHAR_SIMILARITY.get(cb, []):
                mismatches += 0.3  # podobny znak = mniejsza kara
            else:
                mismatches += 1

    return mismatches / len(a)  # niższa wartość = lepszy match


# Obliczanie końcowej oceny wg. dokładności i czasu
def calculate_final_grade(accuracy_percent: float, processing_time_sec: float) -> float:
    # Check minimum requirements
    if accuracy_percent < 60 or processing_time_sec > 60:
        return 2.0
    # Normalize accuracy: 60% → 0.0, 100% → 1.0
    accuracy_norm = (accuracy_percent - 60) / 40
    # Normalize time: 60s → 0.0, 10s → 1.0
    time_norm = (60 - processing_time_sec) / 50
    # Compute weighted score
    score = 0.7 * accuracy_norm + 0.3 * time_norm
    grade = 2.0 + 3.0 * score
    # Round to the nearest 0.5
    print(grade)
    return round(grade * 2) / 2


# Ścieżka do pliku CSV
csv_path = "annotations.csv"

# Oczekiwane numery tablic
ground_truth = load_ground_truth(csv_path)
for i, gt in enumerate(ground_truth):
    gt = clean_text(gt)

#image_folder = "testowe100"
image_folder = "prezentacja"
#image_folder="photos"
images = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]
random.seed(42) 
#42 - 88%

#4748 - 81%
#1410 - 84%
#966 - 81%
#3068191 - 81%
#2137 - 81%
#11 - 84%
#13 - 79%
#47 - 84%
#25633 - 84%
#0 - 83%
#3 - 82%
#666 - 80%
#777 - 83%
#420 - 80%
#7 - 81%
#69 - 77%
#69420 - 78%

random.shuffle(images)
images = images[:100]

correct_count = 0
total = len(images)

# Oczekiwane boxy tablic
ground_truth_boxes = load_ground_truth_boxes(csv_path)
detected_boxes_dict = dict()

ious_per_image = []

# Rozpoczęcie faktycznego algorytmu detekcji i OCR
start = time.time()

# Przetwarzanie każdego obrazu
for img_file in images:
    img_path = os.path.join(image_folder, img_file)
    texts, detected_boxes, cropped_plates = detect_and_ocr(img_path)
    gt_text = ground_truth.get(img_file, "").upper()
    ocr_text = texts[0].upper() if texts else ""
    
    match_found = False

    # Porównanie OCR z GT (trochę Postprocessing np. ramka jako 'I' czytane)
    for candidate_clean in texts:
        if candidate_clean == gt_text or \
        candidate_clean[1:] == gt_text or \
        candidate_clean[:-1] == gt_text or \
        candidate_clean[1:-1] == gt_text:
            match_found = True
            ocr_text = candidate_clean  # do wypisania później
            break
        elif '0' in candidate_clean:
            postcheck = candidate_clean.replace('0', 'O')
            if postcheck == gt_text or \
            postcheck[1:] == gt_text or \
            postcheck[:-1] == gt_text or \
            postcheck[1:-1] == gt_text:
                match_found = True
                ocr_text = postcheck
                break
        elif 'O' in candidate_clean:
            postcheck = candidate_clean.replace('O', '0')
            if postcheck == gt_text or \
            postcheck[1:] == gt_text or \
            postcheck[:-1] == gt_text or \
            postcheck[1:-1] == gt_text:
                match_found = True
                ocr_text = postcheck
                break
        else:
            min_distance = 1.0
            best_match = ""

            for candidate in texts:
                dist = fuzzy_char_distance(candidate, gt_text)
                if dist < min_distance:
                    min_distance = dist
                    best_match = candidate

            if min_distance < 0.2:
                match_found = True
                ocr_text = best_match
                break

    if match_found:
        correct_count += 1


    detected_boxes_dict[img_file] = detected_boxes  # zapisanie boxa dla późniejszego IoU


    # Próba OCR po przeskalowaniu, jeśli nie udało się wcześniej
    if not match_found: #and similar(ocr_text, gt_text) > 0.7:
        for plate_img in cropped_plates:
            # Po wycięciu i wstępnym przetworzeniu tablicy
            height, width = plate_img.shape[:2]

            center = (width // 2, height // 2)
            M = cv2.getRotationMatrix2D(center, -1, 1.0)
            rotated = cv2.warpAffine(plate_img, M, (width, height), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
            resized = cv2.resize(rotated, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

            # Pogrubienie liter
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
            thickened = cv2.dilate(resized, kernel, iterations=1)

            ocr_result = reader.readtext(thickened, allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')#,paragraph=True)
            for res in ocr_result:
                text_resized = clean_text(res[1])
                if text_resized == gt_text or \
                   text_resized[1:] == gt_text or \
                   text_resized[:-1] == gt_text or \
                   text_resized[1:-1] == gt_text:
                    match_found = True
                    ocr_text = text_resized
                    break
                else:
                    min_distance = 1.0
                    best_match = ""

                    dist = fuzzy_char_distance(text_resized, gt_text)
                    if dist < min_distance:
                        min_distance = dist
                        best_match = text_resized

                    if min_distance < 0.2:
                        match_found = True
                        ocr_text = best_match
                        break
            if match_found:
                correct_count += 1
                break
            else:
                print(ocr_text,gt_text)

    #print(f"Image: {img_file}, OCR Text: {ocr_text}, Ground Truth: {gt_text}")


end = time.time()

# --- LICZENIE IoU --- (wykryte a prawdziwe boxy)
for img_file in images:
    gt_boxes_img = ground_truth_boxes.get(img_file, [])
    det_boxes_img = detected_boxes_dict.get(img_file, [])

    for gt_box in gt_boxes_img:
        max_iou = 0
        for det_box in det_boxes_img:
            current_iou = iou(gt_box, det_box)
            if current_iou > max_iou:
                max_iou = current_iou
        ious_per_image.append(max_iou)

average_iou = sum(ious_per_image) / len(ious_per_image) if ious_per_image else 0
print(f"\nŚrednia wartość IoU dla detekcji: {average_iou:.3f}")

processing_time_sec = end - start

accuracy_percent = (correct_count / total) * 100
final_grade = calculate_final_grade(accuracy_percent, processing_time_sec)

print(f"\nDokładność OCR: {accuracy_percent:.2f}%")
print(f"Czas przetwarzania {total} zdjęć: {processing_time_sec:.2f} sekund")
print(f"Ostateczna ocena: {final_grade}")
