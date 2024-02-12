from datetime import timedelta
from data_processing.ColumnStatistics import ColumnStatistics
from data_processing.DataProcessing import DataProcessing
from user_preferences.data_templates import DataModelEnvelope

def assign_welding_performance(instance, df):
    setattr(instance, "performance", type("Performance", (object,), {}))

    for column in DataModelEnvelope.welding_performance:
        setattr(
            instance.performance,
            column.lower().replace(" ", "_"),
            ColumnStatistics(df, column),
        )
    return instance.performance


def assign_overview_performance(instance, df):
    part = int(df["Part"].iloc[0])
    folder_name = f"part_0{part}"

    configuration_data = DataProcessing(folder_name=folder_name, df=df)

    setattr(instance, "overview", type("Performance", (object,), {}))

    instance.overview.part = part
    instance.overview.folder_name = folder_name

    instance.overview.wire_feed_speed = configuration_data.assign_wire_feed_speed()
    instance.overview.travel_speed = configuration_data.assign_travel_speed()
    instance.overview.speed_ratio = configuration_data.calculate_speed_ratio()

    instance.overview.records = configuration_data.calculate_records()

    from data_processing.Part import Part
    from data_processing.Layer import Layer

    if isinstance(instance, Part):
        instance.overview.total_time = df["Timestamp"].max() - df["Timestamp"].min()
        instance.overview.layers_number = len(df["Layer Number"].unique())
        production_time = sum(
            [layer.overview.production_time for layer in instance.layer]
        )
        instance.overview.production_time = timedelta(seconds=production_time)
    elif isinstance(instance, Layer):
        instance.overview.production_time = df["Elapsed Time"].iloc[-1]
        instance.overview.layer_number = df["Layer Number"].iloc[0]
        instance.overview.layer_value = df["Layer Value"].iloc[0]

    return instance.overview
