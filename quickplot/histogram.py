import seaborn as sns
from matplotlib.ticker import PercentFormatter
import matplotlib.pyplot as plt
import numpy as np
from .number_formatter import usd_or_num_formatter
from .colors import *

sns.set_style("white")

def histogram(df, xvar, gpvar=None, nbins=50, xlab=None, 
              x_as_pct=False, x_as_usd=False, x_decimals=0, xticks=8, 
              color=fivethirtyeight_blue, alpha=0.4, width=10, height=4):
    """
    Plot histogram with density curve to show the distribution of a 
    continuous variable.

    Parameters
    ----------
    df : data frame
    xvar : str
        Name of a continous variable in the input data frame, to be shown on x-axis.
    gpvar : str (default = None)
        Name of a categorical variable in the input data frame, to be used as a
        grouping variable, each level will have its own histogram made in a 
        separate panel. 
    nbins : int (default = 50)
        Number of bins.
    xlab : str (default = None)
        Label of x-axis. By default, xvar is used as xlabel. To remove xlabel, 
        set `xlab=''`.
    x_as_pct : logical (default = False)
        Whether to format x-tick labels as %.
    x_as_usd : logical (default = False)
        Whether to format x-tick labels as $.
    x_decimals : int (default = 0)
        How many decimal points to show on x-tick labels.
    xticks : int  (default = 8)
        Number of x-ticks. 
    color : str (default = '#008FD5')
        Color for histogram and density curve.
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
    # draw plot using seaborn
    g = sns.displot(data=df, x=xvar, col=gpvar, bins=nbins, color=color, 
                    alpha=alpha, kde=True, rug=True)
    if xlab is None: 
        xlab = xvar    
    g.set(xlabel=xlab)
    
    # format axes
    if x_as_pct:
        for ax in g.axes.flat:
            ax.xaxis.set_major_formatter(PercentFormatter(1, decimals=x_decimals))
    if x_as_usd:
        for ax in g.axes.flat:
            ax.xaxis.set_major_formatter(usd_or_num_formatter(True, decimals=x_decimals))
    
    # show granular ticks on the axes, including the min and max values
    x = df[xvar]
    steps = (x.max() - x.min()) / xticks
    plt.xticks(np.arange(x.min(), x.max()+steps, steps))
    
    # set figure size
    fig = plt.gcf()
    fig.set_size_inches(width, height)
    
    # ensure nothing out of plotting area when saving the figure
    plt.tight_layout()