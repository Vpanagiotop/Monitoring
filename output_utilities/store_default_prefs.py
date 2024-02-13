import os
from output_utilities import plotting_functions
from output_utilities import excel_writer

def part_output(df):
    dataframes = {
        "Report": df.report,
        "Layer Details": df.layer_details,
    }

    excel_file_path = os.path.join(df.output_directory, df.tag + " - summary.xlsx")
    excel_writer.dataframes_to_excel(
        dataframes, excel_file_path
    )

    plotting_functions.rolling_mean(df.layer[0], "Records", "Heat Input", save = "Yes")
    plotting_functions.rolling_mean(
        df.layer[len(df.layer) // 2], "Records", "Heat Input", save="Yes"
    )
    plotting_functions.rolling_mean(df.layer[-1], "Records", "Heat Input", save = "Yes")
    plotting_functions.barplot(df, "Layer Number", "Heat Input", save="Yes")
    plotting_functions.histogram(df, "Heat Input", 0.01, save = "Yes")
    plotting_functions.barplot(df, "Layer Number", "Records", save="Yes")
