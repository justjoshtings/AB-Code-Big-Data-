import numpy as np
import pandas as pd
from pandas import ExcelWriter

class Process:
	def __init__(self, name, time):
		self.__name = name
		self.__time = time
	
	def set_name(self, name):
		self.__name = name

	def set_time(self, time):
		self.__time = time

	def get_name(self):
		return self.__name

	def get_time(self):
		return self.__time

	def __str__(self):
		return "Process Name: {} | Processing Time: {}".format(self.get_name(), self.get_time())

class Buffer:
	def __init__(self, name, time, rate, capacity): #name, minutes, cans/minute, % of area
		self.__name = name
		self.__time = time
		self.__rate = rate
		self.__capacity = capacity
	
	def set_name(self, name):
		self.__name = name

	def set_time(self, time):
		self.__time = time

	def set_rate(self, rate):
		self.__rate = rate

	def set_capacity(self, capacity):
		self.__capacity = capacity

	def get_name(self):
		return self.__name

	def get_time(self):
		return self.__time

	def get_rate(self):
		return self.__rate

	def get_capacity(self):
		return self.__capacity

	def __str__(self):
		return "Buffer Name: {} | Buffering Time: {} | Rate: {} | Capacity: {}%".format(self.get_name(), self.get_time(), self.get_rate(), self.get_capacity())

# class TruckToLoader(Buffer):
# 	def __init__(self, time, rate, capacity): #name, minutes, cans/minute, % of area
# 		Buffer.__init__('Cans: Truck to Loader', time, rate, capacity)
# 		self.__time = time
# 		self.__rate = rate
# 		self.__capacity = capacity

# 	def set_time(self, time):
# 		self.__time = time

# 	def set_rate(self, rate):
# 		self.__rate = rate

# 	def set_capacity(self, capacity):
# 		self.__capacity = capacity

# 	def get_time(self):
# 		return self.__time

# 	def get_rate(self):
# 		return self.__rate

# 	def get_capacity(self):
# 		return self.__capacity

def data_enter_02():
	num_processes = 2
	num_buffers = 2
	df_p = pd.DataFrame(columns=['Process Name', 'Processing Time'])
	for i in range(num_processes):
		print("----------------------------\nProcess Number {}:\n----------------------------".format(i+1))
		name = str(input("Process name: "))
		time = float(input("Process time: "))
		df_p.loc[i] = [name, time]
	df_b = pd.DataFrame(columns=['Buffer Name', 'Buffering Time', 'Buffering Rate', 'Buffer Capacity'])
	for i in range(num_buffers):
		print("----------------------------\nBuffer Number {}:\n----------------------------".format(i+1))
		name = str(input("Buffer name: "))
		time = float(input("Buffer time: "))
		rate = float(input("Buffering rates: "))
		capacity = float(input("Buffer capacity: "))
		df_b.loc[i] = [name, time, rate, capacity]
	writer = ExcelWriter('AB_processes.xlsx')
	df_p.to_excel(writer, 'Processes')
	df_b.to_excel(writer, 'Buffers')
	writer.save()
	return

data_enter_02()



