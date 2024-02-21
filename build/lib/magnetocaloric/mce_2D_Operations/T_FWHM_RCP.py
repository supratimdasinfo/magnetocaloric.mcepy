import numpy as np

def T_FWHM_RCP(n, Label_one, six_entropy_change_con):
    """
    Calculate Full Width at Half Maximum (FWHM) and Relative Cooling Power (RCP) from entropy data.

    Args:
        n (int): Number of data points.
        Label_one (list): List of temperature values.
        six_entropy_change_con (list): List of lists containing entropy change data.

    Returns:
        tuple: A tuple containing four lists: 
               1. T_FWHM_con: List of calculated FWHM values.
               2. RCP_con: List of calculated RCP values.
               3. RCP_final: List of RCP values with sufficient data.
               4. H_for_RCP: List of H values corresponding to RCP.
    """
    T_FWHM_con = []
    RCP_con = []
    RCP_error = []
    RCP_final = []
    T_FWHM_con_final = []
    H_for_RCP = []

    # Iterate through each temperature data.
    for j in range(1, len(Label_one) + 1):
        del_S_peak = np.min(six_entropy_change_con[j])

        # Find the index of the maximum entropy change value.
        for k in range(n - 1):
            if six_entropy_change_con[j][k] == del_S_peak:
                kth_index = k
                max_entropy_at_T = six_entropy_change_con[0][kth_index]

        half_max = del_S_peak / 2
        half_max_entropy_at_T_con = [six_entropy_change_con[0][0]]

        # Find the temperatures where the entropy change is approximately half of the maximum value.
        for i in range(n - 2):
            i_th = six_entropy_change_con[j][i]
            i_th_plus_one = six_entropy_change_con[j][i + 1]
            if (i_th_plus_one >= half_max >= i_th) or (i_th_plus_one <= half_max <= i_th):
                T_i_th = six_entropy_change_con[0][i]
                T_i_th_plus_one = six_entropy_change_con[0][i + 1]
                del_S_dif = abs(i_th_plus_one - i_th)
                T_dif = T_i_th_plus_one - T_i_th
                dif_bet_ith_half = abs(half_max - i_th)
                half_max_entropy_at_T = (T_dif / del_S_dif) * dif_bet_ith_half + T_i_th
                half_max_entropy_at_T_con.append(abs(half_max_entropy_at_T))
        half_max_entropy_at_T_con.append(six_entropy_change_con[0][n - 2])

        # Find the temperature range for FWHM
        for l in range(len(half_max_entropy_at_T_con) - 1):
            l_th = half_max_entropy_at_T_con[l]
            l_th_plus_one = half_max_entropy_at_T_con[l + 1]
            if l_th <= max_entropy_at_T and l_th_plus_one >= max_entropy_at_T:
                T_left = l_th
                T_right = l_th_plus_one

        T_FWHM = T_right - T_left
        RCP = abs(T_FWHM) * abs(del_S_peak)
        T_FWHM_con.append(round(T_FWHM, 4))
        RCP_con.append(round(RCP, 4))

        # Detect insufficient data for RCP calculation.
        if (T_left == six_entropy_change_con[0][0] != 0.0) or (T_right == six_entropy_change_con[0][n - 2]):
            RCP_error.append(Label_one[j - 1])
        else:
            T_FWHM_con_final.append(T_FWHM)
            RCP_final.append(round(RCP, 4))
            H_for_RCP.append(Label_one[j - 1])

    lst_RCP_error = len(RCP_error) - 1

    if len(RCP_error) == 1:
        print("</> insufficient data ----> error detected while calculating RCP at H : {} T".format(RCP_error[0]))
    elif len(RCP_error) >= 1:
        print("</> insufficient data ----> error detected while calculating RCP from H : {} T to H : {} T".format(RCP_error[0], RCP_error[lst_RCP_error]))
    else:
        print('')

    return T_FWHM_con, T_FWHM_con_final, RCP_con, RCP_final, H_for_RCP