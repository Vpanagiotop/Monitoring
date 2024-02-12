import progress_utilities
from data_processing import performance_assignment
from settings.dataframe_attributes import DataModelEnvelope
from data_processing.DataProcessing import DataProcessing

class Layer:
    def __init__(self, df, folder_name):
        self.df = df
        configuration_data = DataProcessing(folder_name=folder_name, df=df)
        configuration_data.add_columns_from_mapping(DataModelEnvelope.layer)

        performance_assignment.assign_welding_performance(self, self.df)
        performance_assignment.generate_overview(self, df)

        self.layer_number = df["Layer Number"].iloc[0]
        self.layer_value = df["Layer Value"].iloc[0]

        self.tag = f"Part: {self.overview.part} / Layer: {self.layer_number}"
