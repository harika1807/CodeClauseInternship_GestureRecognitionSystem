import cv2
import os

# Set the label for the gesture you want to collect (change this for each gesture)
label = 'thumbs_up'  # <- Change this to 'palm', 'thumbs_up', etc. when needed

# Set the save path
save_dir = os.path.join('dataset', label)
os.makedirs(save_dir, exist_ok=True)

# Start webcam
cap = cv2.VideoCapture(0)

print(f"📸 Collecting images for '{label}' gesture... Press 'q' to quit.")

count = 0
max_images = 100

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame.")
        break

    frame = cv2.flip(frame, 1)

    # Region of interest (ROI)
    roi = frame[100:400, 100:400]
    cv2.rectangle(frame, (100, 100), (400, 400), (0, 255, 0), 2)

    if count < max_images:
        file_path = os.path.join(save_dir, f"{label}_{count}.jpg")
        cv2.imwrite(file_path, roi)
        count += 1
    else:
        print("✅ Done collecting 100 images.")
        break

    cv2.putText(frame, f"Collecting: {label} ({count}/{max_images})", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    cv2.imshow("Collecting Gesture", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("🛑 Interrupted by user.")
        break

cap.release()
cv2.destroyAllWindows()
