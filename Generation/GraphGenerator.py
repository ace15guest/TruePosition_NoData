import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.ticker import AutoMinorLocator

from Analysis.DataError import Radial_Error



def ScatterPlot(x_ideal=(), x_meas=(), y_ideal=(), y_meas=(), ideal_marker="+", real_marker="+",
                s1=40, s2=40, title=""):
    fig = Figure()
    fig.patch.set_facecolor('#f0f0ed')
    fig.patch.set_alpha(1)
    fig.tight_layout()
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_aspect('auto')
    ax.grid(False)
    # Moving Spines to be centered
    ax.spines.left.set_position('center')
    ax.spines.bottom.set_position('center')
    # Scatter Points
    ax.scatter(x_ideal, y_ideal, marker=ideal_marker, s=s1)
    ax.scatter(x_meas, y_meas, marker=real_marker, s=s2)
    fig.set_size_inches(4.5, 4)
    # Set Max and Min

    return fig


def RadialFullHistogram(x_ideal=0, x_meas=0, y_ideal=0, y_meas=0, title=""):
    """

    :param title:
    :param x_ideal:
    :param x_meas:
    :param y_ideal:
    :param y_meas:
    :return:
    """
    radial_error = Radial_Error(x_ideal, x_meas, y_ideal, y_meas)[0]

    # Create figure and axis
    fig, ax = plt.subplots(1, figsize=(8, 8), facecolor='#f0f0ed')
    ax.set_facecolor('#f0f0ed')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    #
    n, bins, patches = plt.hist(radial_error, bins='doane')

    minor_locator = AutoMinorLocator(2)
    plt.gca().xaxis.set_minor_locator(minor_locator)
    plt.grid(which='minor', color='#f0f0ed', lw=0.5)
    # xticks = [(bins[idx + 1] + value) / 2 for idx, value in enumerate(bins[:-1])]
    # xticks_labels = ["{:.0f}-{:.0f}".format(value, bins[idx + 1]) for idx, value in enumerate(bins[:-1])]
    # x ticks
    xticks = [(bins[idx + 1] + value) / 2 for idx, value in enumerate(bins[:-1])]
    xticks_labels = ["{:.2f}\nto\n{:.2f}".format(value, bins[idx + 1]) for idx, value in enumerate(bins[:-1])]
    plt.xticks(xticks, labels=xticks_labels)
    ax.tick_params(axis='x', which='both', length=0)
    plt.xticks(xticks, labels=xticks_labels, c='black', fontsize=13)
    ax.tick_params(axis='x', which='both', length=0)
    # Hide the right and top spines
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    for idx, value in enumerate(n):
        if value > 0:
            plt.text(xticks[idx], value + .1, int(value), ha='center', fontsize=16, c='black')
    plt.title(title, fontsize=15)
    plt.xlabel('Error (\u03BCm) ', c='black', fontsize=14)
    plt.savefig(title + "_hist.png")

    return
