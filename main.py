from settings.project_settings import data_directory, output_directory
from data_processing.data_organization import arrange_data
from dataframe_operations.initialization import initial_dataframe
from data_visualization import plotting_functions
from Part import Part

folders = arrange_data(data_directory, output_directory)
assembled_data = initial_dataframe(output_directory, folders[0])

dataset = Part(assembled_data)

plotting_functions.rolling_mean(dataset.layer[0], "Records", "Heat Input")
plotting_functions.barplot(dataset, "Layer Number", "Heat Input")
plotting_functions.histogram(dataset, "Heat Input", 0.01)


xx =1
