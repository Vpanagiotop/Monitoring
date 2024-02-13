import copy
from user_preferences import adjustable_parameters

def add_units_to_label(key):
    if key in adjustable_parameters.units:
        key = f"{key} ({adjustable_parameters.units[key]})"
    return key


def add_units_to_dataframe(dataframe):
    units = adjustable_parameters.units
    df = dataframe#copy.deepcopy(dataframe)

    rename = {key: f"{key} ({units[key]})" for key in units}
    df.rename(columns=rename, index=rename, inplace=True)
    return df
