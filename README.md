
# Gesture Recognition System 🎯✋🤖

![Banner](https://raw.githubusercontent.com/harika1807/CodeClauseInternship_GestureRecognitionSystem/main/banner.png)
![License](https://img.shields.io/github/license/harika1807/CodeClauseInternship_GestureRecognitionSystem)
![Last Commit](https://img.shields.io/github/last-commit/harika1807/CodeClauseInternship_GestureRecognitionSystem)

## 🔍 Project Overview
A real-time hand gesture recognition system that detects and classifies hand gestures using deep learning and computer vision techniques.

## 🎯 Aim
Develop a system that recognizes hand gestures from a video stream or camera feed to enable interactions with digital environments.

## 🛠️ Technologies Used
- Python 🐍
- OpenCV 🎥
- TensorFlow/Keras 🤖
- CNN (Convolutional Neural Networks) 🧠

## 📂 Dataset
This project uses the [HaGRID Dataset](https://github.com/hukenovs/hagrid), a large-scale hand gesture recognition dataset.

## 🚀 Features
- Real-time gesture detection via webcam
- Custom trained CNN model using HaGRID
- Classifies 17 hand gestures

## ✋ Supported Gestures (with emoji & thumbnail placeholders)

| Gesture           | Emoji | Sample |
|-------------------|-------|--------|
| Call              | 📞    | ![call](samples/call.png) |
| Dislike           | 👎    | ![dislike](samples/dislike.png) |
| Fist              | ✊    | ![fist](samples/fist.png) |
| Four              | 4️⃣    | ![four](samples/four.png) |
| Like              | 👍    | ![like](samples/like.png) |
| Mute              | 🤐    | ![mute](samples/mute.png) |
| OK                | 👌    | ![ok](samples/ok.png) |
| One               | ☝️    | ![one](samples/one.png) |
| Palm              | ✋    | ![palm](samples/palm.png) |
| Peace             | ✌️    | ![peace](samples/peace.png) |
| Peace Inverted    | ✌️⬇️  | ![peace_inverted](samples/peace_inverted.png) |
| Rock              | 🤘    | ![rock](samples/rock.png) |
| Stop              | 🛑    | ![stop](samples/stop.png) |
| Stop Inverted     | 🛑⬇️  | ![stop_inverted](samples/stop_inverted.png) |
| Three             | 3️⃣    | ![three](samples/three.png) |
| Three2            | 3️⃣✌️ | ![three2](samples/three2.png) |
| Two Up            | ✌️⬆️  | ![two_up](samples/two_up.png) |
| Two Up Inverted   | ✌️⬇️  | ![two_up_inverted](samples/two_up_inverted.png) |

## 🖥️ Usage
1. Clone the repository.
2. Install the dependencies from `requirements.txt`
3. Run the `collect_images.py` script to collect gesture images (if using custom dataset).
4. Run `train_model.py` to train your model.
5. Execute `recognize_gesture.py` for real-time prediction.

## 📽️ Sample Output
> The `output.avi` shows real-time hand gesture predictions in action.

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## 🙌 Acknowledgments
- [HaGRID Dataset](https://github.com/hukenovs/hagrid)
- CodeClause Internship AI Projects
