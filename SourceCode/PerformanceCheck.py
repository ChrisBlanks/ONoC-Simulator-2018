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

def checkPerformance():
	"""Checks the performance of Logger files created from Simulation2.py code. """
	if len(sys.argv) == 2:
		directory = sys.argv[1]
	else:
		directory = os.getcwd()

	assert os.path.exists(directory), "Not an existing directory: {}".format(directory)
	assert os.path.isdir(directory), "Not a directory: {}".format(directory)

	print("Looking in this directory: {}".format(directory))

	files = os.listdir(directory)
	OutputDirectory = os.getcwd() + "/ChrisTestData/Performance_Counts/"

	Logger_files = []
	for file in files:
		if "Logger" in file:
			Logger_files.append(file)

	assert Logger_files, "No Logger files in directory."

	for file in Logger_files:
		full_path =  directory+"/"+file
		good_count = 0
		bad_count = 0
		average_count = 0
		
		with open(full_path,"r") as f:
			lines = f.readlines()
			for line in lines:
				"""
				# Only useful if classification in file is right, which some aren't *sigh*
				if "Classification:" in line:
					line_Strings = line.split(" ")
					classification = line_Strings[-1].strip(" ").strip("\n")
					assert classification != "","No classification." #throws error if no classification

					if classification == "bad":
						bad_count+=1
					elif classification == "good":
						good_count+=1
					elif classification == "average":
						same_count+=1
					else:
						print("Erroneous classification!")
				"""
				if "Runtime:" in line:
					line_Strings = line.split(" ")
					time = line_Strings[-1].strip(" ").strip("\n").strip("seconds")
					assert time != "","No time." #throws error if no classification
					time = float(time) #converts string to float

					if time <= 2.8856e-06:
						good_count+=1
					elif time < 3.0e-6:
						average_count+=1
					elif time >= 3.0e-6:
						bad_count+=1
					else:
						print("Erroneous time")	

		msg = "Counts->  Good: "+ str(good_count) + " Bad: " + str(bad_count) + \
		" Average: " + str(average_count) + "\n"

		performance_check_file = file.replace("Logger","Performance")
		perf_file_path = OutputDirectory +performance_check_file

		with open(perf_file_path,"a+") as out:
			out.write(msg)


if __name__ == "__main__":
	checkPerformance()
