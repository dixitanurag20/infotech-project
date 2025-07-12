import os
import shutil

FILE_TYPES = {
    "Documents": ['.pdf', '.doc', '.docx', '.txt'],
    "Images": ['.jpg', '.jpeg', '.png'],
    "Videos": ['.mp4', '.mkv', '.avi'],
}

def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_files(directory):
    if not os.path.isdir(directory):
        print("Path of the folder is not correct.")
        return

    for item in os.listdir(directory):
        file_path = os.path.join(directory, item)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(item)
            category = get_category(ext)
            category_folder = os.path.join(directory, category)
            os.makedirs(category_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(category_folder, item))
            print(f"{item} -> {category}/")


__name__ == "_main_"
folder = input("Enter folder path: ").strip()
organize_files(folder)