import os


def ensure_folder_exists(folder_directory, folder_name):
    folder = os.path.join(folder_directory, folder_name)
    if not os.path.exists(folder):
        os.makedirs(folder)
    return os.path.abspath(folder)
