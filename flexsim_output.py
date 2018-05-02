import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import patches as mpatches


file_path = 'FlexSim_Output.xlsx'
try:
	sum_at_filler_df = pd.read_excel(file_path, sheet_name='Sum At Filler', header=0, index_col=None, usecols='B:S')
except FileNotFoundError:
	print("File not found! Please check file name")
except IOError:
	print("Error loading file!")

try:
	sum_at_filler_df2 = pd.read_excel(file_path, sheet_name='Sum At Filler', header=0, index_col=None, usecols='I:S')
except FileNotFoundError:
	print("File not found! Please check file name")
except IOError:
	print("Error loading file!")

try:
	sum_at_filler_df3 = pd.read_excel(file_path, sheet_name='Sheet1', header=0, index_col=None, usecols='A:I')
except FileNotFoundError:
	print("File not found! Please check file name")
except IOError:
	print("Error loading file!")

try:
	sum_at_filler_df4 = pd.read_excel(file_path, sheet_name='Sheet2', header=0, index_col=None, usecols='A:H')
except FileNotFoundError:
	print("File not found! Please check file name")
except IOError:
	print("Error loading file!")


def bar_plot(sum_at_filler_df, loop_num):
	X = []
	sum_at_filler_lst = []
	value_at_zero = 444226
	for i in range(sum_at_filler_df.shape[1]):
		X.append(i+1)
		sum_at_filler_lst.append(abs((((sum_at_filler_df.loc[0][i])-value_at_zero)/value_at_zero)*100))
	X_labels = list(sum_at_filler_df)

	fig, ax = plt.subplots()
	barlist = ax.bar(X, sum_at_filler_lst, align='center', edgecolor='black')
	ax.set_xticklabels(X_labels)
	ax.set_xticks(X)
	
	plt.ylim(-1,27)
	# plt.grid(True)
	plt.ylabel('Percentage Increase (%)')
	plt.title('Output Percentage Increase for Simulations of Different Breakdown Situations')
	
	ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda X, loc: "{:,}".format(int(X))))
	
	if loop_num == 0:
		plt.xticks(rotation='55')
		ax.tick_params(axis = 'x', which = 'major', labelsize = 6)
		color_list = list(range(10,17))
		barlist[7].set_color('lightgreen')
		barlist[8].set_color('lightcoral')
		barlist[9].set_color('lightcoral')
		barlist[17].set_color('lightgreen')
		for i in range(len(color_list)):
			barlist[color_list[i]].set_color('crimson')

		for i in range(len(sum_at_filler_lst)):
			v = sum_at_filler_lst[i]+1
			ax.text(i+0.65, v, "{:,.1f}%".format(sum_at_filler_lst[i]), color='black', va='center', fontweight='bold', fontsize=9)

		red_patch = mpatches.Patch(color='crimson', label='Effective Change Scenarios')
		c_patch = mpatches.Patch(color='lightgreen', label='Extreme Change Scenarios')
		m_patch = mpatches.Patch(color='lightcoral', label='Non-Effective Change Scenarios')
		b_patch = mpatches.Patch(color='dodgerblue', label='Other Scenarios')
		plt.legend(handles=[red_patch, c_patch, m_patch, b_patch], loc=2, prop={'size': 8})
	
	elif loop_num == 1:
		plt.xticks(rotation='35')
		ax.tick_params(axis = 'x', which = 'major', labelsize = 8)
		color_list = list(range(3,10))
		barlist[0].set_color('lightgreen')
		barlist[1].set_color('lightcoral')
		barlist[2].set_color('lightcoral')
		barlist[10].set_color('lightgreen')
		for i in range(len(color_list)):
			barlist[color_list[i]].set_color('crimson')

		for i in range(len(sum_at_filler_lst)):
			v = sum_at_filler_lst[i]+1
			ax.text(i+0.65, v, "{:,.1f}%".format(sum_at_filler_lst[i]), color='black', va='center', fontweight='bold', fontsize=9)

		red_patch = mpatches.Patch(color='crimson', label='Effective Change Scenarios')
		c_patch = mpatches.Patch(color='lightgreen', label='Extreme Change Scenarios')
		m_patch = mpatches.Patch(color='lightcoral', label='Non-Effective Change Scenarios')
		plt.legend(handles=[red_patch, c_patch, m_patch], loc=2, prop={'size': 8}) 

	elif loop_num == 2:
		plt.xticks(rotation='35')
		ax.tick_params(axis = 'x', which = 'major', labelsize = 8)
		color_list = list(range(2,6))
		barlist[6].set_color('firebrick')
		barlist[1].set_color('firebrick')
		barlist[7].set_color('firebrick')
		# barlist[2].set_color('lightcoral')
		# barlist[10].set_color('forestgreen')
		for i in range(len(color_list)):
			barlist[color_list[i]].set_color('orange')

		for i in range(len(sum_at_filler_lst)):
			v = sum_at_filler_lst[i]+1
			ax.text(i+.75, v, "{:,.1f}%".format(sum_at_filler_lst[i]), color='black', va='center', fontweight='bold', fontsize=9)

		red_patch = mpatches.Patch(color='firebrick', label='Process Improvement Scenarios')
		c_patch = mpatches.Patch(color='orange', label='Breakdown Reduction Scenarios')
		m_patch = mpatches.Patch(color='dodgerblue', label='Extreme Scenarios')
		plt.legend(handles=[red_patch, c_patch, m_patch], loc=2, prop={'size': 10}) 
	
	elif loop_num == 3:
		plt.xticks(rotation='50')
		ax.tick_params(axis = 'x', which = 'major', labelsize = 8)
		barlist[0].set_color('dimgray')
		barlist[11].set_color('dimgray')
		barlist[1].set_color('forestgreen')
		barlist[2].set_color('forestgreen')
		barlist[3].set_color('forestgreen')
		barlist[6].set_color('forestgreen')
		barlist[9].set_color('forestgreen')
		barlist[4].set_color('orange')
		barlist[7].set_color('orange')
		barlist[10].set_color('orange')
		
		barlist[5].set_color('orange')
		barlist[5].set_hatch(hatch='-')
		barlist[8].set_color('orange')

		for i in range(len(sum_at_filler_lst)):
			v = sum_at_filler_lst[i]+1
			ax.text(i+0.65, v, "{:,.1f}%".format(sum_at_filler_lst[i]), color='black', va='center', fontweight='bold', fontsize=9)

		red_patch = mpatches.Patch(color='dimgray', label='Extreme Scenarios')
		another_patch = mpatches.Patch(color='forestgreen', label='Seamer')
		idk_patch = mpatches.Patch(color='orange', label='Packers')
		c_patch = mpatches.Patch(color='lightcoral', label='Combined Processes')
		# m_patch = mpatches.Patch(color='dodgerblue', label='Extreme Scenarios')
		plt.legend(handles=[red_patch, another_patch, idk_patch, c_patch], loc=2, prop={'size': 10}) 
	

	plt.show()

