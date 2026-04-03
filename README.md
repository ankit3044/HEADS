# H.E.A.D.S – Helmet Enforcement and Automated Detection System

## 🚀 Overview
H.E.A.D.S (Helmet Enforcement and Automated Detection System) is an AI-powered system designed to detect helmet violations in real-time using computer vision. The system analyzes images and videos of two-wheeler riders and determines whether they are wearing helmets. In case of violations, it can generate a challan (fine) automatically.

---

## 🎯 Features

- ✅ Helmet detection using YOLOv8
- 🎥 Video-based detection with frame analysis
- 🖼 Image-based detection
- ⚡ Real-time processing via Flask API
- 💻 Interactive frontend built with React
- 💰 Automatic challan generation for violations

---

## 🧠 Tech Stack

### Backend
- Python
- Flask
- OpenCV
- Ultralytics YOLOv8

### Frontend
- React (Vite)
- TypeScript
- Tailwind CSS
- shadcn-ui

---

## ⚙️ How It Works

1. User uploads an image or video
2. Backend processes input using YOLOv8 model
3. Helmet / No Helmet is detected
4. For video:
   - Frames are sampled
   - Confidence scores are aggregated
5. Final result is returned to frontend
6. Challan is generated if violation is detected

---

## 📦 Installation & Setup

### 🔹 Clone Repository
```bash
git clone https://github.com/rajsaw2005-crypto/H.E.A.D.S.-ride-ai.git
cd H.E.A.D.S.-ride-ai
