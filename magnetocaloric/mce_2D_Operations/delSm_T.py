import numpy as np
def delSm_T(n, one_n, two_n, H, M, T):
    """
    Calculate entropy changes for different temperatures and magnetic fields.

    Parameters:
        n (int): Number of temperature values.
        one_n (int): Total number of data samples per magnetic field.
        two_n (int): Total number of data samples for all magnetic fields.
        H (list): List of external magnetic field values.
        M (list): List of magnetization values.
        T (list): List of temperature values.

    Returns:
        three_entropy_change_con (list): A list of lists containing the calculated entropy changes.
        temperatures (list): A list of temperature values used for calculating the entropy changes.
        Label_one (list): A list of magnetic field values (in Tesla * 10^-4) for which entropy changes were calculated.
    """
    # Initialize variables to store entropy changes and temperatures
    three_entropy_change_con = []
    temperatures = []

    # Calculate the multiplier for magnetic field values
    one_n_max = one_n - 2
    #Multiplier = (H[one_n_max] - H[0]) / 10
    
    # Loop through temperature values to calculate entropy changes
    for q in range(0, n - 1, 1):
        one_entropy_change_con = 0
        two_entropy_change_con = []
        Label_one = []

        # Calculate entropy change for each data point in the one_n-1 range
        for j, i in zip(range(0, (one_n - 1), 1), range(q, two_n, n)):
            entropy_change = ((float(M[i + 1]) - float(M[i])) / (float(T[i + 1]) - float(T[i]))) * abs(float(H[j + 1]) - float(H[j]))

            one_entropy_change_con += entropy_change
            one_entropy_change_con = float(one_entropy_change_con)

            #j_th_field = H[j]
            #remainder = j_th_field % Multiplier

            let = one_n - 1
            div = 15
            if one_n < 16 :
                print ("</> there is not enough Magnetic Field data available")
            else:
                pass
            let_by = int(let/div)
            if (j % let_by == 0) or (j == one_n - 2):
                two_entropy_change_con.append(one_entropy_change_con)
                Label_one.append(round((H[j]), 2))

        # Store calculated entropy changes and temperature values for each iteration
        temperatures.append(float(T[q]))
        three_entropy_change_con.append(two_entropy_change_con)

    # Return the final calculated entropy changes, temperature values, and magnetic field labels
    return three_entropy_change_con, temperatures, Label_one