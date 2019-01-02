import config
import sys

print(str(sys.argv))

for i in range(1,5):
	config.volume = i*100  #changes the volume factor each loops
	print("Volume Factor: ",str(config.volume),"\n")
	import Simulation2  #runs the expressions not in a function