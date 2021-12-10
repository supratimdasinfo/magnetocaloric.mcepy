# 1. Download Python Software from https://www.python.org/downloads/
# 2. Open Command Prompt as Administrator.
# 3. To Check pip version type ‘pip --version’.
# 4. If Pip Is Installed And Working, You Will See A Version Number, Otherwise Type ‘python get-pip.py’ And Run.
# 5. To Download Required Libraries for This MCE program, Type Following
#    Commands:
#    a. pip install num2words
#    b. pip install matplotlib
#    c. pip install xlrd==1.2.0
#    d. pip install openpyxl
#    e. pip install tableprint
#    f. pip install xlsxwriter
#    g. pip install numpy

#IMPORT_LIBRARIES
import numpy as np
import xlsxwriter
import tableprint
from random import randint
import xlrd
import matplotlib.pyplot as plt
from num2words import num2words


#INPUT_VALUES

M_values = []
M = M_values
T = []
H = []

print("\n\n\n   -------------------------- I N P U T   F I E L D --------------------------")
print("\n   i.e. Please add one extra Magnetic Field in your excel sheet with Null \n   Magnetization values (M) to get accurate output.\n\n   e.g. If the value of Hmax = 50000, then add Hmax + ∇H \n\n")
datasample = [[0, -9.86761, -7.71622, '...'],[500, 4.69588, 7.84249, '...'],['...','...','...','...']]
tableprint.table(datasample, ['Magnetic Field (H)', 'Moment(M) at 40K','Moment(M) at 44K','...'])

yesorno = input("\n   Did You Enter The Data Into Your Excel Sheet Like This Format Given Above ?  ")

if yesorno == 'YES' :
     print ("\n")
elif yesorno == 'yes' :
     print ("\n")
else:
     print ("\n   Please Arrange Your Excel Data Like This Above Format.  ")
     exit()


Path = input("\n   OK, Enter Your Excel File Location (example : C:\File name.xlsx): ")
nn = int(input("\n   Enter the number of applied magnetic Field : "))
Num_val = int(input("\n   Enter the total number of M value you need to take from Excel sheet : "))
n = int(Num_val/nn)
print("\n\n   OK...Now, enter", num2words(n), "Temperature Values\n")

for b in range(0, (n)):
     T_v = input("   Enter the Temperature Value : ")
     T.append(T_v)
          
print("\n\n   Now, From This Table data : \n")


     
book = xlrd.open_workbook(Path)
sheet = book.sheet_by_name('Sheet1')

data = [[sheet.cell_value(r, c) for c in range(n+1)] for r in range(sheet.nrows)]

Del_H = data[2][0] - data[1][0]

for a in range(1, nn+1, 1):          

     H.append((data[a])[0])
     for b in range(0, n):
          T.append(T[b])
               
     for b in range(1, n+1):
          M.append((data[a])[b])





# MCE Calculation

S_TT = 0

for j in range(0, (nn-1), 1):
     lw = n*j
     up = ((j+1)*n) - 1
     S_T = 0

     for i in range (lw, up, 1):
          S_m = ((float(M[i+1]) - float(M[i]))/(float(T[i+1]) - float(T[i]))) * (float(H[j+1]) - float(H[j]))
          S_T += S_m
          
          S_T = float(S_T)


     S_TT += S_T







DSSSort = []
TSort = []
indmax = nn - 2
Multiplier = (H[indmax]-H[0])/10
for q in range(0, n-1, 1):
       
     S_TTT = 0
     DSSort = []

     lww = q
     for j,i in zip(range(0, (nn-1), 1),range(q, Num_val, n)):

          S_mm = ((float(M[i+1]) - float(M[i]))/(float(T[i+1]) - float(T[i]))) * (float(H[j+1]) - float(H[j]))
          S_TTT += S_mm
          S_TTT = float(S_TTT)
          Hj = H[j]
          HHj = Hj % Multiplier
          neg_S_TTT = -S_TTT
          if HHj == 0 :
               DSSort.append(neg_S_TTT)
                    
     TSort.append(float(T[q]))
     DSSSort.append(DSSort)

     
Label = []
for i in range(0, 11, 1):
     Label.append(str((i*Multiplier*((10)**(-4)))))


