from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from helmet_detection_image import detect_helmet_image
from helmet_detection_video import detect_helmet_video

app = Flask(__name__)
CORS(app)   # 🔥 IMPORTANT (fixes your issue)

UPLOAD_FOLDER = "uploads"

# Create uploads folder if not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# ✅ IMAGE DETECTION (already working)
@app.route("/detect", methods=["POST"])
def detect():
    file = request.files["file"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    result = detect_helmet_image(path)

    challan = 1000 if result == "Without Helmet" else 0

    return jsonify({
        "result": result,
        "challan": challan
    })


# ✅ VIDEO DETECTION (NEW)
@app.route("/detect-video", methods=["POST"])
def detect_video():
    file = request.files["file"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    data = detect_helmet_video(path)

    # data can be string OR dict (handle both safely)
    if isinstance(data, dict):
        result = data.get("result", "No Detection")
        violations = data.get("violations", 0)
    else:
        result = data
        violations = 0

    challan = 1000 if result == "Without Helmet" else 0

    return jsonify({
        "result": result,
        "violations": violations,
        "challan": challan
    })


if __name__ == "__main__":
    app.run(debug=True)