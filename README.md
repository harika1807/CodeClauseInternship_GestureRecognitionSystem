
# ✋ Gesture Recognition System

![Banner](https://raw.githubusercontent.com/harika1807/CodeClauseInternship_GestureRecognitionSystem/main/banner.png)
![License](https://img.shields.io/github/license/harika1807/CodeClauseInternship_GestureRecognitionSystem)

This project is part of the **CodeClause AI Internship (Golden Level)** and focuses on building a real-time **hand gesture recognition system** using deep learning and computer vision.

---

## 📂 Dataset

We used a subset of the **HaGRID (HAnd Gesture Recognition Image Dataset)**, extracting five gestures:
- ✊ Fist  
- ✋ Palm  
- 👍 Thumbs Up  
- 👎 Thumbs Down  
- ✌️ Victory (Peace)

Dataset organized into:
```
dataset/
├── fist/
├── palm/
├── thumb_up/
├── thumb_down/
└── victory/
```

Each folder contains respective gesture images, and `hagrid_labels.csv` maps image paths to labels.

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/harika1807/CodeClauseInternship_GestureRecognitionSystem
   cd CodeClauseInternship_GestureRecognitionSystem
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 📆 Requirements

```
tensorflow==2.11.0
opencv-python==4.8.0.76
numpy==1.23.5
pandas==1.5.3
matplotlib==3.6.2
scikit-learn==1.2.0
```

---

## 🧠 Model Training

To train the CNN model:
```bash
python gesture_recognition_model.py
```

- Trains a Convolutional Neural Network using the dataset.
- Saves the model as `gesture_recognition_model.h5`.

---

## 📊 Training Results

#### 🔹 Model Accuracy
![Model Accuracy](https://github.com/harika1807/CodeClauseInternship_GestureRecognitionSystem/blob/main/model_accuracy.png)

#### 🔹 Model Loss
![Model Loss](https://github.com/harika1807/CodeClauseInternship_GestureRecognitionSystem/blob/main/model_loss.png)

---

## 📸 Real-Time Gesture Recognition

To launch the real-time gesture detection using webcam:
```bash
python gesture_recognition_live.py
```

- Loads the trained `.h5` model.
- Detects and classifies hand gestures from the live video feed.
- Saves output as `gesture_output.mp4` in the project folder.

---

## 🖥️ Output Video

The real-time classification video will be saved as:
```
gesture_output.mp4
```

You can view it with VLC or any media player.

---

## 📁 Project Structure

```
├── dataset/
│   ├── fist/
│   ├── palm/
│   ├── thumb_up/
│   ├── thumb_down/
│   └── victory/
├── hagrid_labels.csv
├── gesture_recognition_model.py
├── realtime_gesture_recognition.py
├── gesture_output.mp4
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 💡 Notes

- To keep the repo lightweight, the trained model (`.h5`) is not included.
- 📅 [Download Gesture Recognition Model (.h5) from Google Drive](https://drive.google.com/file/d/1DycxuFZ1LB3i9zH0W-tjJJaqrqhLuGMS/view?usp=drive_link)

---

## 👩‍💻 Developed by

**Harika Devi**  
B.Tech CSE, Rise Krishna Sai Gandhi Group of Institutions  
🎯 CodeClause AI Internship (Golden Level)

---

## 📬 Contact

📧 [harikaseelam2004@gmail.com]  
🌐 [LinkedIn](https://www.linkedin.com/in/harika-devi-seelam-242709256/)
