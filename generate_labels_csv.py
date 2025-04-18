import pandas as pd

# Load your original CSV
df = pd.read_csv('hagrid_labels.csv')

# Map label to folder path
folder_mapping = {
    'fist': 'dataset/fist/',
    'palm': 'dataset/palm/',
    'thumb_up': 'dataset/thumb_up/',
    'thumb_down': 'dataset/thumb_down/',
    'victory': 'dataset/victory/'
}

# Update the image column with the correct path
df['image'] = df.apply(lambda row: folder_mapping[row['label']] + row['image'], axis=1)

# Save the updated CSV
df.to_csv('updated_hagrid_labels.csv', index=False)

print("CSV updated successfully!")
