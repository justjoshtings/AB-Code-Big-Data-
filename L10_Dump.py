#Anheuser-Busch Filler Line 10 9 Months Dump Data
#Objective of this script is to show filler dump data for a period of 9 months 
#test

import time
#begin code execution timing
start_time = time.time()

#import required libraries
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib.ticker as ticker
import math
import datetime
from openpyxl import load_workbook

print("5% Completed")

#read from excel file
try:
	wb = pd.read_excel('L10_Data.xlsx', sheet_name='Sheet2')
except IOerror as io:
	print("An error occured trying to read file.", io)
except:
	print("Unknown error occured")
print("50% Completed")
wb2 = pd.DataFrame(wb)

#indexing dataframe data into variables
filler_temp = pd.to_numeric(wb2.iloc[:,1], errors='coerce')
beer_pipe_temp = pd.to_numeric(wb2.iloc[:,2], errors='coerce')
print("55% Completed")
warm_bowl_dump = pd.to_numeric(wb2.iloc[:,3], errors='coerce')

print("65% Completed")

#set minutes array and count number of dumps
py_date = [0]*(397391)
counter_dump = 0
times_o_dump = [0]*3347
j = 0
for i in range(0,397391):
	py_date[i] = i
	if warm_bowl_dump[i] == 1:
		counter_dump += 1
		times_o_dump[j] = i
		j += 1
print("75% Completed")
num_of_days = (397391/(1440))
dumps_per_day = counter_dump/num_of_days

print("80% Completed")

#plot data
fig = plt.figure()
ax1 = fig.add_subplot(111)
for xc in times_o_dump: #plotting vertical lines for instances of dumping
    plt.vlines(x=xc,ymin=0, ymax=250, color='#50CD95', zorder=3, alpha=0.025)
ax1.scatter(py_date,beer_pipe_temp,s=10, c='#FB5633', marker="o", label='Pipe Temp.', zorder=1, alpha=0.5)
ax1.scatter(py_date,filler_temp,s=10, c='#2375CC', marker="s", label='Filler Temp.', zorder=1)
ax1.scatter(py_date,warm_bowl_dump*25,s=10, c='#50CD95', marker="|", label='Dumping', alpha=0.5, zorder=2)
plt.title('Beer Pipe Temperature and Dump Data vs Time (9 Months)', fontsize = "16")
print("90% Completed")
plt.xlabel('Time (mins) for 9 Months Period', fontsize="12")
plt.ylabel(r'Temperature ($^\circ$F)', fontsize="12")
plt.legend(loc='upper left');
plt.ylim(0,250)
ax1.get_xaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

# #end time
print("100% Completed")
end_time = time.time()
print("Code Executed In:{:.3f}s".format(end_time - start_time))

#show results
print("Number of times dumped: {:,d}\nAverage number of dumps per day: {:,.2f} over a period of {:,.2f} days".format(counter_dump, dumps_per_day, num_of_days))
plt.show()
