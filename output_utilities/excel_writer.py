import os
import pandas as pd
from data_management.data_formatting import add_units_to_dataframe


def dataframe_to_excel(dataframe, type, sheet_name = "Initial Data"):
    df = getattr(dataframe, type)
    id = f"({dataframe.tag})"
    excel_file_path = os.path.join(dataframe.output_directory, type + id + ".xlsx")
    export_df = add_units_to_dataframe(df.copy())
    export_df.to_excel(excel_file_path, index=True, sheet_name=sheet_name)


def dataframes_to_excel(df_dict, excel_file_path):
    with pd.ExcelWriter(excel_file_path) as writer:
        for sheet_name, df in df_dict.items():
            if "Timestamp" in df.columns:
                df = df.drop(columns=["Timestamp"])
            df.to_excel(writer, sheet_name=sheet_name)
