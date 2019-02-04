#!/usr/bin/env python3

"""
Programmer: Chris Blanks
Purpose: Plots the performance of the 1000 configuration set with multiple volume vlaues.
"""

import matplotlib.pyplot as plt
import sys
import os


SEARCH_STR = "Performance_flow_freqmine1000"  #string used to differentiat between performance files

cur_dir = os.getcwd()
performance_dir = "/Performance_Counts/"
desired_dir = sys.argv[1]            #directory name for searching

path = cur_dir + performance_dir + desired_dir

assert os.path.exists(path), "\nNot an existing path: {}".format(path)

os.chdir(path)

list_of_files = (os.listdir(os.getcwd()))
list_of_files.sort()



x= []   #volume factor value
y = []  #number of average + good performance results

for file in list_of_files:
	if SEARCH_STR in file:
		print("Parsed volume value for {} : ".format(file) + \
		 file.split("Performance_flow_freqmine1000_cb_configurations_1000_volume_")[1].replace(".txt",""))

		volume_val = int(file.split("Performance_flow_freqmine1000_cb_configurations_1000_volume_")[1].replace(".txt",""))
		with open(file,"r") as data:
			content = data.readlines()[-1]  #grabs latest performance check in file
			print(content)
			temp_str_list = content.split(" ")

			count = 0
			isRelevantCount = False
			for str in temp_str_list:

				if isRelevantCount:
					count = count + int(str)
					isRelevantCount = False

				if str == "Good:" or str == "Average:":
					isRelevantCount = True

			x.append(volume_val)
			y.append(count)

			plt.plot(volume_val,count,'ro') #plot each value pair as a point


#plt.plot(x,y) #plots a line 

plt.xlabel('Volume Factor Values',fontsize=10)
plt.ylabel('Count of Average and Good Classifications',fontsize=10)
plt.title('Performance of Configuration Set With Varying Volume Values')
plt.show() #show plot results