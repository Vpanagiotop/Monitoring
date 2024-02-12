from utilities.progress_display import progress_bar
from Layer import Layer

def group_dataframe_by_layer(part, folder_name, df, group_by_value):

    grouped_df = df.groupby(group_by_value)
    grouped_dataframe = []
    iterations = len(df[group_by_value].unique())

    print(f"Part {part}: Grouping by {group_by_value}")

    for layer_number, layer in grouped_df:
        progress_bar(layer_number, iterations, f"Layer {layer_number}/{iterations}:")
        grouped_dataframe.append(Layer(layer, folder_name))
    return grouped_dataframe
