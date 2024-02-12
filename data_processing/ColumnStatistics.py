import pandas as pd

class ColumnStatistics:
    def __init__(self, df, column_name):
        column_describe = df[column_name].describe()
        self.count = int(column_describe["count"])
        self.mean = column_describe["mean"]
        self.std = column_describe["std"]
        self.minimum = column_describe["min"]
        self.q1 = column_describe["25%"]
        self.median = column_describe["50%"]
        self.q3 = column_describe["75%"]
        self.maximum = column_describe["max"]
        self.description_series = pd.DataFrame(column_describe).T.round(2)
