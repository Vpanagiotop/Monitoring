import os
import pickle
import pandas as pd
from utilities.progress_display import progress_bar, section_messages
from data_processing.DataProcessing import DataProcessing
from settings.dataframe_attributes import DataModelEnvelope


def initial_dataframe(output_directory, folder_name, replace="No"):
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

            configuration_data = DataProcessing(folder_name, csv_file, iter, df_i)

            configuration_data.add_columns_from_mapping(DataModelEnvelope.initial)

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
