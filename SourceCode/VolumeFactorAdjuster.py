#!/usr/bin/env python3
"""
Programmer: ChrisB
Purpose:
This script varies the volume factor global variable value within an arbitrary range.
The impact of varying this value will manifest in the runtime/performance value.


Notes:
 > To run this in SublimeREPL, enter the following commands:
	>import sys
	>sys.argv = ["placeholder","Benchmark_Data/16-core/7/flow_freqmine100#1.txt",
				"ParallelFiles/cb_configurations_1000.txt"]
	>import VolumeFactorAdjuster
 
 >The placeholder is needed because the first index is usually the script name, but
  that's not needed in this case
 > The sys.argv arguments can also be defined in this script instead of in the interpreter
"""

import config
import sys

print(str(sys.argv))

for i in range(1,10):
	config.volume = (i)*100  #changes the volume factor each loops
	print("Volume Factor: ",str(config.volume),"\n")
	import Simulation2  #runs the expressions not in a function