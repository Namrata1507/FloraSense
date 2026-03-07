import os
import shutil

# Show current location
print("Current working directory:", os.getcwd())

# Show folders inside agri_data
print("Files inside agri_data:", os.listdir("agri_data"))

# Source folder (where original files are)
source = "agri_data"

# Destination folders
img_folder = os.path.join("agri_data", "images", "train")
label_folder = os.path.join("agri_data", "labels", "train")

# Create folders if they don't exist
os.makedirs(img_folder, exist_ok=True)
os.makedirs(label_folder, exist_ok=True)

# Loop through files in source
for file in os.listdir(source):
    file_path = os.path.join(source, file)

    # Move image files
    if file.endswith(".jpg") or file.endswith(".png"):
        shutil.move(file_path, os.path.join(img_folder, file))

    # Move label files
    elif file.endswith(".txt"):
        shutil.move(file_path, os.path.join(label_folder, file))

print("Sorting completed")