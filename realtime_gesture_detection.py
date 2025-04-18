import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Load your trained model
model = load_model("gesture_recognition_model.h5")

# Labels used during training
labels = ['fist', 'palm', 'thumb_down', 'thumb_up', 'victory']

# Start webcam
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object for .mp4
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or use 'X264' for better compression
out = cv2.VideoWriter('gesture_output.mp4', fourcc, 20.0, (640, 480))

print("🎬 Press 'q' to quit and save the video as gesture_output.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Region of interest (ROI)
    roi = frame[100:350, 100:350]
    cv2.rectangle(frame, (100, 100), (350, 350), (0, 255, 0), 2)

    # Preprocess the ROI
    roi_resized = cv2.resize(roi, (224, 224))
    roi_array = img_to_array(roi_resized) / 255.0
    roi_array = np.expand_dims(roi_array, axis=0)

    # Prediction
    prediction = model.predict(roi_array)
    class_index = np.argmax(prediction)
    label = labels[class_index]
    confidence = prediction[0][class_index] * 100

    # Show prediction
    text = f"{label} ({confidence:.2f}%)"
    cv2.putText(frame, text, (100, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)

    # Display and record
    cv2.imshow("Gesture Recognition", frame)
    out.write(frame)  # Save frame to mp4

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()
print("✅ Video saved as gesture_output.mp4")
