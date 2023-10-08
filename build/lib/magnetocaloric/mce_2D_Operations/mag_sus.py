import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def mag_sus(g_name, n, one_n, T, H, M, field, linear_threshold):
	T_sus = [T[i] for i in range(0, n)]
	M_sus_con = []
	mm = 0
	nn = n
	for j in range(0, one_n):
		M_sus = []
		for i in range(mm, nn):
			M_sus.append(M[i])
		mm += n	
		nn += n	
		M_sus_con.append(M_sus)


	sus_head = []
	arrow = []	
	sus_head_int = []
	for i in range(0, n):
		sus_head_int.append(str(T_sus[i]))
		arrow.append('↓')
	sus_head.append(sus_head_int)
	sus_head[0].insert(0, 'Temperature')
	sus_head[0].insert(1, '→')
	arrow.insert(0, 'Field(H)')
	arrow.insert(1, '')
	sus_head.append(arrow)

	last_array = M_sus_con[-1]
	contains_string = any(isinstance(item, str) for item in last_array)

	# If there's at least one string element, remove the last array
	if contains_string:
	    M_sus_con.pop()
	    sus_sus_inv_con = []

	    for i in range(0, one_n-1):          

	        sus_inv_store = []
	        sus_store = []
	        for j in range(0, n):
	            sus_inv_store.append(str(H[i]/(M_sus_con[i])[j]))
	            sus_store.append(str(M_sus_con[i][j]/H[i]))   
	        sus_sus_inv_con.append(sus_inv_store)
	        sus_sus_inv_con.append(sus_store)  
	    for i, j, k in zip(range(0, 2*(one_n-1), 2), range(1, 2*(one_n-1), 2), range(0, (one_n-1))):
	        sus_sus_inv_con[i].insert(0, str(H[k]))
	        sus_sus_inv_con[i].insert(1, f"1/Chi →")
	        sus_sus_inv_con[j].insert(0, ' ')
	        sus_sus_inv_con[j].insert(1, 'Chi →')

	    for i in range(0, 2*(one_n-1)):
	        sus_head.append(sus_sus_inv_con[i])


	else:
	    sus_sus_inv_con =[]
	    for i in range(0, one_n):
	        sus_inv_store = []
	        sus_store = []
	        for j in range(0, n):
	            sus_inv_store.append(str(H[i]/(M_sus_con[i])[j]))
	            sus_store.append(str(M_sus_con[i][j]/H[i]))	
	        sus_sus_inv_con.append(sus_inv_store)
	        sus_sus_inv_con.append(sus_store)
	    for i,j,k in zip(range(0, 2*one_n, 2), range(1, 2*one_n, 2), range(0, one_n)):
	        sus_sus_inv_con[i].insert(0 , str(H[k]))
	        sus_sus_inv_con[i].insert(1 , f"1/Chi →")
	        sus_sus_inv_con[j].insert(0 , ' ')
	        sus_sus_inv_con[j].insert(1 , 'Chi →')		

	    for i in range(0, 2*one_n):
	            sus_head.append(sus_sus_inv_con[i])


	susceptibility_final = sus_head

	H_ind = None
	for i in range(0, one_n):
		if field == str(H[i]):
			H_ind = i
			break
			
	sus_inv = [H[int(H_ind)]/M_sus_con[int(H_ind)][i] for i in range(0, n)]
	sus = [M_sus_con[int(H_ind)][i]/H[int(H_ind)] for i in range(0, n)]


	T_sus_inp = np.linspace(min(T_sus), max(T_sus), 100)
	sus_inv_interpol = np.interp(T_sus_inp, T_sus, sus_inv)
	sus_interpol = np.interp(T_sus_inp, T_sus, sus)

	ele = 0
	for l in range (2, n):
		sus_inv_last = sus_inv[-l:]
		T_sus_last = T_sus[-l:]
		slope, intercept, r_value, p_value, std_err = stats.linregress(T_sus_last, sus_inv_last)
		if (linear_threshold >= r_value):
			ele = (l)
			break

	np_T_sus = np.asarray(T_sus[-ele:])		
	regression_line = float(slope) * np_T_sus + float(intercept)

	np_T_sus_bu = np_T_sus
	regression_bu = sus_inv[-ele:]
	x = float((round(min(sus), 2) - float(intercept))/float(slope))
	regression_line = np.insert(regression_line, 0, 0)
	np_T_sus = np.insert(np_T_sus, 0, x)



	return susceptibility_final, T_sus, sus_inv, sus, np_T_sus, regression_line, np_T_sus_bu, regression_bu, x



