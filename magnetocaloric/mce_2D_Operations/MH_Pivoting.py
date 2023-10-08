def MH_Pivoting(one_n, n, M, H):
    """
    Reshape the magnetization and external field data for plotting.

    Args:
        one_n (int): Number of data points along one direction.
        n (int): Total number of data points.
        M (list): List of magnetization values.
        H (list): List of external field values.

    Returns:
        tuple: A tuple containing two lists:
               - one_M_plot_final (list): A list of lists containing magnetization data,
                 grouped by one direction.
               - two_M_plot_final (list): A list of lists containing magnetization data,
                 grouped by the other direction.
    """
    # Reshape the data for one direction (H/M data grouped by the other direction).
    one_M_plot_final = []
    for k in range(0, n, 1):
        one_M_plot = []
        for l in range(0, (one_n - 1), 1):
            index = (((l + 1) * (n - k)) + l * k) - 1
            one_M_plot.append(M[index])
        one_M_plot_final.append(one_M_plot)

    # Reshape the data for the other direction (H/M data grouped by one direction).
    two_M_plot_final = []
    for k in range(0, (one_n - 1), 1):
        two_M_plot = []
        for l in range(k * n, ((k + 1) * n) - 1, 1):
            two_M_plot.append(M[l])
        two_M_plot_final.append(two_M_plot)

    return one_M_plot_final, two_M_plot_final