# bar_plt_lst = [sum_at_filler_df, sum_at_filler_df2, sum_at_filler_df3, sum_at_filler_df4]
# for i in range(len(bar_plt_lst)):
# 	bar_plot(bar_plt_lst[i], i)

file_path = 'Faults2_Greg.xlsx'
try:
	distribution_faults_df = pd.read_excel(file_path, sheet_name='Sheet2', header=0, index_col=None, usecols='A:B')
except FileNotFoundError:
	print("File not found! Please check file name")
except IOError:
	print("Error loading file!")

def plot(distribution_faults_df):
	X = []
	Y = []
	for i in range(distribution_faults_df.shape[0]):
		X.append(distribution_faults_df.loc[i][0])
		Y.append((distribution_faults_df.loc[i][1])*100)
		if distribution_faults_df.loc[i][0] == 13.0:
			at_13 = (distribution_faults_df.loc[i][1])*100

	labels = list(distribution_faults_df)
	plt.plot(X, Y, linewidth=3)
	plt.grid(True)
	plt.xlabel(labels[0])
	plt.ylabel(labels[1])
	plt.title('Percentage of Faults Over Breakdown Duration')
	plt.xlim(6, 31)
	plt.yticks(np.arange(0, 80, 10))
	plt.xticks(np.arange(6, 32, 2))
	# plt.text(7.5, at_13+7, 'Percentage of Faults\nUnder 13 Mins:\n{:.1f}%'.format(at_13), fontsize=13)
	# plt.axvline(x=13.0, color='r', linestyle='--')
	# horiz_line_data = np.array([at_13 for i in range(len(X))])
	# plt.plot(X, horiz_line_data, 'r--') 

	plt.show()

# plot(distribution_faults_df)

