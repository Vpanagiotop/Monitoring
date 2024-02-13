import os
import copy
from data_processing.DataProcessing import DataProcessing
from user_preferences.data_templates import DataModelEnvelope, DataFrameSchemas
from user_preferences import adjustable_parameters
from data_management.data_organization import group_data_by_layer
from data_processing import performance_assignment, filter_data
from output_utilities import store_default_prefs
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

        generate_performance_analysis(self, folder_name)


    def startd_export(self):
        print(f"Starting {self.tag} output process...")
        store_default_prefs.part_output(self)

    def refined_dataset_by_attribute(
        self, attribute_name, min_value=None, max_value=None
    ):
        self.filtered_dataset = copy.deepcopy(self)
        folder_name = f"part_0{self.part}"
        self.filtered_dataset.tag = f"{self.tag} - Filtered Data ({attribute_name})"
        self.filtered_dataset.layer = filter_data.apply_range_criteria(
            self.filtered_dataset, attribute_name, min_value, max_value
        )
        generate_performance_analysis(self.filtered_dataset, folder_name)

        return self.filtered_dataset


def generate_performance_analysis(part, folder_name):
    performance_assignment.assign_overview_performance(part, part.df)
    performance_assignment.assign_welding_performance(part, part.df)

    index_data = DataFrameSchemas.report
    part.report = create_report_dataframe(part, index_data)

    column_data = DataFrameSchemas.layerDetails
    statistic_value = DataFrameSchemas.statistic_value["layerDetails"]
    part.layer_details = create_layer_details_dataframe(
        part, column_data, statistic_value
    )
    part.output_directory = os.path.join(
        adjustable_parameters.output_directory, folder_name
    )
