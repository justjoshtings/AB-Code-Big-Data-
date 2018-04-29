import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


file_path = 'Shift_Output_Data.xlsx'
try:
	shift_can_output_data = pd.read_excel(file_path, sheet_name='Shift_Output', header=0, index_col=None, usecols='A:U')
except FileNotFoundError:
	print("File not found! Please check file name")
except IOError:
	print("Error loading file!")

# print(shift_can_output_data.head())

def calc_total_cans_per_shift(shift_can_output_data):
	num_shifts = shift_can_output_data.shape[1]
	num_shifts_per_day = 3
	total_cans_shift_1_lst = np.empty(shape=(int(num_shifts/num_shifts_per_day), 1))
	total_cans_shift_2_lst = np.empty(shape=(int(num_shifts/num_shifts_per_day), 1))
	total_cans_shift_3_lst = np.empty(shape=(int(num_shifts/num_shifts_per_day), 1))
	counter = 0
	for i in range(int(num_shifts/num_shifts_per_day)):
		for j in range(num_shifts_per_day):
			counter += 1
			if j == 0:
				total_cans_shift_1_lst[i] = shift_can_output_data.loc[counter].sum()
			elif j == 1:
				total_cans_shift_2_lst[i] = shift_can_output_data.loc[counter].sum()
			elif j == 2:
				total_cans_shift_3_lst[i] = shift_can_output_data.loc[counter].sum()
			else:
				print("Error in shift numbers!")
	total_cans_shift_lst = np.array([total_cans_shift_1_lst, total_cans_shift_2_lst, total_cans_shift_3_lst])
	return total_cans_shift_lst

def bar_plot(total_cans_shift_lst):
	avg_shift_output = []
	total_shift_output = []
	for i in range(total_cans_shift_lst.shape[0]):
		mean_output = np.mean(total_cans_shift_lst[i])
		avg_shift_output.append(mean_output)
		total_ouput = np.sum(total_cans_shift_lst[i])
		total_shift_output.append(total_ouput)
	

	all_shift_output = np.sum(total_shift_output)
	percentage_of_total_output = []
	for i in range(total_cans_shift_lst.shape[0]):
		percentage_of_total_output.append((total_shift_output[i]/all_shift_output)*100)

	X = [1, 2, 3]
	
	total_shift_output = [2525553, 3089514, 2623086]
	avg_shift_output = [420926, 514919, 437181]
	percentage_of_total_output = []
	for i in range(3):
		percentage_of_total_output.append((total_shift_output[i]/sum(total_shift_output))*100)

	X = [1, 2, 3]
	X_labels = ['Shift 1', 'Shift 2', 'Shift 3']

	fig, ax = plt.subplots()
	ax.bar(X, avg_shift_output, align='center')
	ax.set_xticklabels(X_labels)
	ax.set_xticks(X)
	plt.xlabel('Shift #')
	# plt.ylim(0,55)
	plt.grid(True)
	plt.ylabel('Average Output (# of Cans)')
	plt.title('Average Output per Shift')
	ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda X, loc: "{:,}".format(int(X))))

	for i in range(3):
		v = avg_shift_output[i]+3000
		ax.text(i+.9, v, "{:,.0f}".format(avg_shift_output[i]), color='black', va='center', fontweight='bold', fontsize=10)
	
	fig, ax = plt.subplots()
	ax.bar(X, total_shift_output, align='center')
	ax.set_xticklabels(X_labels)
	ax.set_xticks(X)
	plt.xlabel('Shift #')
	# plt.ylim(0,55)
	plt.grid(True)
	plt.ylabel('Total Output (# of Cans)')
	plt.title('Total Output per Shift')

	for i in range(3):
		v = total_shift_output[i]+60000
		ax.text(i+.9, v, "{:,.0f}".format(total_shift_output[i]), color='black', va='center', fontweight='bold', fontsize=10)
	
	ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda X, loc: "{:,}".format(int(X))))

	fig, ax = plt.subplots()
	ax.bar(X, percentage_of_total_output, align='center')
	ax.set_xticklabels(X_labels)
	ax.set_xticks(X)
	plt.xlabel('Shift #')
	plt.ylim(0,50)
	plt.grid(True)
	plt.ylabel('Percentage of Total Output (%)')
	plt.title('Output Distribution Per Shift')

	for i in range(3):
		v = percentage_of_total_output[i]+5
		ax.text(i+.95, v, "{:.1f}%".format(percentage_of_total_output[i]), color='black', va='center', fontweight='bold', fontsize=10)
		ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda X, loc: "{:,}".format(int(X))))

	plt.show()


total_cans_shift_lst = calc_total_cans_per_shift(shift_can_output_data)
bar_plot(total_cans_shift_lst)

file_path = 'Shift_Output_Data.xlsx'
try:
	shift_speed_data = pd.read_excel(file_path, sheet_name='Sheet2', header=0, index_col=None, usecols='A:C')
except FileNotFoundError:
	print("File not found! Please check file name")
except IOError:
	print("Error loading file!")

def speed_graphs(shift_speed_data):
	shift_speed_lst = []
	for i in range(3):
		mean_speed = np.mean(shift_speed_data.loc[i]*100)
		shift_speed_lst.append(mean_speed)

	X = [1, 2, 3]
	X_labels = ['Shift 1', 'Shift 2', 'Shift 3']
	shift_speed_lst = [50.84, 62.19, 52.80]

	fig, ax = plt.subplots()
	ax.bar(X, shift_speed_lst, align='center')
	ax.set_xticklabels(X_labels)
	ax.set_xticks(X)
	plt.xlabel('Shift #')
	plt.ylabel('Percentage of Maximum Potential Operation Speed (%)')
	plt.ylim(0, 80)
	plt.grid(True)
	plt.title('Line Operational Speed Per Shift')	

	for i in range(3):
		v = shift_speed_lst[i]+5
		ax.text(i+.9, v, "{:.1f}%".format(shift_speed_lst[i]), color='black', va='center', fontweight='bold', fontsize=10)

	plt.show()

speed_graphs(shift_speed_data)






