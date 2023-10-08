import xlrd
import math
import xlsxwriter
import numpy as np
import matplotlib.pyplot as plt


def interpol(path, sheet_index, T_row, H_col, int_val, final_val, interval, interpol_type, interpolation, deg):

    def column_letter_to_number(column_letter):
        column_number = 0
        for char in column_letter:
            # Convert the character to its ASCII value and subtract 64
            # to get the 1-based index (A=1, B=2, ..., Z=26)
            column_number = column_number * 26 + (ord(char.upper()) - 64)
        return column_number


    # Open the Excel workbook
    workbook = xlrd.open_workbook(path)
    sheet = workbook.sheet_by_index(sheet_index-1)

    n_rows = sheet.nrows
    n_cols = sheet.ncols

    prov_data = []

    prov_T = []
    # Extract temperature values from the first row
    for i in range(n_cols):
        prov_T.append(sheet.cell_value((int(T_row)-1), i))

    # Extract data from the Excel sheet
    for i in range(n_cols):
        col_data = []
        for j in range(1, n_rows):
            col_data.append(sheet.cell_value(j, i))

        prov_data.append(col_data)

    H_col_num = column_letter_to_number(H_col)


    prov_H = prov_data.pop(int(H_col_num) -1)


    # Define a function to check if the last element of a list is a string
    def check_last_element(prov_data):
        last_element = prov_data[0][-1]
        if isinstance(last_element, str):
            return True
        else:
            return False

    # If the last element of prov_data is a string, remove it from each list
    if check_last_element(prov_data):
        for i in range(0, len(prov_data)):
            prov_data[i].pop(len(prov_data[i]) - 1)
        prov_H.pop(len(prov_H) - 1)
    else:
        pass

    H_num = int(((final_val - int_val)/interval) + 1)	
    H_np = np.linspace(int(int_val), int(final_val), H_num) 
    H = H_np.tolist() 

    if (interpol_type == 'poly'):
        best_degree_con = []
        # Define a range of polynomial degrees to test
        if (interpolation == 'auto'):
            degrees_to_test = range(1, 50)  # Test degrees from 1 to 49   
            se_con_final = [] 
            for i in range(0, len(prov_data)):
                best_degree = 1
                best_mse = np.inf
                for degree in degrees_to_test:
                    
                    coef = np.polyfit(prov_H, prov_data[i], degree)
                    poly1d_fn = np.poly1d(coef)

                    # Calculate the predicted values
                    prov_data_pred = poly1d_fn(H)
                    prov_data_intt = np.interp(H, prov_H, prov_data[i])
                    # Calculate the Mean Squared Error (MSE)
                    mse = np.mean((prov_data_intt - prov_data_pred) ** 2)
                    se_con = ((prov_data_intt - prov_data_pred) ** 2)


                    # Check if this degree has a lower MSE
                    if mse < best_mse:
                        best_mse = mse
                        best_degree = degree
                #se_con_final.append(se_con)        
                best_degree_con.append(best_degree)
        else:
            for i in range(0, len(prov_data)):
                best_degree = deg
                best_degree_con.append(best_degree)
        # Fit the best degree polynomial to the data
        M_fitted_con = []
        se_con_final = [] 

        for i in range(0, len(prov_data)):

            best_coef = np.polyfit(prov_H, prov_data[i], best_degree_con[i])
            prov_data_fn = np.poly1d(best_coef)
            M_fitted = prov_data_fn(H)
            prov_data_intt = np.interp(H, prov_H, prov_data[i])
            # Calculate the Mean Squared Error (MSE)
            mse = np.mean((prov_data_intt - M_fitted) ** 2)
            se_con = ((prov_data_intt - M_fitted) ** 2)
            se_con_final.append(se_con)
            M_fitted = M_fitted.tolist()
            M_fitted_con.append(M_fitted)
        total_interp_M_con = M_fitted_con

        plt.pcolor(se_con_final, cmap='terrain')

        # Add colorbar with a custom label
        cbar = plt.colorbar(orientation='horizontal')
        cbar.set_label('Square Error', fontname='monospace')

        # Set labels for the X and Y axes with monospace font
        plt.xlabel('x-axis (sheet_col)', fontname='monospace')
        plt.ylabel('y-axis (sheet_row)', fontname='monospace')

        # Show the plot
        plt.show()


    elif (interpol_type == 'lin'):    
        total_interp_M_con = []
        se_con_final = [] 
        for m in range(0, len(prov_data)):
            interp_M_con = np.interp(H, prov_H, prov_data[m])
            prov_data_intt = np.interp(H, prov_H, prov_data[m])
            # Calculate the Mean Squared Error (MSE)
            mse = np.mean((prov_data_intt - interp_M_con ) ** 2)
            se_con = ((prov_data_intt - interp_M_con) ** 2)
            se_con_final.append(se_con)
            interp_M_con_list = interp_M_con.tolist()
            total_interp_M_con.append(interp_M_con_list)

        plt.pcolor(se_con_final, cmap='terrain')

        # Add colorbar with a custom label
        cbar = plt.colorbar(orientation='horizontal')
        cbar.set_label('Square Error', fontname='monospace')

        # Set labels for the X and Y axes with monospace font
        plt.xlabel('x-axis (sheet_col)', fontname='monospace')
        plt.ylabel('y-axis (sheet_row)', fontname='monospace')

        # Show the plot
        plt.show()

    else :
        print ("</> invalid 'interpol_type', choose either 'lin' or 'poly' ")


	
    total_interp_M_con.insert(0, H)

    for i in range(0, len(prov_T)):
        total_interp_M_con[i].insert(0, prov_T[i])

    final_data = total_interp_M_con
    # Write the interpolated data to a new Excel file
    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet()

    for col, col_data in enumerate(final_data):
        for row, value in enumerate(col_data):
            worksheet.write(row, col, value)
    workbook.close()

    print ("</> data -----> interpolated based on 'col' data")

    return ("")