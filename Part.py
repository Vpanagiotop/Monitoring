import pandas as pd
import configurations, column_definitions, progress_utilities
from Layer import Layer
from ConfigurationManager import ConfigurationManager
from progress_display import progress_bar

class Part:
    def __init__(self, df):
        self.df = df
        self.part = int(df["Part"].iloc[0])
        folder_name = f"part_0{self.part}"

        configuration_data = ConfigurationManager(folder_name=folder_name, df=df)
        configuration_data.add_columns_from_mapping(column_definitions.part_dataframe)

        group_value = configurations.group_by_value
        self.layer = group_dataframe_by_layer(self.part, folder_name, df, group_value)

        progress_utilities.assign_welding_performance(self, self.df)
        progress_utilities.generate_overview(self, df)

        self.layer_info_dataframe = create_layer_info_dataframe(
            self,
            column_definitions.part_layer_info,
            column_definitions.part_layer_info_statistic_value,
        )
        self.overview_dataframe = progress_utilities.create_overview_dataframe(
            self, column_definitions.part_overview
        )
        self.tag = f"Part: {self.part}"

def group_dataframe_by_layer(part, folder_name, df, group_by_value):

    grouped_df = df.groupby(group_by_value)
    grouped_dataframe = []
    iterations = len(df[group_by_value].unique())

    print(f"Part {part}: Grouping by {group_by_value}")

    for layer_number, layer in grouped_df:
        progress_bar(layer_number, iterations, f"Layer {layer_number}/{iterations}:")
        grouped_dataframe.append(Layer(layer, folder_name))
    return grouped_dataframe

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
