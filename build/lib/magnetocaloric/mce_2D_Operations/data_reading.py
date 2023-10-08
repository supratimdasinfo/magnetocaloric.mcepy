import xlrd

def data_reading(file_dir, sheet_index, T_row, H_col):
    """
    Collects magnetization (M) and external fields (H) data from an Excel sheet.

    Parameters:
        file_dir (str): The file path of the Excel sheet.
        n (int): The number of temperature values (columns) in the Excel sheet.
        one_n (int): The number of data rows for each field value (H) in the Excel sheet.
        T (list): A list containing the temperature values.

    Returns:
        H (list): A list containing the external fields data.
        M (list): A list containing the magnetization data.
    """

    # Initialize empty lists to store magnetization (M) and external fields (H) data
    Magnetization_val = []
    External_Fields = []
    M = Magnetization_val
    H = External_Fields

    # Open the Excel file and read the data
    book = xlrd.open_workbook(file_dir)
    sheet = book.sheet_by_index(sheet_index-1)
    data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

    def column_letter_to_number(column_letter):
        column_number = 0
        for char in column_letter:
            # Convert the character to its ASCII value and subtract 64
            # to get the 1-based index (A=1, B=2, ..., Z=26)
            column_number = column_number * 26 + (ord(char.upper()) - 64)
        return column_number
    H_col_num = column_letter_to_number(H_col)
    T = data[T_row-1] 
    T.pop(0)
    # Loop to collect magnetization (M) and external fields (H) data from the Excel sheet
    for a in range(T_row, sheet.nrows, 1):
        H.append((data[a])[int(H_col_num)-1])
        for b in range(0, sheet.ncols-1):
            T.append(T[b])
        for b in range(H_col_num, sheet.ncols):
            M.append((data[a])[b])   
    two_n =  int((sheet.ncols-1)*(sheet.nrows-1))
    n = int(sheet.ncols-1)
    one_n = int(sheet.nrows-1)

    print ("</> source file accessed ---> cell_values successfuly stored in [data] \n ---> [M]<-->[H]<-->[T] seperated properly")
    # Return the collected external fields (H) and magnetization (M) data as lists
    return H, M, T, n, one_n, two_n