#Anheuser-Busch Filler Line 10 Filler Stoppage Data
#objective: to find how long the filler stops, avg stops per day/month, etc.

import time
#begin code execution timing
start_time = time.time()

import L10_filler_stops_fn as fn
print("5% Completed")

tot_mins_stop = 397391
mins_per_day = 1440

#read from excel file
wb2 = fn.file_read()
print("70% Completed")

#indexing dataframe data into variables
filler_speed = fn.index_fn(wb2)
print("75% Completed")

#calculate stops per day
counter_stops, stops_list, stops_list_2 = fn.dump_fn(filler_speed, tot_mins_stop, mins_per_day)
print("90% Completed")
stops_per_day = fn.dump_day_fn(counter_stops, tot_mins_stop, mins_per_day)
fn.save_fn(stops_list_2, stops_list)

#end time
print("100% Completed")
end_time = time.time()
print("Code Executed In:{:.3f}s".format(end_time - start_time))

print("Total Mins Stops: {:.2f} | Avg Mins Stops per Day: {:.2f}".format(counter_stops, stops_per_day))