tem = []
for i in range(0, n-1, 1):
     tempr = T[i]
     tem.append(tempr)

del_S_values = []

del_S_values.append(tem)

DSfinall = []
for j in range(0, 11, 1):

     DSfinal = []
     for i in range(0, n-1, 1):
          DSfinal.append((10**(-4))*(DSSSort[i])[j])
     DSfinall.append(DSfinal)
     del_S_values.append(DSfinal)

     
colour = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'tab:orange', 'tab:gray', 'tab:brown', 'tab:blue']


     
dirt = input("\n   Enter The File Name With Path (example : C:\File name.xlsx), In Which You Want To Save The ∇S data at those specific Temperatures : ")
dirtt = input("\n   Enter The File Name With Path (example : C:\File name.xlsx), In Which You Want To Save The M^2 vs H/M data at those specific Temperatures : ")





workbook = xlsxwriter.Workbook(dirt)
worksheet = workbook.add_worksheet()

row = 0
for col, data in enumerate(del_S_values):
     worksheet.write_column(row, col, data)

workbook.close()





nnp = nn - 1
M_plot_final = []
H_plot_final = H
H_plot_final.pop(nnp)
for k in range(0, (n), 1):
     
     M_plot = []
     for l in range(0, (nn-1), 1):

          index = (((l+1)*(n - k)) + l*k) - 1
          M_plot.append(M[index])

     M_plot_final.append(M_plot)






M_sqr = np.square(M_plot_final)

H_by_M = []

for j in range(0, n, 1):
    H_by_M_1D = []
    for i in range(0, nn-1, 1):
        
        H_by_M_val = H_plot_final[i] / M_plot_final[j][i]
        H_by_M_1D.append(H_by_M_val)
        
            
    H_by_M.append(H_by_M_1D)






#GRAPH_PLOT

plt.subplot(2,2,1)
for q in range(0, 11, 1):
     for j in range(0, n-1, 1):
          plt.plot((TSort), (DSfinall[q]), linestyle='solid', color = colour[q], marker = 'o')

     for j in range(0, 1, 1):
          plt.plot((TSort)[0], ((DSfinall[q])[0]), linestyle='solid',label= Label[q], color = colour[q], marker = 'o')
          plt.legend(loc='upper right')   

plt.xlabel("Temperature")
plt.ylabel("-∇S")
plt.title("Change in Entropy vs Temperature")

    


plt.subplot(2,2,2)
for k in range (0, n, 1):
     plcolour = (randint(0.0,1.0), randint(0.0,1.0), randint(0.0,1.0))
     plt.plot(H_plot_final, M_plot_final[k], linestyle='solid', c = plcolour, marker = 'o', label = T[k] )


plt.legend(loc='upper right')     
plt.xlabel("Magnetic Field(H)")
plt.ylabel("Magnetization(M)")
plt.title("Magnetization vs Applied Field")



plt.subplot(2,2,3)
for i in range (0, n, 1):
    plt.plot(H_by_M[i], M_sqr[i], linestyle='solid', label = T[i])


plt.legend(loc='upper right')     
plt.xlabel("H/M (Applied Field / Magnetization)")
plt.ylabel("M^2 (Magnetization Square)")
plt.title("M^2 vs H/M")
plt.show()






for i in range (0,2*n,1):
    lo = 2*i+1
    T.insert(lo, '   ')   
    
xla = H_by_M
xlb = M_sqr.tolist()



for i in range (0,n,1):
    x_index = 2*i + 1
    xla.insert(x_index, xlb[i])

for i in range (0,2*n,1):

    xla[i].insert(0, T[i])
    xla[i].insert(1, ' ')
    if i%2 == 0 :
        xla[i].insert(2, 'H/M')
    else:
        xla[i].insert(2, 'M^2')
        


  


workbook = xlsxwriter.Workbook(dirtt)
worksheet = workbook.add_worksheet()

row = 0
for col, data in enumerate(xla):
     worksheet.write_column(row, col, data)

workbook.close()
print ("\n   Please Check Your Excel Files, Data Successfully Saved In These Files")

#Encoded By Supratim Das...
