import torch
import cv2
import os
import pathlib

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
model = torch.hub.load('yolov5', 'custom', path='weights/best.pt', source='local')
model.conf = 0.5

def detect_plate(image_path, output_path='plate.jpg'):

    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Görsel bulunamadı: {image_path}")

    results = model(img)

    detections = results.xyxy[0]

    if len(detections) == 0:
        print("Plaka tespit edilemedi.")
        return None

    x1, y1, x2, y2, conf, cls = detections[0].tolist()
    x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
    plate_img = img[y1:y2, x1:x2]

    cv2.imwrite(output_path, plate_img)
    print(f"Plaka kaydedildi: {output_path}")

    return output_path