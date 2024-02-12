from progress_utilities import apply_units
import matplotlib.pyplot as plt
import seaborn as sns

def rolling_mean(dataset, x_column, y_column, window_size=None):
    if window_size == None:
        window_size = max(int(5e-4 * len(dataset.df[y_column])), 1)
    
    plt.figure(figsize=(10, 6))

    if x_column == "Records":
        x = range(len(dataset.df))
    else:
        x = dataset.df[x_column]
    y = dataset.df[y_column].rolling(window=window_size).mean()
    
    x_label = apply_units(x_column)
    y_label = apply_units(y_column)
    title = f"{dataset.tag} - Rolling mean of {y_column}"

    plt.plot(x, y, label=f"Rolling mean")

    add_mean_horizontal_line(dataset.df[y_column].mean(), y_label)
    set_plot_attributes(title, x_label, y_label)

def barplot(dataset, x_column, y_column):
    plt.figure(figsize=(10, 6))

    x_label = apply_units(x_column)
    y_label = apply_units(y_column)
    title = f"{dataset.tag} - Bar plot of {y_column}"

    plt.bar(dataset.layer_info_dataframe[x_column], dataset.layer_info_dataframe[y_column])
    
    add_mean_horizontal_line(dataset.layer_info_dataframe[y_column].mean(), y_label)
    set_plot_attributes(title, x_label, y_label)

def histogram(dataset, column, frac = 0.1):
    plt.figure(figsize=(10, 6))
    subsampled_data = dataset.df.sample(frac=frac)
    sns.histplot(subsampled_data, x=column, kde=True)
    title = f"{dataset.tag} - Histogram of {column} (frac = {frac})"
    x_label = apply_units(column)
    y_label = "Count"
    set_plot_attributes(title, x_label, y_label)



def add_mean_horizontal_line(mean, y_label):
    plt.axhline(
        mean,
        color="red",
        linestyle="--",
        label=f"Mean {y_label} = {mean:.2f}",
    )

def set_plot_attributes(title, x_label, y_label):
    plt.title(title, fontweight='bold', fontsize=12)
    plt.xlabel(x_label, fontweight='bold', fontsize=12)
    plt.ylabel(y_label, fontweight='bold', fontsize=12)
    plt.tick_params(axis='x', which='both', labelsize=12)
    plt.tick_params(axis='y', which='both', labelsize=12)
    plt.grid()
    plt.legend()
    plt.show()
