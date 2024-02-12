import pandas as pd
from data_processing.DataProcessing import DataProcessing
from settings.dataframe_attributes import DataModelEnvelope
from data_processing.group_data import group_dataframe_by_layer
from data_processing import performance_assignment
from dataframe_operations.overview import create_overview_dataframe
import settings.project_settings as project_settings, column_definitions, progress_utilities

class Part:
    def __init__(self, df):
        self.df = df
        self.part = int(df["Part"].iloc[0])
        folder_name = f"part_0{self.part}"

        configuration_data = DataProcessing(folder_name=folder_name, df=df)
        configuration_data.add_columns_from_mapping(DataModelEnvelope.part)

        group_value = project_settings.group_by_value
        self.layer = group_dataframe_by_layer(self.part, folder_name, df, group_value)

        performance_assignment.assign_welding_performance(self, self.df)
        performance_assignment.generate_overview(self, df)

        self.layer_info_dataframe = create_layer_info_dataframe(
            self,
            column_definitions.part_layer_info,
            column_definitions.part_layer_info_statistic_value,
        )
        self.overview_dataframe = create_overview_dataframe(
            self, column_definitions.part_overview
        )
        self.tag = f"Part: {self.part}"


def create_layer_info_dataframe(part, column_data, statistic_value):
    info_dataframe = []

    for layer in part.layer:
        data = [
            getattr(layer.overview, column.lower().replace(" ", "_")) for column in column_data
        ]

        for column in column_definitions.welding_performance:
            column_name = column.lower().replace(" ", "_")
            value = getattr(getattr(layer.performance, column_name), statistic_value)
            data.append(round(value, 2))

        df = pd.DataFrame([data], columns=column_data + column_definitions.welding_performance)
        info_dataframe.append(df)
    return pd.concat(info_dataframe, ignore_index=True)
