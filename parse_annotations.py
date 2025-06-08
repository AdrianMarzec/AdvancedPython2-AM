import xml.etree.ElementTree as ET
import csv
import os

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

                # YOLO conversion: [class_id, x_center, y_center, width, height] (normalized)
                class_id = 0
                x_center = ((xtl + xbr) / 2) / width
                y_center = ((ytl + ybr) / 2) / height
                bbox_width = (xbr - xtl) / width
                bbox_height = (ybr - ytl) / height

                yolo_line = f"{class_id} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}\n"

                base_filename = os.path.splitext(filename)[0]
                with open(os.path.join(output_yolo_dir, f"{base_filename}.txt"), "w") as yolo_file:
                    yolo_file.write(yolo_line)

    print(f"Zapisano dane do: {output_csv} i {output_yolo_dir}/")

# Przykładowe wywołanie
if __name__ == "__main__":
    parse_annotations("annotations.xml")