from configurations import data_directory, output_directory
from Part import Part
import processing_pipeline, plotting_tool

folders = processing_pipeline.arrange_data(data_directory, output_directory)
assembled_data = processing_pipeline.build_dataframe(output_directory, folders[0])

dataset = Part(assembled_data)

plotting_tool.rolling_mean(dataset.layer[0], "Records", "Heat Input")
plotting_tool.barplot(dataset, "Layer Number", "Heat Input")
plotting_tool.histogram(dataset, "Heat Input", 0.01)



xx =1
