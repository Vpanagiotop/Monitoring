import column_definitions, settings.project_settings as project_settings
import pandas as pd
from datetime import timedelta
from data_processing.DataProcessing import DataProcessing
from data_processing.ColumnStatistics import ColumnStatistics




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
