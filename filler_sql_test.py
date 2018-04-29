import sqlite3
import pandas as pd
from pandas import ExcelWriter
from matplotlib import pyplot as plt
import numpy as np

conn = sqlite3.connect('filler.db') #Has table: 'filler'

c = conn.cursor()

def get_lines(num):
	return print(pd.read_sql_query("SELECT * FROM filler LIMIT ?;", conn, params=(num, )))

def get_headers():
	return print(pd.read_sql_query("PRAGMA table_info(filler);", conn))

def num_dumps():
	return print(pd.read_sql_query("SELECT * FROM filler WHERE 'Warm Bowl Dump Y/N' = 1 LIMIT 10;", conn))

def get_avg_fault_duration():
	return print(pd.read_sql_query("SELECT * FROM faults WHERE 'Duration' LIMIT 15;", conn))


coords = c.execute("""
		  SELECT "Equipment Fault Number & Desc",
		  "Equipment Short Name",
		  CAST("Duration" as float), 
		  CAST("Count of Faults" as float) 
		  FROM faults;"""
		).fetchall()

def avg_fault_duration(coords):
	df = pd.DataFrame(columns=['Equipment Name', 'Short Name', 'Avg. Fault Duration'])
	for i in range(len(coords)):
		is_six = coords[i][2]/coords[i][3]
		if  is_six >= 6:
			df.loc[i] = [coords[i][0], coords[i][1], is_six]
	# print(df)
	# print("There are {} individual faults with greater than 6 minutes duration per fault.".format(len(df)))
	# df.to_csv('avg_fault_duration.csv', sep='\t', encoding='utf-8')
	writer = ExcelWriter('Faults.xlsx')
	df.to_excel(writer, 'Avg Fault Duration')
	writer.save()
	return

def most_occurances(coords):
	df2 = pd.DataFrame(columns=['Equipment Name', 'Short Name', 'Count of Faults'])	
	for i in range(len(coords)):
		df2.loc[i] = [coords[i][0], coords[i][1], coords[i][3]]
	df2.sort_values(by=['Count of Faults'])
	# print(df2)
	# df2.to_csv('most_occurances.csv', sep='\t', encoding='utf-8')
	writer2 = ExcelWriter('Faults2.xlsx')
	df2.to_excel(writer2, 'Most Occurances')
	writer2.save()
	return

# avg_fault_duration(coords)
# most_occurances(coords)
# 
def cross_ref(coords):
	df = pd.DataFrame(columns=['Equipment Name', 'Short Name', 'Avg. Fault Duration'])
	for i in range(len(coords)):
		is_six = coords[i][2]/coords[i][3]
		df.loc[i] = [coords[i][0], coords[i][1], is_six]
	df2 = pd.DataFrame(columns=['Equipment Name', 'Short Name', 'Count of Faults'])	
	for i in range(len(coords)):
		df2.loc[i] = [coords[i][0], coords[i][1], coords[i][3]]
	df2.sort_values(by=['Count of Faults'])
	df3 = pd.DataFrame(columns=['Equipment Name', 'Short Name', 'Avg. Fault Duration', 'Count of Faults'])
	for i in range(len(coords)):
		if df.loc[i][0] == df2.loc[i][0]:
	 		df3.loc[i] = [df.loc[i][0], df.loc[i][1], df.loc[i][2], df2.loc[i][2]]
	print('Run1')
	df4 = pd.DataFrame(columns=['Equipment Name', 'Short Name', 'Avg. Fault Duration', 'Count of Faults'])
	for i in range(len(coords)):
		if float(df3.loc[i][2]) >= 5.5:
			df4.loc[i] = [df3.loc[i][0], df3.loc[i][1], df3.loc[i][2], df3.loc[i][3]]
	print('Run2')
	writer = ExcelWriter('Faults3.xlsx')
	df4.to_excel(writer, 'Cross Reference')
	writer.save()

def between_six_twelve(coords):
	df = pd.DataFrame(columns=['Equipment Name', 'Short Name', 'Avg. Fault Duration Per Fault', 'Count of Faults'])
	df2 = pd.DataFrame(columns=['Equipment Name', 'Short Name', 'Avg. Fault Duration Per Fault', 'Count of Faults'])
	sum_is=0
	sum_isnot=0
	breakdown = 0
	not_breakdown = 0
	for i in range(len(coords)):
		is_six_twelve = coords[i][2]/coords[i][3]
		if is_six_twelve >= 6 and is_six_twelve <= 12.5:
			df.loc[i] = [coords[i][0], coords[i][1], is_six_twelve, coords[i][3]]
			temp_sum_is = coords[i][2]
			sum_is += temp_sum_is
			temp_breakdown = coords[i][3]
			breakdown += temp_breakdown
		else:
			df2.loc[i] = [coords[i][0], coords[i][1], is_six_twelve, coords[i][3]]
			temp_sum_isnot = coords[i][2]
			sum_isnot += temp_sum_isnot
			temp_not_breakdown = coords[i][3]
			not_breakdown += temp_not_breakdown
	total_sums = sum_isnot+sum_is
	percent_is = (sum_is/total_sums)*100
	total_sums_breakdowns = breakdown+not_breakdown
	percent_breakdowns_saved = (breakdown/total_sums_breakdowns)*100
	df3 = pd.DataFrame(columns=['Total Fault Duration (mins) (6-12mins)', 'Total Fault Duration (mins) (Not 6-12mins)', 'Sum of Total Fault Durations (mins)', 'Percentage of Fault Duration Saved'])
	df3.loc[0] = [sum_is, sum_isnot, total_sums, percent_is] 
	df4 = pd.DataFrame(columns=['Total Number of Breakdowns (6-12mins)', 'Total Number of Breakdowns (Not 6-12mins)', 'Sum of Total Number of Breakdowns', 'Percentage of Number of Faults Saved'])
	df4.loc[0] = [breakdown, not_breakdown, total_sums_breakdowns, percent_breakdowns_saved]
	writer = ExcelWriter('Faults3.xlsx')
	df.to_excel(writer, sheet_name='Processes Between 6mins and 12.5mins')
	df2.to_excel(writer, sheet_name='Processes Not Between 6mins and 12.5mins')
	df3.to_excel(writer, sheet_name='Savings')
	df4.to_excel(writer, sheet_name='Savings - Breakdowns')
	writer.save()

