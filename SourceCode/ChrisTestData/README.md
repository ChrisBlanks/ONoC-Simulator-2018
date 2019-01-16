# README.md
## Author: Chris Blanks
## Heading 2  Date: 1/16/2019

** This folder contains the data that was acquired after adapting the existing code base that I have made to this project during the winter break of the 2018-2019 year. The following are the most significant adaptions/additions:**
---

** Adaptation to the Simulation2.py script (Located in the SourceCode directory)**
	> * Logger files are now created with information regarding the performance of a configuration in the simulator
	> * The "writeForNeuralNet" function will output data to the ChrisTestData directory now if the "config.isVolumeSpecific" global variable is set in the "config.py" script beforehand
	> * If "config.isVolumeSpecific" is true, then the configuration analysis files have their volume factor volume appended to their names


** PerformanceCheck.py (Located in the SourceCode directory) **
	> * Counts the occurrences of good, bad, and average performances of "Simulation2.py" output logger files
	> * A single command line argument can be passed to indicate the desired directory; All "Logger" files will be checked within that directory 
	> * Output directory will be based on the result of "os.getcwd()", so it is recommended to run this script in the SourceCode directory or change output path

** VolumeFactorAdjuster.py (Located in the SourceCode directory) **
	> * Varies the volume factor value specified in the "config.py" script and runs the main() of "Simulation2.py" with that new value.
	> * The varyVolumeFactor() will take bounds, an offset, and a scaling value for changing the volume, but there are defaults set

** CreateRandomInput.py (Located in this directory) **
	> * Splits a Neural Network input file (after DataConverter is invoked on it) into training and testing csv files
	> * Uses a random number and conditional statement for determining whether each line in the original input file goes into either the train or test files
	> * Takes a single command line argument for specifying the directory path for finding ".csv" files to split

** premade_estimator.py **
	> * more command line arguments were added to specify the train and test data files
	> * The directory for saving the model was changed to ChrisTestData/Models
	> * Alterations to the neural network structure
