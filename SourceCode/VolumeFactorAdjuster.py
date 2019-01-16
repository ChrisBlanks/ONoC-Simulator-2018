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
sys.argv = ["placeholder","Benchmark_Data/16-core/7/flow_freqmine7000.txt","ParallelFiles/cb_configurations_1000.txt"]

import config
import Simulation2 as Sim2

def varyVolumeFactor(UPPER=11,LOWER=1,OFFSET=0,SCALE=10):
	"""Varies the Volume factor in the Simulation. UPPER & LOWER define an integer range, and each
	value in that range will be multiplied by SCALE and have OFFSET added to it."""
	
	print( "Command Line Args: {}".format( str(sys.argv) ) )

	for i in range(LOWER,UPPER):
		config.volume = (i*SCALE) + OFFSET  #changes the volume factor each loops
		print( "Volume Factor: {} \n".format( str(config.volume) ) )
		Sim2.main()

		
if __name__ == "__main__":
	varyVolumeFactor()