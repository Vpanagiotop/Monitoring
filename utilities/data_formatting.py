from settings import project_settings
def add_units_to_label(key):
    if key in project_settings.units:
        key = f"{key} ({project_settings.units[key]})"
    return key
