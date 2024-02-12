import pandas as pd
from user_preferences.data_templates import DataModelEnvelope


def create_report_dataframe(instance, index_data):
    data = {
        "Info": [
            getattr(instance.overview, column.lower().replace(" ", "_"))
            for column in index_data
        ]
    }
    df = [pd.DataFrame(data, index=index_data)]

    for column in DataModelEnvelope.welding_performance:
        column_name = column.lower().replace(" ", "_")
        description_series = getattr(
            instance.performance, column_name
        ).description_series
        df.append(description_series)
    return pd.concat(df, axis=0).fillna("-")


def create_layer_details_dataframe(part, column_data, statistic_value):
    info_dataframe = []

    for layer in part.layer:
        data = [
            getattr(layer.overview, column.lower().replace(" ", "_"))
            for column in column_data
        ]

        for column in DataModelEnvelope.welding_performance:
            column_name = column.lower().replace(" ", "_")
            value = getattr(getattr(layer.performance, column_name), statistic_value)
            data.append(round(value, 2))

        df = pd.DataFrame(
            [data], columns=column_data + DataModelEnvelope.welding_performance
        )
        info_dataframe.append(df)
    return pd.concat(info_dataframe, ignore_index=True)
