import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical

dataset_path = 'dataset'  # path inside Gesture_Recognition_System/
img_size = 64
data = []
labels = []
label_names = sorted(os.listdir(dataset_path))

# Encode class names to indexes
class_map = {name: i for i, name in enumerate(label_names)}

# Load data
for class_name in label_names:
    folder = os.path.join(dataset_path, class_name)
    for file in os.listdir(folder):
        img_path = os.path.join(folder, file)
        img = cv2.imread(img_path)
        if img is None:
            continue
        img = cv2.resize(img, (img_size, img_size))
        data.append(img)
        labels.append(class_map[class_name])

data = np.array(data, dtype='float32') / 255.0
labels = to_categorical(labels, num_classes=len(label_names))

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Build model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(img_size, img_size, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Dropout(0.3),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(len(label_names), activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test), batch_size=32)

model.save('gesture_model.h5')
print("✅ Model trained and saved as gesture_model.h5")
