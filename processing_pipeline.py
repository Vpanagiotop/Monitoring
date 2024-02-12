import os, zipfile, pickle
import pandas as pd
from ConfigurationManager import ConfigurationManager
from progress_display import progress_bar, section_messages
from progress_utilities import ensure_folder_exists
from column_definitions import initial_dataframe

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


def build_dataframe(output_directory, folder_name, replace="No"):
    part_directory = os.path.join(output_directory, folder_name, "csv_folder")
    csv_files = [f for f in os.listdir(part_directory) if f.endswith(".csv")]
    df_directory = os.path.join(output_directory, folder_name, f"{folder_name}_df.pkl")

    if os.path.isfile(df_directory) and replace == "No":
        with open(df_directory, "rb") as file:
            df = pickle.load(file)

        messages = [
            f"The DataFrame {folder_name}_dataframe.pkl already exists.",
            f"File path: {df_directory}",
        ]

    else:
        section_messages([f"Create Data Frame"])

        df = []

        for iter, csv_file in enumerate(sorted(csv_files), start=1):
            file_directory = os.path.join(part_directory, csv_file)

            df_i = pd.read_csv(file_directory, sep=";", parse_dates=["Timestamp"])

            configuration_data = ConfigurationManager(folder_name, csv_file, iter, df_i)

            configuration_data.add_columns_from_mapping(initial_dataframe)

            df.append(df_i)

            progress_bar(iter, len(csv_files), prefix=f"{folder_name} / Layer_{iter}:")

        df = pd.concat(df, ignore_index=True)

        with open(f"{df_directory}", "wb") as file:
            pickle.dump(df, file)

        messages = [
            f"The DataFrame {folder_name}_dataframe.pkl has been created.",
            f"File path: {df_directory}",
        ]

    section_messages(messages)

    return df
