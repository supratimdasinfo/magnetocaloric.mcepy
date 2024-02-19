import numpy as np

def n_expo(n, one_n, two_n, H, M, T):

    '''
        Parameters:
            n (int): Number of temperature values.
            one_n (int): Total number of data samples per magnetic field.
            two_n (int): Total number of data samples for all magnetic fields.
            H (list): List of external magnetic field values.
            M (list): List of magnetization values.
            T (list): List of temperature values.
    '''

    H_arr = H
    T_arr = [] 
    M_arr = []
    er_init = 0
    er_final = n
    for i in range(0, one_n):
            M_arr_prov = []
            for j in range (er_init, er_final):
                    M_arr_prov.append(M[j])
            M_arr.append(M_arr_prov)
            er_init += n
            er_final += n
    for i in range (0, n):
            T_arr.append(T[i])


    entropy_change_con = []
    sum_array = np.zeros(n-1)
    for i in range (0, one_n-1):
            entropy_change_con_prov = []
            for j in range (0, n-1):
                    entropy_change = ((float(M_arr[i][j + 1]) - float(M_arr[i][j])) / (float(T_arr[j + 1]) - float(T_arr[j]))) * abs(float(H_arr[i+1]) - float(H_arr[i])) 

                    entropy_change_con_prov.append(entropy_change)
            sum_array += np.asarray(entropy_change_con_prov)
            sum_list = sum_array.tolist()
            entropy_change_con.append(sum_list)
                    

    N_expo_con = []
    count = 0
    N_H_label = []
    for i in range (0, one_n-2):
            N_expo_con_prov = []
            for j in range (0, n-1):
                    N_expo =  (np.log(abs(float(entropy_change_con[i+1][j]))) - np.log(abs(float(entropy_change_con[i][j]))))/ (np.log(abs(float(H_arr[i+1]))) - np.log(abs(float(H_arr[i]))))
                    N_expo_con_prov.append(N_expo)


            let = one_n - 1
            div = 15
            if one_n < 16 :
                print ("</> there is not enough Magnetic Field data available")
            else:
                pass
            let_by = int(let/div)

            if (i % let_by == 0) or (i == one_n - 3):
                    N_expo_con.append(N_expo_con_prov)
                    count +=1
                    N_H_label.append(round(H_arr[i], 2))

    T_arr.pop()

    return N_expo_con, T_arr, H_arr, N_H_label
 







                


