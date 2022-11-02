import seaborn as sns
from matplotlib.ticker import PercentFormatter
import matplotlib.pyplot as plt
import numpy as np
from .number_formatter import usd_or_num_formatter

sns.set_style("white")

def mk_histogram(df, xvar, gpvar=None, nbins=50, title=None, xlab=None, 
                 x_as_pct=False, x_as_usd=False, x_decimals=0, xticks=8):
    """Plot histogram with density curve to show the distribution of a 
    continuous variable.

    Parameters
    ----------
    df : data frame
    xvar : str
        Name of a continous variable in the input data frame.
    gpvar : str (default = None)
        Name of a categorical variable in the input data frame.
    nbins : int (default = 50)
        Number of bins.
    title, xlab : str (default = None)
        Figure title and x label.
    x_as_pct : logical (default = False)
        Whether to format x-tick labels as %.
    x_as_usd : logical (default = False)
        Whether to format x-tick labels as $.
    x_decimals : int (default = 0)
        How many decimal points to show on x-tick labels.
    xticks : int  (default = 8)
        Number of x-ticks. 

    Returns
    -------
    None. Display the plot as side effect.    
    """
    # draw plot using seaborn, annotate, and format axes
    g = sns.displot(data=df, x=xvar, col=gpvar, bins=nbins, kde=True, rug=True)
    if title is not None:
        g.set(title=title)
    if xlab is not None: 
        g.set(xlabel=xlab)
    if x_as_pct:
        for ax in g.axes.flat:
            ax.xaxis.set_major_formatter(PercentFormatter(1, decimals=x_decimals))
    if x_as_usd:
        for ax in g.axes.flat:
            ax.xaxis.set_major_formatter(usd_or_num_formatter(True, decimals=x_decimals))
    # show granular ticks on the axes, including the min and max values
    x = df[xvar]
    steps = (max(x) - min(x)) / xticks
    plt.xticks(np.arange(min(x), max(x)+steps, steps))