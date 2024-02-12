from data_processing.DataProcessing import DataProcessing
from user_preferences.data_templates import DataModelEnvelope, DataFrameSchemas
from user_preferences import adjustable_parameters
from data_management.data_organization import group_data_by_layer
from data_processing import performance_assignment
from visualization_exporter.plotting_functions import *
from dataframe_operations.summary import (
    create_report_dataframe,
    create_layer_details_dataframe,
)


class Part:
    def __init__(self, df):
        self.df = df
        self.part = int(df["Part"].iloc[0])
        self.tag = f"Part: {self.part}"
        folder_name = f"part_0{self.part}"

        configuration_data = DataProcessing(folder_name=folder_name, df=df)
        configuration_data.add_columns_from_mapping(DataModelEnvelope.part)

        group_value = adjustable_parameters.group_by_value
        self.layer = group_data_by_layer(self.part, folder_name, df, group_value)

        performance_assignment.assign_overview_performance(self, df)
        performance_assignment.assign_welding_performance(self, self.df)

        index_data = DataFrameSchemas.report
        self.report = create_report_dataframe(self, index_data)

        column_data = DataFrameSchemas.layerDetails
        statistic_value = DataFrameSchemas.statistic_value["layerDetails"]
        self.layer_details = create_layer_details_dataframe(self, column_data, statistic_value)
