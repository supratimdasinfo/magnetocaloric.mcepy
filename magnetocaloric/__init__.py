import numpy as np
import xlsxwriter
import tableprint
from random import randint
import xlrd
import matplotlib.pyplot as plt
from num2words import num2words
import sys
import itertools

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

plt.rcParams.update({'font.size':7})

def mce(n, one_n):
    
    Magnetization_val = []
    Temperature_vals = []
    External_Fields = []
    M = Magnetization_val
    T = Temperature_vals
    H = External_Fields

    print("\n    i.e. Please add one extra magnetic field (Hmax + ∆H) in your excel sheet with null \n   magnetization values (M) to get accurate output.\n\n \n\n")
    datasample = [['H0', 'M (T0,H0)', 'M (T1,H0)', '...'],['H1', 'M (T0,H1)', 'M (T1,H1)', '...'],['H2', 'M (T0,H2)', 'M (T1,H2)', '...'],['...','...','...','...']]
    tableprint.table(datasample, ['Magnetic Field (H)', 'Magnetization(M) at T0','Magnetization(M) at T1','...'])
    yesorno = input("\n    have you arranged your data in your excel sheet according to the format given above (YES/NO)?  ")
    
    if yesorno == 'YES' :
         print ("\n")
    else:
         print ("\n    please arrange your data according to the format given above.  ")
         exit()
    samp_name = input("\n    enter the sample nomenclature  : ")     
    Path_one = input("\n    enter the excel file directory of M(H) data(example : C:\File name.xlsx): ")
    path_two = input("    enter the file directory (example : C:\File name.xlsx), where the -∆Sm(T) data will be stored : ")
    path_three = input("    enter the file directory (example : C:\File name.xlsx), where the arrott plot data will be stored : ")
    
    n = int(n)
    one_n = int(one_n)
    two_n = int(n * one_n)
    print("\n\n    now, enter", num2words(n), "temperature values\n")

    for b in range(0, (n)):
         Temperature_val = input("    enter the temperature value : ")
         T.append(Temperature_val)
    plot_marker = input("\n\n    do you want to plot the figures with markers (YES/NO)?  ")     
    book = xlrd.open_workbook(Path_one)
    sheet = book.sheet_by_name('Sheet1')
    data = [[sheet.cell_value(r, c) for c in range(n+1)] for r in range(sheet.nrows)]

    for a in range(1, one_n+1, 1):          
         H.append((data[a])[0])
         for b in range(0, n):
              T.append(T[b])               
         for b in range(1, n+1):
              M.append((data[a])[b])

    three_entropy_change_con = []

    temperatures = []
    one_n_max = one_n - 2
    Multiplier = (H[one_n_max]-H[0])/10
    for q in range(0, n-1, 1):
         one_entropy_change_con = 0

         two_entropy_change_con = []

         for j,i in zip(range(0, (one_n-1), 1),range(q, two_n, n)):
              entropy_change = abs((float(M[i+1]) - float(M[i]))/(float(T[i+1]) - float(T[i]))) * (float(H[j+1]) - float(H[j]))

              one_entropy_change_con += entropy_change

              one_entropy_change_con = float(one_entropy_change_con)
              j_th_field = H[j]
              remainder = j_th_field % Multiplier
              
              if remainder == 0 :
                   two_entropy_change_con.append(one_entropy_change_con)
      
         temperatures.append(float(T[q]))
         three_entropy_change_con.append(two_entropy_change_con)

         
    Label_one = []
    for i in range(0, 11, 1):
         Label_one.append(round((i*Multiplier*((10)**(-4))),2))
         
    six_entropy_change_con = []
    six_entropy_change_con.append(temperatures)
    five_entropy_change_con = []


    for j in range(0, 11, 1):
         four_entropy_change_con = []

         for i in range(0, n-1, 1):
              four_entropy_change_con.append((10**(-4))*(three_entropy_change_con[i])[j])

         five_entropy_change_con.append(four_entropy_change_con)

         six_entropy_change_con.append(four_entropy_change_con)
         
    colour = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'tab:orange', 'tab:gray', 'tab:brown', 'tab:blue']
    marker = itertools.cycle(['^', 'o', 'v', '*', '<', 'p', '>', 'h', 'P', 'H', 'X'])    

    workbook = xlsxwriter.Workbook(path_two)
    worksheet = workbook.add_worksheet()
    row = 0
    for col, data in enumerate(six_entropy_change_con):
         worksheet.write_column(row, col, data)
    workbook.close()

    one_n_pop = one_n - 1
    one_M_plot_final = []
    H_plot_final = H
    H_plot_final.pop(one_n_pop)
    for k in range(0, n, 1):     
         one_M_plot = []
         for l in range(0, (one_n-1), 1):
              index = (((l+1)*(n - k)) + l*k) - 1
              one_M_plot.append(M[index])
         one_M_plot_final.append(one_M_plot)

    M_sqr = np.square(one_M_plot_final)
    one_H_by_M_con = []

    for j in range(0, n, 1):
        two_H_by_M_con = []
        for i in range(0, one_n-1, 1):        
            H_by_M_val = H_plot_final[i] / one_M_plot_final[j][i]
            two_H_by_M_con.append(H_by_M_val)            
        one_H_by_M_con.append(two_H_by_M_con)

    two_M_plot_final = []
    for k in range(0, (one_n - 1), 1):
         two_M_plot = []
         for l in range(k*n, ((k+1)*n)-1, 1):
              two_M_plot.append(M[l])
         two_M_plot_final.append(two_M_plot)
                   
    if plot_marker == 'YES' :

         
         for k in range (0, n, 1):
              plt.plot(H_plot_final, one_M_plot_final[k], linestyle='solid', label = T[n-(k+1)], marker = next(marker), markersize =6, linewidth=2)
         plt.legend(loc='upper left',frameon = False, ncol= 3)     
         plt.xlabel("Magnetic Field(H)", fontname = "Georgia")
         plt.ylabel("Magnetization(M)", fontname = "Georgia")
         plt.title("Magnetization vs Applied Field", fontname = "Georgia")
         
         plt.show()


         for k,l in zip(range (0, (one_n - 1), (int(one_n/10))), range(0, 11, 1)):
              plt.plot(temperatures, two_M_plot_final[k], linestyle='solid', label = Label_one[l], marker = next(marker), markersize =6, linewidth=2)
         plt.legend(loc='upper right',frameon = False, ncol= 2)     
         plt.xlabel("Temperature(T)", fontname = "Georgia")
         plt.ylabel("Magnetization(M)", fontname = "Georgia")
         plt.title("Magnetization vs Temperature", fontname = "Georgia")
         
         plt.show()


         for q in range(0, 11, 1):
              plt.plot((temperatures), (five_entropy_change_con[q]), linestyle='solid', color = colour[q], marker = next(marker), markersize =6, linewidth=2)
              plt.plot((temperatures)[0], ((five_entropy_change_con[q])[0]), linestyle='solid', label= Label_one[q], color = colour[q], marker = next(marker), markersize =6, linewidth=2)
              plt.legend(loc='upper right',frameon = False, ncol= 2)   
         plt.xlabel("Temperature(T)", fontname = "Georgia")
         plt.ylabel("-∆Sm", fontname = "Georgia")
         plt.title("-∆Sm vs Temperature", fontname = "Georgia")
         
         plt.show()
             

         for i in range (0, n, 1):
             plt.plot(one_H_by_M_con[i], M_sqr[i], linestyle='solid', label = T[n-(i+1)], marker = next(marker), markersize =6, linewidth=2)
         plt.legend(loc='upper right',frameon = False, ncol= 2)     
         plt.xlabel("H/M (Applied Field / Magnetization)", fontname = "Georgia")
         plt.ylabel("M^2 (Magnetization Square)", fontname = "Georgia")
         plt.title("M^2 vs H/M", fontname = "Georgia")
         
         plt.show()
    else:

         for k in range (0, n, 1):
              plt.plot(H_plot_final, one_M_plot_final[k], linestyle='solid', label = T[n-(k+1)], linewidth=2.5)
         plt.legend(loc='upper left',frameon = False, ncol= 3)     
         plt.xlabel("Magnetic Field(H)", fontname = "Georgia")
         plt.ylabel("Magnetization(M)", fontname = "Georgia")
         plt.title("Magnetization vs Applied Field", fontname = "Georgia")
         
         plt.show()


         for k,l in zip(range (0, (one_n - 1), (int(one_n/10))), range(0, 11, 1)):
              plt.plot(temperatures, two_M_plot_final[k], linestyle='solid', label = Label_one[l], linewidth=2.5)
         plt.legend(loc='upper right',frameon = False, ncol= 2)     
         plt.xlabel("Temperature(T)", fontname = "Georgia")
         plt.ylabel("Magnetization(M)", fontname = "Georgia")
         plt.title("Magnetization vs Temperature", fontname = "Georgia")
         
         plt.show()


         for q in range(0, 11, 1):
              plt.plot((temperatures), (five_entropy_change_con[q]), linestyle='solid', color = colour[q], linewidth=2.5)
              plt.plot((temperatures)[0], ((five_entropy_change_con[q])[0]), linestyle='solid', label= Label_one[q], color = colour[q], linewidth=2.5)
              plt.legend(loc='upper right',frameon = False, ncol= 2)   
         plt.xlabel("Temperature(T)", fontname = "Georgia")
         plt.ylabel("-∆Sm", fontname = "Georgia")
         plt.title("-∆Sm vs Temperature", fontname = "Georgia")
         
         plt.show()
             

         for i in range (0, n, 1):
             plt.plot(one_H_by_M_con[i], M_sqr[i], linestyle='solid', label = T[n-(i+1)], linewidth=2.5)
         plt.legend(loc='upper right',frameon = False, ncol= 2)     
         plt.xlabel("H/M (Applied Field / Magnetization)", fontname = "Georgia")
         plt.ylabel("M^2 (Magnetization Square)", fontname = "Georgia")
         plt.title("M^2 vs H/M", fontname = "Georgia")
         
         plt.show()           





    M_pow_MFT = np.power(one_M_plot_final, 2)
    H_by_M_pow_MFT = np.power(one_H_by_M_con, 1)

    M_pow_TMFT = np.power(one_M_plot_final, 4)
    H_by_M_pow_TMFT = np.power(one_H_by_M_con, 1)

    M_pow_3DH = np.power(one_M_plot_final, (1/0.365))
    H_by_M_pow_3DH = np.power(one_H_by_M_con, (1/1.336))

    M_pow_3DI = np.power(one_M_plot_final, (1/0.325))
    H_by_M_pow_3DI = np.power(one_H_by_M_con,(1/1.24))


    plt.subplot(2,2,1)
    for i in range (0, n, 1):
        plt.plot(H_by_M_pow_MFT[i], M_pow_MFT[i], linestyle='solid', linewidth=2)     
    plt.xlabel("(H/M)^(1/γ)", fontname = "Georgia")
    plt.ylabel("M^(1/β)", fontname = "Georgia")
    plt.title("Arrott plot 01 (β:0.5; γ:1)" , fontname = "Georgia")
    

    plt.subplot(2,2,2)
    for i in range (0, n, 1):
        plt.plot(H_by_M_pow_TMFT[i], M_pow_TMFT[i], linestyle='solid', linewidth=2)     
    plt.xlabel("(H/M)^(1/γ)", fontname = "Georgia")
    plt.ylabel("M^(1/β)", fontname = "Georgia")
    plt.title("Arrott plot 02 (β:0.25; γ:1)" , fontname = "Georgia")
    

    plt.subplot(2,2,3)
    for i in range (0, n, 1):
        plt.plot(H_by_M_pow_3DH[i], M_pow_3DH[i], linestyle='solid', linewidth=2)     
    plt.xlabel("(H/M)^(1/γ)", fontname = "Georgia")
    plt.ylabel("M^(1/β)", fontname = "Georgia")
    plt.title("Arrott plot 03 (β:0.365; γ:1.336)" , fontname = "Georgia")
    

    plt.subplot(2,2,4)
    for i in range (0, n, 1):
        plt.plot(H_by_M_pow_3DI[i], M_pow_3DI[i], linestyle='solid', linewidth=2)     
    plt.xlabel("(H/M)^(1/γ)", fontname = "Georgia")
    plt.ylabel("M^(1/β)", fontname = "Georgia")
    plt.title("Arrott plot 04 (β:0.325; γ:1.24)" , fontname = "Georgia")
    

    plt.tight_layout()
    plt.show()



    for i in range (0,2*n,1):
        lo = 2*i+1
        T.insert(lo, '   ')       
    M_sqr_vs_H_by_M = one_H_by_M_con
    M_sqr_tolist = M_sqr.tolist()

    for i in range (0,n,1):
        x_index = 2*i + 1
        M_sqr_vs_H_by_M.insert(x_index, M_sqr_tolist[i])

    for i in range (0,2*n,1):  
        M_sqr_vs_H_by_M[i].insert(0, T[i])
        M_sqr_vs_H_by_M[i].insert(1, ' ')
        if i%2 == 0 :
            M_sqr_vs_H_by_M[i].insert(2, 'H/M')
        else:
            M_sqr_vs_H_by_M[i].insert(2, 'M^2')
            
    workbook = xlsxwriter.Workbook(path_three)
    worksheet = workbook.add_worksheet()
    row = 0
    for col, data in enumerate(M_sqr_vs_H_by_M):
         worksheet.write_column(row, col, data)
    workbook.close()

    T_FWHM_con = []
    RCP_con = []
    for j in range(1, 12, 1):
        T_left = 0
        T_right = float(six_entropy_change_con[0][n-2])
        del_S_peak = np.max(six_entropy_change_con[j])
        half_max = float(del_S_peak/2)
        for i in range(0, n-2, 1):
            i_th = six_entropy_change_con[j][i]
            i_th_plus_one = six_entropy_change_con[j][i+1]
            if ((half_max >= i_th) and (half_max <= i_th_plus_one)):
                T_i_th = six_entropy_change_con[0][i]
                T_i_th_plus_one = six_entropy_change_con[0][i+1]
                del_S_dif = float(i_th_plus_one - i_th)
                T_dif = float(T_i_th_plus_one - T_i_th)
                dif_bet_ith_half = half_max - i_th
                T_left = float((T_dif/del_S_dif) * dif_bet_ith_half) + T_i_th
            elif((half_max <= i_th) and (half_max >= i_th_plus_one)):
                T_i_th = six_entropy_change_con[0][i]
                T_i_th_plus_one = six_entropy_change_con[0][i+1]
                del_S_dif = float(i_th - i_th_plus_one)
                T_dif = float(T_i_th_plus_one - T_i_th)
                dif_bet_ith_half = i_th - half_max
                T_right = float((T_dif/del_S_dif) * dif_bet_ith_half) + T_i_th

        T_FWHM = T_right - T_left
        RCP = T_FWHM * del_S_peak
        T_FWHM_con.append(float(round(T_FWHM,4)))
        RCP_con.append(float(round(RCP,4)))

    samp_name_plus_RCP = "RCP (" + samp_name + ") :: max val : " + str(np.max(RCP_con))
    samp_name_plus_T_FWHM = "T_FWHM (" + samp_name + ") :: max width : " + str(np.max(T_FWHM_con))

    fig,ax1 = plt.subplots()
    ax1.set_xlabel("Magnetic Field(H)", fontname = "Georgia")
    ax1.set_ylabel("RCP", fontname = "Georgia")
    if plot_marker == 'YES' :         

         ax1.plot(Label_one, RCP_con, linestyle='solid', marker = 'h', label = samp_name_plus_RCP, color = 'b', markersize =6, linewidth=2)
    else:
         ax1.plot(Label_one, RCP_con, linestyle='solid', label = samp_name_plus_RCP, color = 'b',linewidth=2.5) 
    ax1.legend(loc='upper left',frameon = False, ncol= 2)
    ax1.tick_params(axis='y')

    ax2 = ax1.twinx()
    ax2.set_ylabel("T_FWHM", fontname = "Georgia")
    if plot_marker == 'YES' : 
         ax2.plot(Label_one, T_FWHM_con, linestyle='solid', marker = 'H', label = samp_name_plus_T_FWHM, color = 'r', markersize =6, linewidth=2)
    else:
         ax2.plot(Label_one, T_FWHM_con, linestyle='solid', label = samp_name_plus_T_FWHM, color = 'r', linewidth=2.5) 
    ax2.legend(loc='lower right',frameon = False, ncol= 2)
    ax2.tick_params(axis='y')

    plt.title("RCP/T_FWHM vs H", fontname = "Georgia") 
    
    plt.show()
    return ("\n    check the excel spreadsheets, data has been successfully saved.")
 
