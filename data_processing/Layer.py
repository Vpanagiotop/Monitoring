import os
from user_preferences import adjustable_parameters
from data_processing import performance_assignment
from user_preferences.data_templates import DataModelEnvelope, DataFrameSchemas
from data_processing.DataProcessing import DataProcessing
from dataframe_operations.summary import create_report_dataframe

class Layer:
    def __init__(self, df, folder_name):
        self.df = df
        configuration_data = DataProcessing(folder_name=folder_name, df=df)
        configuration_data.add_columns_from_mapping(DataModelEnvelope.layer)

        performance_assignment.assign_welding_performance(self, self.df)
        performance_assignment.assign_overview_performance(self, df)

        self.layer_number = df["Layer Number"].iloc[0]
        self.layer_value = df["Layer Value"].iloc[0]

        self.tag = f"Part: {self.overview.part} - Layer: {self.layer_number}"
        self.output_directory = os.path.join(
            adjustable_parameters.output_directory, folder_name
        )
        index_data = DataFrameSchemas.layer_report
        self.report = create_report_dataframe(self, index_data)
