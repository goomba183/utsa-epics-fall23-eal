import os
import shutil

# Replace these paths with your actual folder paths
source_folder = 'C:\\Users\\Emiliano Aguilar\\Desktop\\epics'
destination_folders = [
    'C:\\Users\\Emiliano Aguilar\\Desktop\\epics/folder_1',
    'C:\\Users\\Emiliano Aguilar\\Desktop\\epics/folder_2',
    'C:\\Users\\Emiliano Aguilar\\Desktop\\epics/folder_3',
    'C:\\Users\\Emiliano Aguilar\\Desktop\\epics/folder_4',
    'C:\\Users\\Emiliano Aguilar\\Desktop\\epics/folder_5'
]

# List all files in the source folder
files = os.listdir(source_folder)

# Create the destination folders if they don't exist
for folder in destination_folders:
    os.makedirs(folder, exist_ok=True)

# Iterate through the files and move them sequentially
for i, file in enumerate(files):
    source_file = os.path.join(source_folder, file)
    destination_folder = destination_folders[i % len(destination_folders)]
    destination_file = os.path.join(destination_folder, file)
    
    shutil.move(source_file, destination_file)
    
    print(f"Moved {file} to {destination_folder}")

print("All files moved.")
