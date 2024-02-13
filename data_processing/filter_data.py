import numpy as np

def apply_range_criteria(dataframe, attribute_name, min_value=None, max_value=None):
    included_layers = []

    for layer in dataframe.layer:
        attr_value = getattr(layer.overview, attribute_name.lower())

        if (min_value is None or attr_value >= min_value) and (
            max_value is None or attr_value <= max_value
        ):
            included_layers.append(layer)

    return included_layers


def define_stabilization_index(layer, column, percent=0.02, std_multiplier=3):
    window_size = max(int(5e-4 * len(layer[column])), 1)
    rolling_mean = layer[column].rolling(window=window_size).mean()
    rolling_mean_stats = rolling_mean.describe()

    percent_index = int(len(rolling_mean) * percent)
    rolling_mean_index = rolling_mean.iloc[0:percent_index]

    average_rolling_mean = rolling_mean_stats["mean"]
    std_rolling_mean = rolling_mean_stats["std"]

    max_threshold = rolling_mean_index.max()
    min_threshold = rolling_mean_index.min()

    upper_bound = min(
        average_rolling_mean + std_multiplier * std_rolling_mean, max_threshold - 1
    )
    lower_bound = max(
        average_rolling_mean - std_multiplier * std_rolling_mean, min_threshold + 1
    )

    upper_index = np.where(rolling_mean_index > upper_bound)[0][-1]
    lower_index = np.where(rolling_mean_index < lower_bound)[0][-1]

    return max(upper_index, lower_index)
