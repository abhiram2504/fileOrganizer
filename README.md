# Downloads Folder Organizer

This script organizes files in the `Downloads` folder by moving them into subdirectories based on their file extensions.

## Features

- Automatically creates directories for different file types if they do not exist.
- Moves files into their respective directories based on their file extension.
- If a file's extension is not recognized, it moves the file to a "Random_Docs" folder.

## Supported File Types

The script organizes the following file types into corresponding folders:

- `.png` files are moved to `PNG_Images`
- `.pdf` files are moved to `PDF_Files`
- `.docx` files are moved to `Word_Documents`
- `.xlsx` files are moved to `Excel_Documents`
- Files with other extensions are moved to `Random_Docs`

## Prerequisites

- Python 3.x

## Usage

1. Clone or download this repository to your local machine.
2. Ensure you have Python 3.x installed.
3. Run the script using the command:
   ```sh
   python organize_downloads.py
