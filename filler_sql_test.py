import sqlite3
import pandas as pd
from pandas import ExcelWriter

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

def test(coords):
	df = pd.DataFrame(columns=['Equipment Name', 'Short Name', 'Avg. Fault Duration Per Fault', 'Count of Faults'])
	for i in range(len(coords)):
		df.loc[i] = [coords[i][0], coords[i][1], coords[i][2], coords[i][3]]
	writer = ExcelWriter('Test.xlsx')
	df.to_excel(writer, sheet_name='Processes Between 6mins and 12.5mins')
	writer.save()


between_six_twelve(coords)
# test(coords)

conn.close()