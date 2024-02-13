import os
import matplotlib.pyplot as plt
def add_mean_horizontal_line(mean, y_label):
    plt.axhline(
        mean,
        color="red",
        linestyle="--",
        label=f"Mean {y_label} = {mean:.2f}",
    )


def set_plot_attributes(fig, title, x_label, y_label):
    plt.title(title, fontweight="bold", fontsize=12)
    plt.xlabel(x_label, fontweight="bold", fontsize=12)
    plt.ylabel(y_label, fontweight="bold", fontsize=12)
    plt.tick_params(axis="x", which="both", labelsize=12)
    plt.tick_params(axis="y", which="both", labelsize=12)

    handles, labels = plt.gca().get_legend_handles_labels()
    labels_exist = any(label not in ["", "_nolegend_"] for label in labels)
    if labels_exist:
        plt.legend()

    plt.grid()
    # plt.show(fig)


def save_figure(fig, dataset, title, save):
    if save == "Yes":
        save_path = os.path.join(dataset.output_directory, title + ".png")
        fig.savefig(save_path)
        plt.close(fig)
