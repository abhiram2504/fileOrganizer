import os 
import shutil

downloads_folder = os.path.expanduser('~/Downloads')

file_types = {
    'png': 'PNG_Images',
    'pdf': 'PDF_Files',
    'docx': 'Word_Documents',
    'xlsx': 'Excel_Documents',
}

# Create directories for each file type if they don't exist
for folder_name in file_types.values():
    folder_path = os.path.join(downloads_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)

# Iterate over files in the Downloads folder
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)
    
    # Check if the file is a regular file
    if os.path.isfile(file_path):
        # Get the file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()[1:]  # Remove the dot and convert to lowercase
        
        # Check if the file extension is in the file_types dictionary
        if file_extension in file_types:
            # Move the file to the corresponding folder
            destination_folder = os.path.join(downloads_folder, file_types[file_extension])
            shutil.move(file_path, destination_folder)
            print(f"Moved '{filename}' to '{destination_folder}'")
        else:
            print(f"Skipped '{filename}' (Unknown file type)")