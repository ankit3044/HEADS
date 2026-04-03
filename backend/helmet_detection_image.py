import cv2
import math
import cvzone
from ultralytics import YOLO

# Load YOLO model once
model = YOLO("Weights/best.pt")

class_labels = ['With Helmet', 'Without Helmet']

def detect_helmet_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return "Error"

    results = model(img)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])
            print("Detected:", class_labels[cls], "Confidence:", conf)

            if conf > 0.2:
                return class_labels[cls]

    return "No Detection"
