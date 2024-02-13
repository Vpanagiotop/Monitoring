from data_management.data_formatting import add_units_to_label
from output_utilities.plot_utilities import *
import matplotlib.pyplot as plt
import seaborn as sns


def rolling_mean(dataset, x_column, y_column, window_size=None, save="No"):
    if window_size == None:
        window_size = max(int(5e-4 * len(dataset.df[y_column])), 1)

    fig, ax = plt.subplots(figsize=(10, 6))

    if x_column == "Records":
        x = range(len(dataset.df))
    else:
        x = dataset.df[x_column]
    y = dataset.df[y_column].rolling(window=window_size).mean()

    x_label = add_units_to_label(x_column)
    y_label = add_units_to_label(y_column)
    title = f"{dataset.tag} - Rolling mean of {y_column}"

    plt.plot(x, y, label=f"Rolling mean (window size: {window_size})")

    add_mean_horizontal_line(dataset.df[y_column].mean(), y_label)
    set_plot_attributes(fig, title, x_label, y_label)
    save_figure(fig, dataset, title, save)


def barplot(dataset, x_column, y_column, save="No"):
    fig, ax = plt.subplots(figsize=(10, 6))

    x_label = add_units_to_label(x_column)
    y_label = add_units_to_label(y_column)
    title = f"{dataset.tag} - Bar plot of {y_column}"

    plt.bar(dataset.layer_details[x_column], dataset.layer_details[y_column])

    add_mean_horizontal_line(dataset.layer_details[y_column].mean(), y_label)
    set_plot_attributes(fig, title, x_label, y_label)
    save_figure(fig, dataset, title, save)


def histogram(dataset, column, frac=0.01, save="No"):
    fig, ax = plt.subplots(figsize=(10, 6))

    subsampled_data = dataset.df.sample(frac=frac)
    legend = f"{frac * 100}% of the original Dataset"

    sns.histplot(subsampled_data, x=column, kde=True, label=legend)

    title = f"{dataset.tag} - Histogram of {column}"
    x_label = add_units_to_label(column)
    y_label = "Count"
    set_plot_attributes(fig, title, x_label, y_label)
    save_figure(fig, dataset, title, save)
