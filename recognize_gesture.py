import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('gesture_model.h5')
label_names = sorted(os.listdir('dataset'))  # Adjust if your dataset path is different
img_size = 64

# Set up webcam
cap = cv2.VideoCapture(0)

# Video writer setup
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 20, (frame_width, frame_height))

cv2.namedWindow("Gesture Recognition", cv2.WINDOW_NORMAL)
cv2.moveWindow("Gesture Recognition", 100, 100)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    roi = frame[100:300, 100:300]
    img = cv2.resize(roi, (img_size, img_size))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)
    confidence = np.max(pred)
    class_idx = np.argmax(pred)
    class_name = f"{label_names[class_idx]} ({confidence*100:.1f}%)"


    cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 2)
    cv2.putText(frame, class_name, (100, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Write frame to video
    out.write(frame)

    # Show the frame
    cv2.imshow("Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
out.release()
cv2.destroyAllWindows()
