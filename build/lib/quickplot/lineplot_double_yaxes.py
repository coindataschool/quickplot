import seaborn as sns
from matplotlib.ticker import PercentFormatter
import matplotlib.pyplot as plt
import numpy as np
from .number_formatter import usd_or_num_formatter
from .colors import *

sns.set_style("white")

def lineplot_dual_yaxes(
    df, left_yvar, right_yvar, title=None, xlab=None, left_ylab=None, right_ylab=None, 
    left_y_as_pct=False, left_y_as_usd=False, right_y_as_pct=False, right_y_as_usd=False,  
    left_y_decimals=0, right_y_decimals=0, left_yticks=8, right_yticks=8,
    alpha=0.4, width=10, height=4):
    """
    Plot line plot with left and right y-axes to show two time series of 
    different scales over time.

    Parameters
    ----------
    df : data frame
    left_yvar : str
        Name of a continous variable in the input data frame, to be shown on 
        the left y-axis.
    right_yvar : str 
        Name of another continuous variable in the input data frame, to be
        shown on the right y-axis. 
    title : str (default = None)
        Figure title. 
    xlab : str (default = None)
        Label of x-axis. By default, index name of the input frame is used.
        Index should be datetime. To remove xlabel, set `xlab=''`.
    left_ylab : str (default = None)
        Label of left y-axis. By default, left_yvar is used. To remove left 
        ylabel, set `left_ylab=''`.
    right_ylab : str (default = None)
        Label of right y-axis. By default, right_yvar is used. To remove right
        ylabel, set `right_ylab=''`.
    left_y_as_pct : logical (default = False)
        Whether to format the left y-tick labels as %.
    left_y_as_usd : logical (default = False)
        Whether to format the left y-tick labels as $.
    right_y_as_pct : logical (default = False)
        Whether to format the right y-tick labels as %.
    right_y_as_usd : logical (default = False)
        Whether to format the right y-tick labels as $.
    left_y_decimals : int (default = 0)
        How many decimal points to show on left y-tick labels.
    right_y_decimals : int (default = 0)
        How many decimal points to show on right y-tick labels.
    left_yticks : int (default = 8)
        Number of left y-ticks. 
    right_yticks : int (default = 8)
        Number of right y-ticks. 
    alpha : float (default = 0.4)
        Color transparency.
    width : float (default = 10)
        Figure width (in inches).
    height : float (default = 4)
        Figure height (in inches).

    Returns
    -------
    None. Display the plot as side effect.    
    """
    if xlab is None: xlab = df.index.name
    if left_ylab is None: left_ylab = left_yvar
    if right_ylab is None: right_ylab = right_yvar

    # left y
    ax1 = df[left_yvar].plot()
    for tl in ax1.get_yticklabels():
        tl.set_color(fivethirtyeight_blue)
    ax1.set_ylabel(left_ylab, color=fivethirtyeight_blue)

    # right y
    ax2 = ax1.twinx()
    ax2.plot(df.index, df[right_yvar], color=fivethirtyeight_green)
    for tl in ax2.get_yticklabels():
        tl.set_color(fivethirtyeight_green)
    ax2.set_ylabel(right_ylab, color=fivethirtyeight_green)

    # format y-axes
    if left_y_as_pct:
        ax1.yaxis.set_major_formatter(PercentFormatter(decimals=left_y_decimals))
    if right_y_as_pct:
        ax2.yaxis.set_major_formatter(PercentFormatter(decimals=right_y_decimals))
    if left_y_as_usd:
        ax1.yaxis.set_major_formatter(
            usd_or_num_formatter(True, decimals=left_y_decimals))
    if right_y_as_usd:
        ax2.yaxis.set_major_formatter(
            usd_or_num_formatter(True, decimals=right_y_decimals))
    
    # # show granular ticks on the y-axes, including the min and max values
    # left_y = df[left_yvar]
    # steps = (left_y.max() - left_y.min()) / left_yticks
    # ax1.yticks(np.arange(left_y.min(), left_y.max()+steps, steps))
    # right_y = df[right_yvar]
    # steps = (right_y.max() - right_y.min()) / right_yticks
    # ax2.yticks(np.arange(right_y.min(), right_y.max()+steps, steps))
    
    # add title
    plt.title(title)

    # set figure size
    fig = plt.gcf()
    fig.set_size_inches(width, height)
    
    # ensure nothing out of plotting area when saving the figure
    plt.tight_layout()