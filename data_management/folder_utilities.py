import os
import shutil


def ensure_folder_exists(folder_directory, folder_name):
    folder = os.path.join(folder_directory, folder_name)
    if not os.path.exists(folder):
        os.makedirs(folder)
    return os.path.abspath(folder)


def delete_folder(folder_path):
    # folder_path = os.path.join(folder_directory, folder_name)
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' has been deleted.")
    else:
        print(f"Folder '{folder_path}' does not exist.")
