import xml.etree.ElementTree as ET
import csv
import os
import shutil
import random

def parse_annotations(xml_path, output_csv="annotations.csv", output_yolo_dir="yolo_labels", image_dir="images"):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    os.makedirs(output_yolo_dir, exist_ok=True)

    with open(output_csv, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["filename", "xmin", "ymin", "xmax", "ymax", "plate_number"])

        for image in root.findall('image'):
            filename = image.attrib['name']
            width = int(image.attrib['width'])
            height = int(image.attrib['height'])

            for box in image.findall('box'):
                label = box.attrib['label']
                if label != "plate":
                    continue

                xtl = float(box.attrib['xtl'])
                ytl = float(box.attrib['ytl'])
                xbr = float(box.attrib['xbr'])
                ybr = float(box.attrib['ybr'])

                plate_number = None
                for attr in box.findall('attribute'):
                    if attr.attrib['name'] == "plate number":
                        plate_number = attr.text.strip()

                writer.writerow([filename, xtl, ytl, xbr, ybr, plate_number])

                # Konwersja do YOLO: [class_id, x_center, y_center, width, height] (normalizowane)
                class_id = 0
                x_center = ((xtl + xbr) / 2) / width
                y_center = ((ytl + ybr) / 2) / height
                bbox_width = (xbr - xtl) / width
                bbox_height = (ybr - ytl) / height

                yolo_line = f"{class_id} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}\n"

                base_filename = os.path.splitext(filename)[0]
                with open(os.path.join(output_yolo_dir, f"{base_filename}.txt"), "w") as yolo_file:
                    yolo_file.write(yolo_line)

    print(f"Zapisano dane do: {output_csv} i {output_yolo_dir}")



def split_yolo_dataset(image_dir='photos', label_dir='yolo_labels', output_dir='dataset', train_ratio=0.7):
    # Lista plików JPG
    image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(".jpg")]
    random.seed(42)
    random.shuffle(image_files)

    train_count = int(len(image_files) * train_ratio)
    train_files = image_files[:train_count]
    val_files = image_files[train_count:]

    for split, files in [('train', train_files), ('val', val_files)]:
        img_out = os.path.join(output_dir, 'images', split)
        lbl_out = os.path.join(output_dir, 'labels', split)
        os.makedirs(img_out, exist_ok=True)
        os.makedirs(lbl_out, exist_ok=True)

        for file in files:
            base = os.path.splitext(file)[0]
            # Kopiuj obraz
            shutil.copy(os.path.join(image_dir, file), os.path.join(img_out, file))
            # Kopiuj etykietę YOLO
            label_path = os.path.join(label_dir, f"{base}.txt")
            if os.path.exists(label_path):
                shutil.copy(label_path, os.path.join(lbl_out, f"{base}.txt"))

    print("Podział na train/val zakończony.")


if __name__ == "__main__":
    parse_annotations("annotations.xml")
    split_yolo_dataset()