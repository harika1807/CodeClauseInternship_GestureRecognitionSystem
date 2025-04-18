import os
import shutil

# Source base directory (update this if different)
source_base = "hagrid-sample-30k-384p/hagrid_30k"

# Destination base directory
dest_base = "dataset"

# Map folder names to desired gesture names
gesture_map = {
    "train_val_fist": "fist",
    "train_val_palm": "palm",
    "train_val_thumb_up": "thumb_up",
    "train_val_thumb_down": "thumb_down",
    "train_val_victory": "victory"
}

# Copy each gesture
for source_folder, gesture_name in gesture_map.items():
    source_path = os.path.join(source_base, source_folder)
    dest_path = os.path.join(dest_base, gesture_name)

    os.makedirs(dest_path, exist_ok=True)

    for img_file in os.listdir(source_path):
        src_file = os.path.join(source_path, img_file)
        dst_file = os.path.join(dest_path, img_file)
        shutil.copy(src_file, dst_file)

    print(f"✅ Copied {gesture_name} images to {dest_path}")
