from user_preferences.adjustable_parameters import data_directory, output_directory
from data_management import data_organization
from dataframe_operations.initialization import initial_dataframe
from data_processing.Part import Part
from visualization_exporter import plotting_functions


folders = data_organization.arrange_data(data_directory, output_directory)
assembled_data = initial_dataframe(output_directory, folders[0])

dataset = Part(assembled_data)

plotting_functions.rolling_mean(dataset.layer[0], "Records", "Heat Input")
plotting_functions.barplot(dataset, "Layer Number", "Heat Input")
plotting_functions.histogram(dataset, "Heat Input", 0.01)

xx = 1
