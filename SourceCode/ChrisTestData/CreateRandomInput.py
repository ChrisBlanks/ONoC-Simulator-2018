#!/usr/bin/env python3
"""
Programmer: Chris B
Purpose: Splits a Neural Network input file into test and train data files.
This split is determined by comparing a threshold with a random float value, so
the proportions will probably not be even.
"""

import random
import time

import os
import sys


if len(sys.argv) > 1:
	desired_dir_path = sys.argv[1]
else:
	desired_dir_path = os.getcwd()

assert os.path.isdir(desired_dir_path), "Not a directory for data"

files = os.listdir(desired_dir_path)
OUTPUT_DIR = "NN_Input/"
THRESHOLD = 0.5

random.seed() #generates a seed based on time or OS nondeterministic process
line_count = 1
for file in files:
	if ".csv" in file:
		data_train = OUTPUT_DIR+ "train_"+file.replace(".out","")
		data_test = OUTPUT_DIR+"test_"+ file.replace(".out","")
		with open(file,"r") as orig_data_file:
			with open(data_train,"w+") as train_data_csv:
				with open(data_test,"w+") as test_data_csv:
					for line in orig_data_file:
						if line_count == 1:                  #copies original file header into new files
							train_data_csv.write(line)
							test_data_csv.write(line)
							line_count+=1                    #no more counting
							continue                         #go to next loop
						
						random_num = random.random()         #random float between 0 and 1
						if random_num > THRESHOLD:
							train_data_csv.write(line)
						else:
							test_data_csv.write(line)





						


