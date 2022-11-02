def usd_or_num_formatter(dollar=False, decimals=0):
    """
    Format axis tick labels as U.S. dollars or abbreviated numbers. 

    Parameters
    ----------
    dollar : logical (default=False)
        If True, will add $ in front of the numbers.
    decimals : int (default=0)
        Number of decimals to display.
        
    Returns
    -------
    Function that does the formmating.
    """
    base_fmt = '%.{}f%s'.format(decimals)
    if dollar: 
        base_fmt = '$' + base_fmt
    def human_format(num, pos): # pos is necessary as it'll be used by matplotlib
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        return base_fmt % (num, ['', 'K', 'M', 'B', 'T', 'P'][magnitude])
    return human_format
