# my_utils/truck_detector.py
import pathlib

import torch
import cv2

# Eğitilmiş kamyon modelini yükle
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
truck_model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/truck.pt')
truck_model.conf = 0.5

def is_truck_present(image_path_or_frame):
    if isinstance(image_path_or_frame, str):
        img = cv2.imread(image_path_or_frame)
    else:
        img = image_path_or_frame

    results = truck_model(img)
    labels = results.names
    detections = results.pred[0]

    for det in detections:
        cls_id = int(det[5])
        label = labels[cls_id].lower()
        if 'truck' in label:
            return True
    return False
