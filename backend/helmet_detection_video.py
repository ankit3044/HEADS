import cv2
from ultralytics import YOLO

# Load your trained model
model = YOLO("Weights/best.pt")

# Class labels
class_labels = ['With Helmet', 'Without Helmet']


def detect_helmet_video(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return "Error"

    helmet_score = 0
    no_helmet_score = 0
    frame_count = 0

    print("Starting video processing...")

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame_count += 1
        print(f"Processing frame: {frame_count}")

        # 🔥 Process every 8th frame (better balance)
        if frame_count % 8 != 0:
            continue

        results = model(frame, verbose=False)

        for r in results:
            boxes = r.boxes

            for box in boxes:
                conf = float(box.conf[0])
                cls = int(box.cls[0])

                print(f"Detected: {class_labels[cls]} | Confidence: {conf:.2f}")

                # 🔥 IMPROVED FILTER
                if conf > 0.4:
                    if class_labels[cls] == "Without Helmet":
                        no_helmet_score += conf
                    else:
                        helmet_score += conf

    cap.release()

    print("Video processing complete.")
    print(f"Helmet Score: {helmet_score:.2f}")
    print(f"No Helmet Score: {no_helmet_score:.2f}")

    # 🔥 FINAL DECISION (CONFIDENCE BASED)
    if no_helmet_score > helmet_score:
        return "Without Helmet"
    elif helmet_score > 0:
        return "With Helmet"
    else:
        return "No Detection"