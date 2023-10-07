import numpy as np
import matplotlib.pyplot as plt
import itertools

def data_plotting(g_name, one_n, n, T, H, M_unit, H_unit, T_unit, colour, marker, Label_one, plot_legend, loc, one_M_plot_final, two_M_plot_final, H_plot_final, temperatures, five_entropy_change_con, M_sqr, one_H_by_M_con, N_expo_con, T_arr, N_H_label, T_sus, sus_inv, sus, np_T_sus, regression_line, np_T_sus_bu, regression_bu, x, linear_threshold, T_FWHM_con, T_FWHM_con_final, RCP_con, RCP_final, H_for_RCP, samp_name):
    """
    Visualize the data using Matplotlib.

    Args:
        one_n (int): Number of data points along one direction.
        n (int): Total number of data points.
        T (list): List of temperature values.
        H (list): List of external field values.
        colour (list): List of color strings for plotting.
        marker (itertools.cycle): Iterator over marker symbols for plotting.
        Label_one (list): List of labels for the legend.
        plot_legend (str): Flag to indicate whether to show legends in the plots ('YES' or 'NO').
        one_M_plot_final (list): List of lists containing magnetization data grouped by one direction.
        two_M_plot_final (list): List of lists containing magnetization data grouped by two directions.
        H_plot_final (list): List of external field values without the last one.
        temperatures (list): List of temperature values for plotting.
        five_entropy_change_con (list): List of lists containing entropy change data.
        M_sqr (list): List of squared magnetization values (M^2).
        one_H_by_M_con (list): List of lists containing H/M (applied field / magnetization) data.

    Returns:
        None: The function displays plots based on the data.
    """

    if (g_name== 'MH_plot' or g_name== 'all_plots'):

        if plot_legend == 'Yes':        
            # Plotting magnetization vs. applied field for each temperature.
            for k in range(n):
                plt.plot(H_plot_final, one_M_plot_final[k], linestyle='solid', label=T[n - (k + 1)], marker=next(marker), markersize =5, linewidth= 0.5)
            plt.legend(loc=str(loc), frameon=False, ncol=3)
            plt.xlabel(f"Magnetic Field (H) {H_unit}")
            plt.ylabel(f"Magnetization (M) {M_unit}")
            plt.title("Field depedence of Magnetization")
            plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
            plt.show()

        else:
            for k in range (0, n, 1):
              plt.plot(H_plot_final, one_M_plot_final[k], linestyle='solid', label = T[n-(k+1)], marker = next(marker), markersize =5, linewidth= 0.5)
             
            plt.xlabel(f"Magnetic Field (H) {H_unit}")
            plt.ylabel(f"Magnetization (M) {M_unit}")
            plt.title("Field depedence of Magnetization", fontname = "monospace")

            plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
            plt.show()
        print ("</> request for MH_plot ----> accepted & generated using [H_plot_final] & [one_M_plot_final]")

    if (g_name== 'MT_plot' or g_name== 'all_plots'):
        
        if plot_legend == 'Yes':
            # Plotting magnetization vs. temperature for selected external field values.
            for k in range(0, one_n - 1, int(one_n / 10)):
                plt.plot(temperatures, two_M_plot_final[k], linestyle='solid', label=(round((H[k] * (10 ** (-4))), 1)), marker=next(marker), markersize =5, linewidth= 0.5)
            plt.legend(loc=str(loc), frameon=False, ncol=2)
            plt.xlabel(f"Temperature ({T_unit})")
            plt.ylabel(f"Magnetization (M) {M_unit}")
            plt.title("Temperature depedence of Magnetization")
            plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
            plt.show()
        else:
            for k in range (0, (one_n - 1), (int(one_n/10))):
              plt.plot(temperatures, two_M_plot_final[k], linestyle='solid', label = (round((H[k]*(10**(-4))),1)), marker = next(marker), markersize =5, linewidth= 0.5)
              
            plt.xlabel(f"Temperature ({T_unit})")
            plt.ylabel(f"Magnetization (M) {M_unit}")
            plt.title("Temperature depedence of Magnetization", fontname = "monospace")

            plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
            plt.show()

        print ("</> request for MT_plot ----> accepted & generated using [temperatures] & [two_M_plot_final]")

    if (g_name== 'dSmT_plot' or g_name== 'all_plots'):

        if plot_legend == 'Yes':        
            # Plotting entropy change vs. temperature for each temperature.
            for q in range(0, len(Label_one)):
                plt.plot(temperatures, five_entropy_change_con[q], linestyle='solid', label=Label_one[q], color= next(colour), marker=next(marker), markersize =5, linewidth= 0.5)
                plt.legend(loc=str(loc), frameon=False, ncol=2)
            plt.xlabel(f"Temperature ({T_unit})")
            plt.ylabel(f"-∆Sm ({M_unit}).{H_unit}/{T_unit}")
            plt.title("Temperature depedence of Entropy change")
            plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
            plt.show()
        else:
            for q in range(0, len(Label_one), 1):
              plt.plot((temperatures), (five_entropy_change_con[q]), linestyle='solid', color= next(colour), marker = next(marker), markersize =5, linewidth= 0.5)
                              
            plt.xlabel(f"Temperature ({T_unit})", fontname = "monospace")
            plt.ylabel(f"-∆Sm ({M_unit}).{H_unit}/{T_unit}", fontname = "monospace")
            plt.title("Temperature depedence of Entropy change", fontname = "monospace")

            plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
            plt.show() 

        print ("</> request for dSmT_plot ----> accepted & generated using [temperatures] & [five_entropy_change_con]")           

    if (g_name== 'N_plot' or g_name== 'all_plots'):
        if plot_legend == 'Yes':        

            for i in range (0, len(N_expo_con)):            
                    plt.plot(T_arr, N_expo_con[i], linestyle='solid', label=N_H_label[i], color= next(colour), marker=next(marker), markersize =5, linewidth= 0.5)
                    plt.legend(loc=str(loc), frameon=False, ncol=2)
            plt.xlabel(f"Temperature ({T_unit})")
            plt.ylabel(f"N exponent ", fontsize= 8)
            plt.title("Temperature depedence of N exponent")
            plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
            plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
            plt.show()

        else:
            for i in range (0, count):            
                    plt.plot(T_arr, N_expo_con[i], linestyle='solid', label=N_H_label[i], color= next(colour), marker=next(marker), markersize =5, linewidth= 0.5)
                    
            plt.xlabel(f"Temperature ({T_unit})")
            plt.ylabel(f"N exponent")
            plt.title("Temperature depedence of N exponent")
            plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
            plt.show()
        print ("</> request for N_plot ----> accepted & generated using [T_arr] & [N_expo_con]")

    if (g_name== 'MFT_plot' or g_name== 'all_plots'):

        if plot_legend == 'Yes':
            # Plotting M^2 vs. H/M for each temperature.
            for i in range(n):
                plt.plot(one_H_by_M_con[i], M_sqr[i], linestyle='solid', label=T[n - (i + 1)], marker=next(marker), markersize =5, linewidth= 0.5)
            plt.legend(loc=str(loc), frameon=False, ncol=2)
            plt.xlabel(f"H/M (Applied Field / Magnetization) {H_unit}/({M_unit})")
            plt.ylabel(f"M^2 (Magnetization Square) {M_unit}^2")
            plt.title("Mean Field Model")
            plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
            plt.show()
        else:
            for i in range (0, n, 1):
             plt.plot(one_H_by_M_con[i], M_sqr[i], linestyle='solid', label = T[n-(i+1)], marker = next(marker), markersize =5, linewidth= 0.5)

            plt.xlabel(f"H/M (Applied Field / Magnetization) {H_unit}/({M_unit})", fontname = "monospace")
            plt.ylabel(f"M^2 (Magnetization Square) {M_unit}^2", fontname = "monospace")
            plt.title("Mean Field Model", fontname = "monospace")

            plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
            plt.show()
        print ("</> request for MFT_plot ----> accepted & generated using [one_H_by_M_con] & [M_sqr]")

    if (g_name== 'sus_plot' or g_name== 'all_plots'):

        label01 = f"1/Chi (inverse susceptibility)"
        label02 = f"Chi (susceptibility)"
        label03 = f"Regression (x= {str(round(x, 2))}, y=0)"
        label04 = f"1/Chi associated with Regression"
        


                    
        fig, ax1 = plt.subplots()
        ax1.set_xlabel(f"Temperature (T) {T_unit}")
        ax1.set_ylabel(f"1/Chi {H_unit}/({M_unit})")
        ax1.plot(T_sus, sus_inv, linestyle='solid', marker='o',label=label01, markerfacecolor='none', color='black',markersize=5, linewidth=0.5)
        if linear_threshold == 0.0 or linear_threshold == 'None':
            pass
        else:
            ax1.plot(np_T_sus, regression_line, linestyle= 'dashed', color='black', label=label03, linewidth=0.7)
            ax1.plot(np_T_sus_bu, regression_bu, linestyle='none', marker='o', markerfacecolor='green', label=label04, color='black',markersize=5, linewidth=0.5)
        ax1.tick_params(axis='y')

        ax2 = ax1.twinx()
        ax2.set_ylabel(f"Chi ({M_unit})/{H_unit}")
        ax2.plot(T_sus, sus, linestyle='solid', marker='o', label=label02, color='r', markersize=5, linewidth=0.5)
        ax2.tick_params(axis='y')

        # Adjust legend positioning


        # Use the bbox_to_anchor parameter to position the legends
        fig.legend(loc= "upper center", frameon=False, ncol=2)
        plt.title(f"Temperature depedence of Susceptibility and Inverse Susceptibility")
        plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
        plt.show()

        print ("</> request for sus_plot ----> accepted & generated ")

    """
    Plot Relative Cooling Power (RCP) and Full Width at Half Maximum (T_FWHM) against magnetic field (H).

    Args:
        T_FWHM_con (list): List of calculated FWHM values.
        Label_one (list): List of temperature values.
        RCP_con (list): List of calculated RCP values for all temperatures.
        RCP_final (list): List of RCP values with sufficient data.
        H_for_RCP (list): List of magnetic field values corresponding to RCP.
        samp_name (str): Name of the sample.

    Returns:
        None: The function only plots the RCP/T_FWHM vs H graphs.
    """
    if (g_name== 'RCP_plot' or g_name== 'all_plots'):
        samp_name_plus_RCP = "RCP (" + samp_name + ") :: max val : " + str(np.max(RCP_con)) + "(" + str(M_unit) + ")." + str(H_unit)
        samp_name_plus_T_FWHM = "T_FWHM (" + samp_name + ") :: max width : " + str(np.max(T_FWHM_con)) + str(T_unit)

        if len(RCP_final) >= 2:
            fig, ax1 = plt.subplots()
            ax1.set_xlabel(f"Magnetic Field(H) {H_unit}")
            ax1.set_ylabel(f"RCP ({M_unit}).{H_unit}")
            ax1.plot(H_for_RCP, RCP_final, linestyle='solid', marker='o', label=samp_name_plus_RCP, color='r', markersize=5, linewidth=0.5)
            ax1.legend(loc='upper left', frameon=False, ncol=2)
            ax1.tick_params(axis='y')

            ax2 = ax1.twinx()
            ax2.set_ylabel(f"T_FWHM ({T_unit})")
            ax2.plot(H_for_RCP, T_FWHM_con_final, linestyle='-', marker='+', label=samp_name_plus_T_FWHM, color='black', markersize=7, linewidth=0.0)
            ax2.legend(loc='lower right', frameon=False, ncol=2)
            ax2.tick_params(axis='y')

            plt.title("Field depedence of RCP/T_FWHM")
            plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
            plt.show()
            print ("</> request for RCP_plot ----> accepted & generated ")
        else:
            print ("</> request for RCP_plot ----> denied for insufficient data ")

    return
