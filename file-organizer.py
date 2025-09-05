import os
import shutil

# --- Configuration ---
# Set the directory you want to organize.
# A good starting point is your Downloads folder.
TARGET_DIRECTORY = "/path/to/your/downloads/folder"

# Define file type categories and their extensions
FILE_TYPES = {
    'Images': ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'),
    'Documents': ('.pdf', '.docx', '.txt', '.xlsx', '.pptx'),
    'Videos': ('.mp4', '.mov', '.avi', '.mkv'),
    'Audio': ('.mp3', '.wav', '.flac'),
    'Archives': ('.zip', '.rar', '.7z'),
    'Scripts': ('.py', '.sh', '.js', '.html', '.css'),
}

def organize_files(directory):
    """Organizes files in a given directory into subfolders by type."""
    if not os.path.isdir(directory):
        print(f"Error: Directory not found at {directory}")
        return

    for filename in os.listdir(directory):
        # Skip directories and the script itself
        if os.path.isdir(os.path.join(directory, filename)) or filename == os.path.basename(__file__):
            continue

        file_extension = os.path.splitext(filename)[1].lower()

        # Check if the file matches any of the defined categories
        found_category = False
        for category, extensions in FILE_TYPES.items():
            if file_extension in extensions:
                destination_folder = os.path.join(directory, category)

                # Create the destination folder if it doesn't exist
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                # Move the file
                shutil.move(os.path.join(directory, filename), destination_folder)
                print(f"Moved {filename} to {category} folder.")
                found_category = True
                break

        if not found_category:
            other_folder = os.path.join(directory, 'Others')
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(os.path.join(directory, filename), other_folder)
            print(f"Moved {filename} to 'Others' folder.")

if __name__ == "__main__":
    print(f"Starting file organization in {TARGET_DIRECTORY}...")
    organize_files(TARGET_DIRECTORY)
    print("File organization complete!")
