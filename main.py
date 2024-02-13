from user_preferences.adjustable_parameters import data_directory, output_directory
from data_management import data_organization
from dataframe_operations.initialization import initial_dataframe
from data_processing.Part import Part
from output_utilities import plotting_functions, excel_writer, store_default_prefs


folders = data_organization.arrange_data(data_directory, output_directory)
assembled_data = initial_dataframe(output_directory, folders[0])

dataset = Part(assembled_data)

# dataset.startd_export()
filtered_dataset = dataset.refined_dataset_by_attribute("Records", 1000)
dataset.filtered_dataset.startd_export()
from data_processing import filter_data

filter_data.apply_range_criteria(dataset, "Records", 1000)
store_default_prefs.part_output(dataset)
part = []
for folder in folders:
    assembled_data = initial_dataframe(output_directory, folder)
    dataset = Part(assembled_data)

    store_default_prefs.part_output(dataset)
    part.append([dataset])
excel_writer.dataframe_to_excel(dataset, "report")
excel_writer.dataframe_to_excel(dataset.layer[0], "report")
excel_writer.dataframe_to_excel(dataset, "layer_details")
plotting_functions.barplot(dataset, "Layer Number", "Heat Input")
plotting_functions.histogram(dataset, "Heat Input", 0.01)


xx = 1
