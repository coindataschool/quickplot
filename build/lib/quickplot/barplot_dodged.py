import seaborn as sns
from matplotlib.ticker import PercentFormatter
import matplotlib.pyplot as plt
import numpy as np
from .number_formatter import usd_or_num_formatter
from .colors import *

sns.set_style("white")

def dodged_barplot(df, xvar, yvar, gpvar=None, title=None, xlab=None, ylab=None, 
                   y_as_pct=False, y_as_usd=False, y_decimals=0, yticks=8,
                   alpha=0.8, width=10, height=4, bar_label_decimals=0, ):
    """
    Plot dodged bar charts.

    Parameters
    ----------
    df : data frame
    xvar : str
        Name of a categorical variable in the input data frame, to be shown on x-axis.
    yvar : str
        Name of a continuous variable in the input data frame, to be shown on y-axis.
    gpvar : str (default = None)
        Name of a categorical variable in the input data frame, to be used as the
        grouping variable for dodged bars. 
    title, xlab, ylab : str (default = None)
        Figure title, x-label and y-label. By default, we use xvar as xlabel and 
        yvar as ylabel. To remove xlabel or ylabel, set `xlab=''` or `ylab=''`.
    y_as_pct : logical (default = False)
        Whether to format y-tick labels as %.
    y_as_usd : logical (default = False)
        Whether to format y-tick labels as $.
    y_decimals : int (default = 0)
        How many decimal points to show on y-tick labels.
    yticks : int  (default = 8)
        Number of y-ticks. 
    alpha : float (default = 0.7)
        Color transparency.
    width : float (default = 10)
        Figure width (in inches).
    height : float (default = 4)
        Figure height (in inches).
    bar_label_decimals : int (default = 0)
        Number of decimals to show on bar labels.

    Returns
    -------
    None. Display the plot as side effect.
    """
    # draw plot using seaborn 
    g = sns.catplot(data=df, x=xvar, y=yvar, hue=gpvar, kind='bar', alpha=alpha,
        legend_out=False)
    if xlab is None: 
        xlab = xvar    
    if ylab is None:
        ylab = yvar
    g.set(title=title, xlabel=xlab, ylabel=ylab)

    for ax in g.axes.flat:
        # format axes
        if y_as_usd:
            ax.yaxis.set_major_formatter(usd_or_num_formatter(True, decimals=y_decimals))
            bar_label_fmt = "${:." + str(bar_label_decimals) + "f}" 
        elif y_as_pct:
            ax.yaxis.set_major_formatter(PercentFormatter(1, decimals=y_decimals))
            bar_label_fmt = "{:." + str(bar_label_decimals) + "%}"
        else: 
            bar_label_fmt = "{:." + str(bar_label_decimals) + "f}" 
        # add bar labels
        for p in ax.patches:
            xpos = p.get_x() + p.get_width()/2
            ypos = p.get_height()
            if ypos > 0:
                ax.annotate(bar_label_fmt.format(p.get_height()), 
                            xy=(xpos, ypos), va='bottom', ha='center')
            else: 
                ax.annotate(bar_label_fmt.format(p.get_height()), 
                            xy=(xpos, ypos), va='top', ha='center')

    # show granular ticks on the axes, including the min and max values
    # only do this if y values are floats, don't do it for ints (count data)
    if df[yvar].dtypes == float:
        y = np.append(df[yvar].values, 0)
        steps = (y.max() - y.min()) / yticks
        plt.yticks(np.arange(y.min(), y.max()+steps, steps))

    # set figure size
    fig = plt.gcf()
    fig.set_size_inches(width, height)
    
    # ensure nothing out of plotting area when saving the figure
    plt.tight_layout()