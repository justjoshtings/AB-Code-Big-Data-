import sqlite3
import pandas as pd

conn = sqlite3.connect('filler.db') #Has table: filler

c = conn.cursor()

def get_lines(num):
	# c.execute("SELECT * FROM filler LIMIT :num", {'num':num})
	# return c.fetchall()
	return print(pd.read_sql_query("SELECT * FROM filler LIMIT ?", conn, params=(num, )))

def get_headers():
	# c.execute("PRAGMA table_info(filler)")
	# return c.fetchall()
	return print(pd.read_sql_query("PRAGMA table_info(filler)", conn))

def num_dumps():
	return print(pd.read_sql_query("SELECT * FROM filler WHERE 'Warm Bowl Dump Y/N' = 1 LIMIT 10", conn))

# get_lines(3)
# num_dumps()
# 



conn.close()