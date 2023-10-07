import numpy as np

def Msqr_HbyM(one_n, n, M, H, T, one_M_plot_final):
    """
    Calculate data for generating the Arrott plot.

    Args:
        one_n (int): Number of data points along one direction.
        n (int): Total number of data points.
        M (list): List of magnetization values.
        H (list): List of external field values.
        T (list): List of temperature values.
        one_M_plot_final (list): List of lists containing magnetization data
                                 grouped by one direction.

    Returns:
        tuple: A tuple containing three lists:
               - H_plot_final (list): List of external field values without the last one.
               - M_sqr (list): List of squared magnetization values (M^2).
               - one_H_by_M_con (list): List of lists containing H/M (applied field / magnetization)
                                        values grouped by one direction.
    """
    one_n_pop = one_n - 1
    H_plot_final = H.copy()  # Create a copy to avoid modifying the original list.
    H_plot_final.pop(one_n_pop)

    M_sqr = np.square(one_M_plot_final)
    one_H_by_M_con = []

    for j in range(0, n, 1):
        two_H_by_M_con = []
        for i in range(0, one_n - 1, 1):
            H_by_M_val = H_plot_final[i] / one_M_plot_final[j][i]
            two_H_by_M_con.append(H_by_M_val)
        one_H_by_M_con.append(two_H_by_M_con)

    return H_plot_final, M_sqr, one_H_by_M_con