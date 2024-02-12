from user_preferences.data_attributes import *

class DataModelEnvelope:
    initial = [
        MachineAttributes.timestamp,
        MachineAttributes.current,
        MachineAttributes.voltage,
        FileNameAttributes.part,
        FileNameAttributes.layer_value,
        FileNameAttributes.layer_number,
    ]
    part = [
        MachineAttributes.timestamp,
        MachineAttributes.current,
        MachineAttributes.voltage,
        FileNameAttributes.part,
        FileNameAttributes.layer_value,
        FileNameAttributes.layer_number,
        WeldingPerformanceAttributes.power,
        WeldingPerformanceAttributes.heat_input,
    ]
    layer = part + [TimeAttributes.elapsed_time, TimeAttributes.delta_time]

    welding_performance = [
        WeldingPerformanceAttributes.current,
        WeldingPerformanceAttributes.voltage,
        WeldingPerformanceAttributes.power,
        WeldingPerformanceAttributes.heat_input,
    ]


class DataFrameSchemas:
    report = [
        FileNameAttributes.part,
        ExtraAttributes.layers_number,
        ExtraAttributes.records,
        TimeAttributes.production_time,
        TimeAttributes.total_tile,
        SpeedAttributes.travel_speed,
        SpeedAttributes.wire_feed_speed,
        SpeedAttributes.speed_ratio
    ]
    layerDetails = [
        FileNameAttributes.part,
        FileNameAttributes.layer_value,
        FileNameAttributes.layer_number,
        ExtraAttributes.records,
        TimeAttributes.production_time,
        SpeedAttributes.travel_speed,
        SpeedAttributes.wire_feed_speed,
        SpeedAttributes.speed_ratio,
    ]
    statistic_value = {
        "layerDetails" : "mean"
    }
    