def bar_plot2(sum_at_filler_df, loop_num):
	X = []
	sum_at_filler_lst = []
	value_at_zero = 444226/1000
	for i in range(sum_at_filler_df.shape[1]):
		X.append(i+1)
		sum_at_filler_lst.append(sum_at_filler_df.loc[0][i]/1000)
	X_labels = list(sum_at_filler_df)

	fig, ax = plt.subplots()
	barlist = ax.bar(X, sum_at_filler_lst, align='center')
	ax.set_xticklabels(X_labels)
	ax.set_xticks(X)
	
	plt.ylim(300,625)
	# plt.grid(True)
	plt.ylabel('Total # of Cans Output per Shift (1000s Cans)')
	plt.title('Output Increase for Simulations of Different Breakdown Situations')
	
	ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda X, loc: "{:,}".format(int(X))))
	
	if loop_num == 0:
		plt.xticks(rotation='55')
		ax.tick_params(axis = 'x', which = 'major', labelsize = 6)
		color_list = list(range(10,17))
		barlist[7].set_color('lightgreen')
		barlist[8].set_color('lightcoral')
		barlist[9].set_color('lightcoral')
		barlist[17].set_color('lightgreen')
		for i in range(len(color_list)):
			barlist[color_list[i]].set_color('crimson')

		for i in range(len(sum_at_filler_lst)):
			v = sum_at_filler_lst[i]+15
			ax.text(i+0.65, v, "+ {:,.1f}%".format(abs(((sum_at_filler_lst[i]-value_at_zero)/value_at_zero)*100)), color='black', va='center', fontweight='bold', fontsize=9)

		red_patch = mpatches.Patch(color='crimson', label='Effective Change Scenarios')
		c_patch = mpatches.Patch(color='lightgreen', label='Extreme Change Scenarios')
		m_patch = mpatches.Patch(color='lightcoral', label='Non-Effective Change Scenarios')
		b_patch = mpatches.Patch(color='dodgerblue', label='Other Scenarios')
		plt.legend(handles=[red_patch, c_patch, m_patch, b_patch], loc=2, prop={'size': 8})
	
	elif loop_num == 1:
		plt.xticks(rotation='35')
		ax.tick_params(axis = 'x', which = 'major', labelsize = 8)
		color_list = list(range(3,10))
		barlist[0].set_color('lightgreen')
		barlist[1].set_color('lightcoral')
		barlist[2].set_color('lightcoral')
		barlist[10].set_color('lightgreen')
		for i in range(len(color_list)):
			barlist[color_list[i]].set_color('crimson')

		for i in range(len(sum_at_filler_lst)):
			v = sum_at_filler_lst[i]+15
			ax.text(i+0.65, v, "+ {:,.1f}%".format(abs(((sum_at_filler_lst[i]-value_at_zero)/value_at_zero)*100)), color='black', va='center', fontweight='bold', fontsize=9)

		red_patch = mpatches.Patch(color='crimson', label='Effective Change Scenarios')
		c_patch = mpatches.Patch(color='lightgreen', label='Extreme Change Scenarios')
		m_patch = mpatches.Patch(color='lightcoral', label='Non-Effective Change Scenarios')
		plt.legend(handles=[red_patch, c_patch, m_patch], loc=2, prop={'size': 8}) 

	elif loop_num == 2:
		plt.xticks(rotation='35')
		ax.tick_params(axis = 'x', which = 'major', labelsize = 8)
		color_list = list(range(2,6))
		barlist[6].set_color('firebrick')
		barlist[1].set_color('firebrick')
		barlist[7].set_color('firebrick')
		# barlist[2].set_color('lightcoral')
		# barlist[10].set_color('forestgreen')
		for i in range(len(color_list)):
			barlist[color_list[i]].set_color('orange')

		for i in range(len(sum_at_filler_lst)):
			v = sum_at_filler_lst[i]+15
			ax.text(i+.75, v, "+ {:,.1f}%".format(abs(((sum_at_filler_lst[i]-value_at_zero)/value_at_zero)*100)), color='black', va='center', fontweight='bold', fontsize=9)

		red_patch = mpatches.Patch(color='firebrick', label='Process Improvement Scenarios')
		c_patch = mpatches.Patch(color='orange', label='Breakdown Reduction Scenarios')
		m_patch = mpatches.Patch(color='dodgerblue', label='Extreme Scenarios')
		plt.legend(handles=[red_patch, c_patch, m_patch], loc=2, prop={'size': 10}) 
	
	elif loop_num == 3:
		plt.xticks(rotation='50')
		ax.tick_params(axis = 'x', which = 'major', labelsize = 8)
		barlist[0].set_color('dimgray')
		barlist[1].set_color('forestgreen')
		barlist[4].set_color('forestgreen')
		barlist[7].set_color('dimgray')
		barlist[2].set_color('orange')
		barlist[5].set_color('orange')
		
		barlist[3].set_color('orange')
		barlist[6].set_color('orange')

		for i in range(len(sum_at_filler_lst)):
			v = sum_at_filler_lst[i]+15
			ax.text(i+0.65, v, "+ {:,.1f}%".format(abs(((sum_at_filler_lst[i]-value_at_zero)/value_at_zero)*100)), color='black', va='center', fontweight='bold', fontsize=9)

		red_patch = mpatches.Patch(color='dimgray', label='Extreme Scenarios')
		another_patch = mpatches.Patch(color='forestgreen', label='Seamer')
		idk_patch = mpatches.Patch(color='orange', label='Packers')
		c_patch = mpatches.Patch(color='lightcoral', label='Combined Processes')
		# m_patch = mpatches.Patch(color='dodgerblue', label='Extreme Scenarios')
		plt.legend(handles=[red_patch, another_patch, idk_patch, c_patch], loc=2, prop={'size': 10}) 
	

	plt.show()

bar_plt_lst = [sum_at_filler_df, sum_at_filler_df2, sum_at_filler_df3, sum_at_filler_df4]
for i in range(len(bar_plt_lst)):
	bar_plot2(bar_plt_lst[i], i)


