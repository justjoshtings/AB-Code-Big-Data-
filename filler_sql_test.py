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

avg_fault_duration(coords)
most_occurances(coords)

conn.close()