#Anheuser-Busch Filler Line 10 9 Monthly Dump Data
#Objective of this script is to show monthly filler dump data for a period of 9 months 
#test

import time
#begin code execution timing
start_time = time.time()

import L10_Dump_Monthly_fn as fn

tot_mins_stop = 397391
mins_per_day = 1440
month_num = fn.which_month()
print("5% Completed")

#read from excel file
wb2, wb2_stops = fn.file_read()

#indexing dataframe data into variables
print("55% Completed")
filler_temp, beer_pipe_temp, warm_bowl_dump, filler_speed = fn.index_fn(wb2, wb2_stops)
print("65% Completed")

mins_in_month = fn.monthly_fn(397391, month_num)

#set minutes array and count number of dumps
print("70% Completed")
filler_temp_new, beer_pipe_temp_new, warm_bowl_dump_new = fn.split_fn(filler_temp, beer_pipe_temp, warm_bowl_dump, mins_in_month, month_num)
py_date, counter_dump, num_of_days, dumps_per_day = fn.split_fn_2(mins_in_month, warm_bowl_dump_new)
print("75% Completed")
times_o_dump = fn.times_o_dump_fn(mins_in_month, warm_bowl_dump_new, counter_dump)
print("80% Completed")
stops_list_2 = fn.dump_fn(filler_speed, tot_mins_stop, mins_per_day)
print("85% Completed")

#plot data
fn.plot_fn(py_date, beer_pipe_temp_new, filler_temp_new, warm_bowl_dump_new, month_num, times_o_dump, stops_list_2)

# #end time
print("100% Completed")
end_time = time.time()
print("Code Executed In:{:.3f}s".format(end_time - start_time))

#show results
print("Month {:d}\nNumber of minutes dumped: {:,d}\nAverage total minutes of dumps per day: {:,.2f} over a period of {:,.2f} days".format(month_num, counter_dump, dumps_per_day, num_of_days))
