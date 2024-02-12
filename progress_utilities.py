import os, column_definitions, configurations
import pandas as pd
from datetime import timedelta
from ConfigurationManager import ConfigurationManager
from ColumnStatistics import ColumnStatistics

def ensure_folder_exists(folder_directory, folder_name):
    folder = os.path.join(folder_directory, folder_name)
    if not os.path.exists(folder):
        os.makedirs(folder)
    return os.path.abspath(folder)

def assign_welding_performance(instance, df):
    setattr(instance, "performance", type("Performance", (object,), {}))

    for column in column_definitions.welding_performance:
        setattr(
            instance.performance,
            column.lower().replace(" ", "_"),
            ColumnStatistics(df, column),
        )
    return instance.performance

def generate_overview(instance, df):
    part = int(df["Part"].iloc[0])
    folder_name = f"part_0{part}"

    configuration_data = ConfigurationManager(folder_name=folder_name, df=df)

    setattr(instance, "overview", type("Overview", (object,), {}))

    instance.overview.part = part
    instance.overview.folder_name = folder_name

    instance.overview.wire_feed_speed = configuration_data.assign_wire_feed_speed()
    instance.overview.travel_speed = configuration_data.assign_travel_speed()
    instance.overview.speed_ratio = configuration_data.calculate_speed_ratio()

    instance.overview.records = configuration_data.calculate_records()

    from Part import Part
    from Layer import Layer
    if isinstance(instance, Part):
        instance.overview.total_time = df["Timestamp"].max() - df["Timestamp"].min()
        instance.overview.layers_number = len(df["Layer Number"].unique())
        production_time = sum([layer.overview.production_time for layer in instance.layer])
        instance.overview.production_time = timedelta(seconds=production_time)
    elif isinstance(instance, Layer):
        instance.overview.production_time = df["Elapsed Time"].iloc[-1]
        instance.overview.layer_number = df["Layer Number"].iloc[0]
        instance.overview.layer_value = df["Layer Value"].iloc[0]

    return instance.overview


def apply_units(key):
    if key in configurations.units:
        key = f"{key} ({configurations.units[key]})"
    return key


def create_overview_dataframe(instance, index_data):
    data = {
        "Info": [
            getattr(instance.overview, column.lower().replace(" ", "_"))
            for column in index_data
        ]
    }
    df = [pd.DataFrame(data, index=index_data)]
    for column in column_definitions.welding_performance:
        column_name = column.lower().replace(" ", "_")
        description_series = getattr(
            instance.performance, column_name
        ).description_series
        df.append(description_series)
    return pd.concat(df, axis=0).fillna("-")

# def dataframe_to_excel(df, output_directory, excel_file_name):
#     excel_file_path = os.path.join(output_directory, excel_file_name + ".xlsx")
#     export_df = rename(df.copy())
#     export_df.to_excel(excel_file_path, index=True)
