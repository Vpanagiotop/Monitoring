from user_preferences import adjustable_parameters


def add_units_to_label(key):
    if key in adjustable_parameters.units:
        key = f"{key} ({adjustable_parameters.units[key]})"
    return key
