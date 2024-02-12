machine = ["Timestamp", "Current", "Voltage"]
file_name = ["Part", "Layer Value", "Layer Number"]
welding_performance = ["Current", "Voltage", "Power", "Heat Input"]
speed_attributes = ["Travel Speed", "Wire Feed Speed", "Speed Ratio"]
time_attributes = ["Production Time", "Total Time", "Elapsed Time", "Delta Time"]


initial_dataframe = machine + file_name
part_dataframe = machine + file_name + welding_performance
layer_dataframe = part_dataframe + ["Elapsed Time", "Delta Time"]

part_layer_info = file_name + ["Records", "Production Time"] + speed_attributes
part_layer_info_statistic_value = "mean"
part_overview = [
    "Part",
    "Layers Number",
    "Records",
    "Production Time",
    "Total Time",
] + speed_attributes


part = {
    "dataframe": {
        "Timestamp",
        "Current",
        "Voltage",
        "Layer Value",
        "Layer Number",
        "Part",
        "Power",
        "Heat Input",
    },
    "overview": [
        "Part",
        "Layers Number",
        "Records",
        "Production Time",
        "Total Time",
        "Travel Speed",
        "Wire Feed Speed",
        "Speed Ratio",
    ],
    "Layer Information": {
        "columns": [
            "Layer Number",
            "Layer Value",
            "Records",
            "Production Time",
            "Travel Speed",
            "Wire Feed Speed",
            "Speed Ratio",
        ],
        "statistic value": "mean",
    },
}
