from settings.data_attributes import *


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
        WeldingPerformanceAttributes.heat_input
    ]
