import os

# Replace 'your_folder_path' with the path to your folder containing the images
folder_path = 'C:\\Users\\Emiliano Aguilar\\Desktop\\epics'

# List all files in the folder
files = os.listdir(folder_path)

# Sort the files if necessary (e.g., by file name)
files.sort()

# Initialize a counter for renaming
counter = 1

# Iterate through the files and rename them sequentially
for filename in files:
    # Check if the file is an image (you can add more image extensions if needed)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        # Generate the new filename with a sequential number
        new_filename = f'{counter:02d}.jpg'  # Adjust the format as needed
        
        # Build the full paths for the source and destination
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(src, dst)
        
        # Increment the counter
        counter += 1

print("Renaming complete.")
