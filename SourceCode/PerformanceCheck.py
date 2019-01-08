#!/usr/bin/env python3
"""
Programmer: ChrisB
Purpose:
This script checks the performance of logger files that hold information
about the volume factor, configuration file, benchmark file, total time, etc.

The script parses the file to make a count of each classification, and it
writes the count for each into a performance file.
"""

import os
import sys


cur_dir = os.getcwd()
files = os.listdir(cur_dir)
OutputDirectory = cur_dir + "/ChrisTestData/"

Logger_files = []
for file in files:
	if "Logger" in file:
		Logger_files.append(file)

for file in Logger_files:
	full_path =  cur_dir+"/"+file
	print(full_path)
	good_count = 0
	bad_count = 0
	same_count = 0
	
	with open(full_path,"r") as f:
		lines = f.readlines()
		for line in lines:
			if "Classification:" in line:
				line_Strings = line.split(" ")
				classification = line_Strings[-1].strip(" ").strip("\n")
				assert classification != "","No classification." #throws error if no classification

				if classification == "bad":
					bad_count+=1
				elif classification == "good":
					good_count+=1
				elif classification == "same":
					same_count+=1
				else:
					print("Erroneous classification!")

	msg = "Counts->  Good: "+ str(good_count) + " Bad: " + str(bad_count) + \
	" Average: " + str(same_count) + "\n"

	performance_check_file = file.replace("Logger","Performance")
	perf_file_path = OutputDirectory +performance_check_file
	with open(perf_file_path,"a+") as out:
		out.write(msg)


