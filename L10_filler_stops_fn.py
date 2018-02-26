#import required library modules
import pandas as pd
import math
import datetime
import numpy as np

#read from excel file
def file_read():
	try:
		wb = pd.read_excel('L10_Data.xlsx', sheet_name='Sheet3')
	except IOerror as io:
		print("An error occured trying to read file.", io)
	except:
		print("Unknown error occured")
	print("50% Completed")
	wb2 = pd.DataFrame(wb)
	return wb2

#indexing dataframe data into variables
def index_fn(wb2):
	filler_speed = pd.to_numeric(wb2.iloc[:,1], errors='coerce')
	return filler_speed

#set minutes array and count number of dumps
def dump_fn(filler_speed, tot_mins_stop, mins_per_day):
	stops_list_2 = [0]*tot_mins_stop
	counter_stops = 0
	for i in range(0, tot_mins_stop):
			if filler_speed[i] == 0:
				stops_list_2[i] = 1
				counter_stops += 1

	stops_list = [0]*math.floor(tot_mins_stop/mins_per_day)
	counter_hours = 0
	counter_hours_2 = 1440
	for j in range(0,math.floor(tot_mins_stop/mins_per_day)):
		stops_list[j] = sum(stops_list_2[counter_hours:counter_hours_2])
		# 24*counter_hours:24*counter_hours_2
		counter_hours += 1440
		counter_hours_2 += 1440
	print(sum(stops_list))
	return counter_stops, stops_list, stops_list_2

def dump_day_fn(counter_stops, tot_mins_stop, mins_per_day):
	stops_per_day = (counter_stops / tot_mins_stop) * mins_per_day
	return stops_per_day

def save_fn(stops_list_2, stops_list):
	try:
		print("Saving to file...")
		file = np.savetxt("stops_list.csv", stops_list, fmt = "%s", delimiter = ",", header = "Mins Filler Stops Per Day", comments = "#")
		file2 = np.savetxt("stops_list2.csv", stops_list_2, fmt = "%s", delimiter = ",", header = "Mins Filler Stops", comments = "#")
		return True
	except IOError:
		raise IOError ("Error writing to file: 'stops_list.csv'.")
	except Exception:
		raise Exception ("Unknown error writing to file: 'stops_list.csv'.")