# File Organizer
This project helps you clean up cluttered directories, like your Downloads folder, by moving files into logical subfolders. For example, all your images (`.jpg`, `.png`, etc.) will be moved to an `Images` folder, documents (`.pdf`, `.docx`) will go to a `Documents` folder, and so on. Any files with an unrecognized extension will be placed in an `Others` folder.

## 🚀 How to Use

1.  **Save the Script**: Save the code as a Python file (e.g., `organizer.py`).
2.  **Configure the Directory**: Open the script in a text editor and change the `TARGET_DIRECTORY` variable to the path of the folder you want to organize.

    ```python
    TARGET_DIRECTORY = "/path/to/your/downloads/folder" 
    ```

3.  **Run the Script**: Open a terminal or command prompt, navigate to the directory where you saved the file, and run the script using the following command:

    ```bash
    python organizer.py
    ```

## 📝 Customizable File Types

The script includes a `FILE_TYPES` dictionary that you can easily modify. You can add new categories or extensions to suit your needs.

```python
FILE_TYPES = {
    'Images': ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'),
    'Documents': ('.pdf', '.docx', '.txt', '.xlsx', '.pptx'),
    # Add or remove categories as needed
}
