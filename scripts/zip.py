import zipfile
import os

def zip_directory(directory, zip_name):
    try:
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, directory))
    except FileNotFoundError:
        print(f"The directory {directory} does not exist.")
    except PermissionError:
        print(f"Permission denied for {zip_name}.")
    except Exception as e:
        print(f"An error occurred: {e}")

directory = "result"
zip_name = "kotatsu.zip"
zip_directory(directory, zip_name)