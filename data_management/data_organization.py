import os
import zipfile
from data_processing.Layer import Layer
from data_management.folder_utilities import ensure_folder_exists
from data_management.progress_display import progress_bar


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


def group_data_by_layer(part, folder_name, df, group_by_value):

    grouped_df = df.groupby(group_by_value)
    grouped_data = []
    iterations = len(df[group_by_value].unique())

    print(f"Part {part}: Grouping by {group_by_value}")

    for layer_number, layer in grouped_df:
        progress_bar(layer_number, iterations, f"Layer {layer_number}/{iterations}:")
        grouped_data.append(Layer(layer, folder_name))
    return grouped_data
