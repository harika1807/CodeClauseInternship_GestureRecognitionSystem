
<p align="center">
  <img src="https://i.imgur.com/VPeXz8k.png" alt="Gesture Recognition Banner" width="800"/>
</p>

# ✋ Gesture Recognition System

This project uses deep learning and computer vision to recognize hand gestures in real-time from a webcam feed using CNNs.

## 📽️ Demo
> 🎥 [Attach your output.avi here or link a Google Drive demo]

## 📌 Features
- Real-time hand gesture recognition
- Trained on a custom or HaGRID dataset
- Displays predicted gesture on webcam feed
- Saves video with gesture labels

## 🧰 Technologies Used
- Python
- OpenCV
- TensorFlow/Keras
- scikit-learn
- CNN

## 📁 Project Structure
```
Gesture_Recognition_System/
├── dataset/                  # Gesture image folders
├── gesture_model.h5          # Trained model
├── train_model.py            # Training script
├── recognize_gesture.py      # Real-time prediction script
├── collect_images.py         # (Optional) Image collection script
├── output.avi                # Output video
├── requirements.txt
├── README.md
└── .gitignore
```

## 🛠️ How to Run

1. Clone the repository
```bash
git clone https://github.com/your-username/Gesture_Recognition_System.git
cd Gesture_Recognition_System
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Train the model (or use the provided model)
```bash
python train_model.py
```

4. Run real-time gesture recognition
```bash
python recognize_gesture.py
```

## ✋ Supported Gestures
- Fist ✊
- Palm ✋
- Thumbs Up 👍
- Thumbs Down 👎
- Peace ✌️

## 📜 License
This project is licensed under the MIT License.

## 🙌 Acknowledgements
- Dataset: [HaGRID Dataset](https://github.com/hukenovs/hagrid)
- Developed by Harika Devi for CodeClause AI Internship (Golden Level Project)
