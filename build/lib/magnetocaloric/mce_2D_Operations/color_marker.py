import itertools

def color_marker():
    """
    Generate lists of colors and markers for plotting purposes.

    Returns:
        colour (list): List of color strings representing different colors for plots.
        marker (itertools.cycle): An iterator that cycles through different marker symbols for plots.
    """
    colour = itertools.cycle(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'tab:orange', 'tab:gray', 'tab:brown', 'tab:blue'])
    marker = itertools.cycle(['^', 'o', 'v', '*', '<', 'p', '>', 'h', 'P', 'H', 'X'])

    print ("</> colors and markers are generated  -----> using itertools.cycle() for [colour] and [marker]")
    return colour, marker