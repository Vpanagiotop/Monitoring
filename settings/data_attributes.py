class MachineAttributes:
    timestamp = "Timestamp"
    current = "Current"
    voltage = "Voltage"


class FileNameAttributes:
    part = "Part"
    layer_value = "Layer Value"
    layer_number = "Layer Number"


class WeldingPerformanceAttributes:
    current = "Current"
    voltage = "Voltage"
    power = "Power"
    heat_input = "Heat Input"


class SpeedAttributes:
    travel_speed = "Travel Speed"
    wire_feed_speed = "Wire Feed Speed"
    speed_ratio = "Speed Ratio"


class TimeAttributes:
    production_time = "Production Time"
    total_tile = "Total Time"
    elapsed_time = "Elapsed Time"
    delta_time = "Delta Time"


# class DataFrameSchemas:
#     INITIAL = [
#         MachineAttributes.TIMESTAMP,
#         MachineAttributes.CURRENT,
#         MachineAttributes.VOLTAGE,
#         FileNameAttributes.PART,
#         FileNameAttributes.LAYER_VALUE,
#         FileNameAttributes.LAYER_NUMBER,
#     ]
#     PART = INITIAL + [
#         WeldingPerformanceAttributes.CURRENT,
#         WeldingPerformanceAttributes.VOLTAGE,
#         WeldingPerformanceAttributes.POWER,
#         WeldingPerformanceAttributes.HEAT_INPUT,
#     ]
#     LAYER = PART + [TimeAttributes.ELAPSED_TIME, TimeAttributes.DELTA_TIME]


# class PartLayerInfo:
#     COLUMNS = [
#         FileNameAttributes.PART,
#         FileNameAttributes.LAYER_VALUE,
#         FileNameAttributes.LAYER_NUMBER,
#         "Records",
#         TimeAttributes.PRODUCTION_TIME,
#         SpeedAttributes.TRAVEL_SPEED,
#         SpeedAttributes.WIRE_FEED_SPEED,
#         SpeedAttributes.SPEED_RATIO,
#     ]
#     STATISTIC_VALUE = "mean"


# class PartOverview:
#     ATTRIBUTES = [
#         FileNameAttributes.PART,
#         "Layers Number",
#         "Records",
#         TimeAttributes.PRODUCTION_TIME,
#         TimeAttributes.TOTAL_TIME,
#         SpeedAttributes.TRAVEL_SPEED,
#         SpeedAttributes.WIRE_FEED_SPEED,
#         SpeedAttributes.SPEED_RATIO,
#     ]
