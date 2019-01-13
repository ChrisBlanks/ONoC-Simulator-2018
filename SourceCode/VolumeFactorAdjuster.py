#!/usr/bin/env python3
"""
Programmer: ChrisB
Purpose:
This script varies the volume factor global variable value within an arbitrary range.
The impact of varying this value will manifest in the runtime/performance value.


Notes:
 > Supply commandline arguments in sublime project file (benchmark path & config path)
 > To run this in SublimeREPL, enter the following commands:
	>import sys
	>sys.argv = ["placeholder","Benchmark_Data/16-core/7/flow_freqmine1000.txt",
				"ParallelFiles/cb_configurations_1000.txt"]
	>import VolumeFactorAdjuster
 
 >The placeholder is needed because the first index is usually the script name, but
  that's not needed in this case
 > The sys.argv arguments can also be defined in this script instead of in the interpreter
"""


import sys
sys.argv = ["placeholder","Benchmark_Data/16-core/7/flow_freqmine2000.txt","ParallelFiles/cb_configurations_1000.txt"]

import config
import Simulation2 as Sim2

print("Command Line Args: " +str(sys.argv))

UPPER = 10
LOWER = 1
for i in range(LOWER,UPPER):
	config.volume = (i*10)  #changes the volume factor each loops
	print("Volume Factor: ",str(config.volume),"\n")
	Sim2.main()
	