def from_six_on(coords):
	df = pd.DataFrame(columns=['Equipment Name', 'Short Name', 'Avg. Fault Duration Per Fault', 'Count of Faults'])
	num_of_stops_over_6 = 0
	for i in range(len(coords)):
		avg_fault_duration = coords[i][2]/coords[i][3]
		if avg_fault_duration >= 0:
			num_of_stops_over_6 += coords[i][3]
		df.loc[i] = [coords[i][0], coords[i][1], avg_fault_duration, coords[i][3]]
	df_sorted_by_duration = df.sort_values(by=['Avg. Fault Duration Per Fault'])
	print(df['Count of Faults'].sum())


	num_of_stoppages_over_lst = []
	for i in range(6, 470): #470 minutes
		percentage_done =((i-6)/(470-6))*100
		print("{:.1f}% Done".format(percentage_done))
		xtime = i
		num_stoppages_over_xtime = 0
		for j in range(df_sorted_by_duration.shape[0]):
			if df_sorted_by_duration.loc[j][2] >= xtime:
				num_stoppages_over_xtime += df_sorted_by_duration.loc[j][3]
		num_of_stoppages_over_lst.append(num_stoppages_over_xtime)
	num_of_stoppages_over_lst_new = []
	for i in range(len(num_of_stoppages_over_lst)):
		temp_insert = (1 - (num_of_stoppages_over_lst[i]/num_of_stops_over_6))*100
		num_of_stoppages_over_lst_new.append(temp_insert)
	x_axis = np.arange(6,470,1)
	plt.figure(figsize=(10,7))
	plt.plot(x_axis, num_of_stoppages_over_lst_new, 'r--', markersize=8)
	plt.xlim(6, 24)
	plt.yticks(np.arange(min(num_of_stoppages_over_lst_new), max(num_of_stoppages_over_lst_new)+10, 10))
	plt.xticks(np.arange(min(x_axis), 26, 2))
	# plt.xscale('log')
	plt.grid(True)
	plt.ylabel('Percentage of Avg. Number of Faults (%)')
	plt.xlabel('Breakdown Duration (Mins)')
	plt.title('Percentage of Faults Over Breakdown Duration (Log-Scale)')
	plt.show()			


def from_six_on_classify_faults(coords):
	df_6_13 = pd.DataFrame(columns=['Equipment Name', 'Short Name', 'Avg. Fault Duration Per Fault', 'Count of Faults'])

	index_label = 0
	total_faults_6_13 = 0
	for i in range(len(coords)): #Narrow data into 6 - 13 mins and insert into data frame
		avg_fault_duration = coords[i][2]/coords[i][3]
		if avg_fault_duration >= 6 and avg_fault_duration <= 13:
			df_6_13.loc[index_label] = [coords[i][0], coords[i][1], avg_fault_duration, coords[i][3]]
			index_label += 1
			total_faults_6_13 += coords[i][3]

	fault_dict = {df_6_13.loc[0][1]:0}
	for i in range(df_6_13.shape[0]):
		fault_dict.update({df_6_13.loc[i][1]:0})

	key_values = []
	for key, value in fault_dict.items():
		key_values.append(key)

	for i in range(df_6_13.shape[0]):
		for j in range(len(key_values)):
			if df_6_13.loc[i][1] == key_values[j]:
				fault_dict[key_values[j]] += df_6_13.loc[i][3]
	# print(fault_dict)
	# # print(sum(fault_dict.values()))
	# print(total_faults_6_13)
	faults_distribution_lst = []	
	for key, value in fault_dict.items():
		faults_distribution_lst.append((value/total_faults_6_13)*100)

	X = np.arange(len(key_values))
	fig, ax = plt.subplots()
	barlist = ax.bar(X, faults_distribution_lst, align='center', color='seagreen')
	ax.set_xticklabels(key_values)
	ax.set_xticks(X)
	plt.xticks(rotation='65')
	ax.tick_params(axis = 'x', which = 'major', labelsize = 8)
	# plt.ylim(0,570000)
	# plt.grid(True)
	plt.ylabel('Percentage of Total Faults Instances (%)')
	plt.title('Distribution of Breakdown Instances to Processes with Breakdown Durations Between 6-13 mins')

	for i in range(len(faults_distribution_lst)):
			v = faults_distribution_lst[i]+1
			ax.text(i-0.4, v, "{:,.1f}%".format(faults_distribution_lst[i]), color='black', va='center', fontweight='bold', fontsize=9)
	ax.text(16, 25, "Total Number of Faults\nBetween 6-13 mins: {:,.0f}".format(total_faults_6_13, color='black', va='center', fontweight='5', fontsize=12))
	ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda X, loc: "{:,}".format(int(X))))

	plt.show()



# from_six_on_classify_faults(coords)
# between_six_twelve(coords)
# test(coords)
# from_six_on(coords)

conn.close()