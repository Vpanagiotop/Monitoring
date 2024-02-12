import column_definitions, progress_utilities
from ConfigurationManager import ConfigurationManager

class Layer:
    def __init__(self, df, folder_name):
        self.df = df
        configuration_data = ConfigurationManager(folder_name=folder_name, df=df)
        configuration_data.add_columns_from_mapping(column_definitions.layer_dataframe)

        performance = progress_utilities.assign_welding_performance(self, self.df)
        overview = progress_utilities.generate_overview(self, df)

        self.layer_number = df["Layer Number"].iloc[0]
        self.layer_value = df["Layer Value"].iloc[0]

        self.tag = f"Part: {self.overview.part} / Layer: {self.layer_number}"
