#import required library modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib.ticker as ticker
import math
import datetime

#read from excel file
def file_read():
	try:
		wb = pd.read_excel('L10_Data.xlsx', sheet_name='Sheet2')
		wb_stops = pd.read_excel('L10_Data.xlsx', sheet_name='Sheet3')
	except IOerror as io:
		print("An error occured trying to read file.", io)
	except:
		print("Unknown error occured")
	print("50% Completed")
	wb2 = pd.DataFrame(wb)
	wb2_stops = pd.DataFrame(wb_stops)
	return wb2, wb2_stops

#indexing dataframe data into variables
def index_fn(wb2, wb2_stops):
	filler_temp = pd.to_numeric(wb2.iloc[:,1], errors='coerce')
	beer_pipe_temp = pd.to_numeric(wb2.iloc[:,2], errors='coerce')
	warm_bowl_dump = pd.to_numeric(wb2.iloc[:,3], errors='coerce')
	filler_speed = pd.to_numeric(wb2_stops.iloc[:,1], errors='coerce')
	return filler_temp, beer_pipe_temp, warm_bowl_dump, filler_speed

#divide into monthly
def monthly_fn(num_mins, month_num):
	mins_in_month = math.ceil(num_mins / 9)
	if month_num == 9:
		mins_in_month = num_mins - (mins_in_month*8) #only for 9th month
	else: 
		pass
	return mins_in_month

def which_month():
	try:
		month_num = int(input("Enter which month (1 to 9): "))
	except ValueError:
		raise ValueError ("Enter only integers!")
	except Exception:
		raise Exception ("Unknown error in entering month.")
	return month_num

def split_fn(filler_temp, beer_pipe_temp, warm_bowl_dump, mins_in_month, month_num):
	filler_temp_new = [0]*mins_in_month
	beer_pipe_temp_new = [0]*mins_in_month
	warm_bowl_dump_new = [0]*mins_in_month
	j = 0
	for i in range(((month_num-1)*mins_in_month), (month_num*mins_in_month)):
		filler_temp_new[j] = filler_temp[i]
		beer_pipe_temp_new[j] = beer_pipe_temp[i]
		warm_bowl_dump_new[j] = warm_bowl_dump[i]
		j += 1
	return filler_temp_new, beer_pipe_temp_new, warm_bowl_dump_new

#set minutes array and count number of dumps
def split_fn_2(mins_in_month, warm_bowl_dump_new):
	py_date = [0]*(mins_in_month)
	counter_dump = 0
	# times_o_dump = [0]*3347
	j = 0
	for i in range(0,mins_in_month):
		py_date[i] = i
		if warm_bowl_dump_new[i] == 1:
			counter_dump += 1
			# times_o_dump[j] = i
			j += 1
	num_of_days = (mins_in_month/(1440))
	dumps_per_day = counter_dump/num_of_days
	return py_date, counter_dump, num_of_days, dumps_per_day

def times_o_dump_fn(mins_in_month, warm_bowl_dump_new, counter_dump):
	j = 0
	times_o_dump = [0]*counter_dump
	for i in range(0,mins_in_month):
		if warm_bowl_dump_new[i] == 1:
			times_o_dump[j] = i
			j += 1
	return times_o_dump

def dump_fn(filler_speed, tot_mins_stop, mins_per_day):
	stops_list_2 = [0]*tot_mins_stop
	counter_stops = 0
	for i in range(0, tot_mins_stop):
			if filler_speed[i] == 0:
				stops_list_2[i] = 1
				counter_stops += 1
	return stops_list_2

#plot graphs
def plot_fn(py_date, beer_pipe_temp_new, filler_temp_new, warm_bowl_dump_new, month_num, times_o_dump, stops_list_2):
	fig = plt.figure()
	ax1 = fig.add_subplot(111)
	plt.vlines(x=0,ymin=0, ymax=0, color='#50CD95', zorder=3, alpha=1, label = "Dumping")
	for xc in times_o_dump: #plotting vertical lines for instances of dumping
	    plt.vlines(x=xc,ymin=0, ymax=250, color='#50CD95', zorder=3, alpha=0.075)
	plt.vlines(x=0,ymin=0, ymax=0, color='#FFA523', zorder=3, alpha=1, label = "Filler Stops")
	for xc in stops_list_2: #plotting vertical lines for instances of filler stopping
	    plt.vlines(x=xc,ymin=0, ymax=250, color='#FFA523', zorder=4, alpha=0.1)
	ax1.scatter(py_date,beer_pipe_temp_new,s=4, c='#FB5633', marker="o", zorder=2, alpha=0.2,label='Pipe Temp.')
	ax1.scatter(py_date,filler_temp_new,s=4, c='#2375CC', marker="+", alpha = 0.7, zorder=1,label='Filler Temp.')
	plt.title('Beer Pipe Temperature and Dump Data vs Time (Month {:d})'.format(month_num), fontsize = "16")
	print("90% Completed")
	plt.xlabel('Time (mins) for 1 Month Period', fontsize="12")
	plt.ylabel(r'Temperature ($^\circ$F)', fontsize="12")
	plt.legend(loc='upper left');
	plt.ylim(0,250)
	ax1.get_xaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
	plt.show()

#testing 
fdfd
