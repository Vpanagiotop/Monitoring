import settings.project_settings as project_settings

class DataProcessing:
    def __init__(self, folder_name=None, csv_file=None, iteration=None, df=None):
        self.folder_name = folder_name
        self.csv_file = csv_file
        self.iteration = iteration
        self.df = df

    def assign_timestamp(self):
        return self.df["Timestamp"]

    def assign_current(self):
        return self.df["Current"]

    def assign_voltage(self):
        return self.df["Voltage"]

    def assign_part_tag(self):
        return int("".join(filter(str.isdigit, self.folder_name)))

    def calculate_layer_value(self):
        return int(self.csv_file.split("-")[3]) + 1

    def calculate_layer_number(self):
        return self.iteration

    def calculate_power(self):
        return self.df["Current"] * self.df["Voltage"]

    def assign_travel_speed(self):
        return project_settings.travel_speed[self.folder_name]

    def assign_wire_feed_speed(self):
        return project_settings.wire_feed_speed[self.folder_name]

    def calculate_speed_ratio(self):
        TS = project_settings.travel_speed[self.folder_name]
        WFS = project_settings.wire_feed_speed[self.folder_name]
        return round(WFS / TS * 1000 / 60,2)

    def calculate_heat_input(self):
        travel_speed = project_settings.travel_speed[self.folder_name]
        heat_input = self.df["Current"] * self.df["Voltage"] / travel_speed
        return heat_input

    def calculate_elapsed_time(self):
        return (self.df["Timestamp"] - self.df["Timestamp"].iloc[0]).dt.total_seconds()

    def calculate_delta_time(self):
        return self.df["Timestamp"].diff().dt.total_seconds()

    def calculate_records(self):
        return self.df.shape[0]

    def add_columns_from_mapping(self, columns):
        for col_name in columns:
            if col_name in self.df:
                pass
            else:
                self.df[col_name] = function_mapping[col_name](self)


function_mapping = {
    "Part": DataProcessing.assign_part_tag,
    "Layer Value": DataProcessing.calculate_layer_value,
    "Layer Number": DataProcessing.calculate_layer_number,
    "Timestamp": DataProcessing.assign_timestamp,
    "Current": DataProcessing.assign_current,
    "Voltage": DataProcessing.assign_voltage,
    "Power": DataProcessing.calculate_power,
    "Travel Speed": DataProcessing.assign_travel_speed,
    "Wire Feed Speed": DataProcessing.assign_wire_feed_speed,
    "WFS / TS": DataProcessing.calculate_speed_ratio,
    "Heat Input": DataProcessing.calculate_heat_input,
    "Elapsed Time": DataProcessing.calculate_elapsed_time,
    "Delta Time": DataProcessing.calculate_delta_time,
    "Records": DataProcessing.calculate_records,
}
