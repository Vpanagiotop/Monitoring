import os
import zipfile
from utilities.file_utilities import ensure_folder_exists
from utilities.progress_display import progress_bar

def arrange_data(data_directory, output_directory):
    file_list = [
        file for file in os.listdir(data_directory) if not file.startswith(".DS_Store")
    ]
    created_folders = []
    for iter, file in enumerate(file_list, start=1):
        part = file.split("_")[4][0:2]
        folder_name = f"part_0{int(part)+1}"
        folder_path = ensure_folder_exists(output_directory, folder_name)
        extract_to = ensure_folder_exists(folder_path, "csv_folder")
        zip_file = os.path.join(data_directory, file)
        csv_file = os.path.splitext(extract_to + "/" + file)[0] + ".csv"

        if not os.path.exists(csv_file):
            with zipfile.ZipFile(zip_file, "r") as zip_ref:
                zip_ref.extractall(extract_to)
        created_folders.append(folder_name)

        progress_bar(iter, len(file_list), prefix=f"Arrange Data:")

    return sorted(list(set(created_folders)))