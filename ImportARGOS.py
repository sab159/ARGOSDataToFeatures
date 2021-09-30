##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2020
## Author: sophia.bryson@duke.edu (for ENV859)
##---------------------------------------------------------------------

# Import modules
import sys, os, arcpy #useful overall modules for general use

# Set input variables (Hard-wired)
inputFile = 'V:\\ARGOSTracking\\Data\\ARGOSData\\1997dg.txt'
outputFC = 'V:\\ARGOSTracking\\Scratch\\ARGOStrack.shp'

#%% Construct a while loop to iterate through all lines in the datafile
# Open the ARGOS data file for reading
inputFileObj = open(inputFile,'r')

# Get the first line of data, so we can use a while loop
lineString = inputFileObj.readline()

# Start the while loop (using a while loop for memory efficiency) - read one line at a time
while lineString:
    
    # Set code to run only if the line contains the string "Date: "
    if ("Date :" in lineString):
        
        # Parse the line into a list
        lineData = lineString.split()
        
        # Extract attributes from the datum header line
        tagID = lineData[0]
        date = lineData[3]
        time = lineData[4]
        loc_class = lineData[7]
        
        # Extract location info from the next line - advances one line
        line2String = inputFileObj.readline()
        
        # Parse the line into a list
        line2Data = line2String.split()
        
        # Extract the date we need to variables
        obsLat = line2Data[2]
        obsLon= line2Data[5]
        
        # Print results to see how we're doing
        print (f"{tagID} Lat: {obsLat}, Long: {obsLon} at {time} on {date}, LC = {loc_class}")
        
    # Move to the next line so the while loop progresses
    lineString = inputFileObj.readline()
    
#Close the file object
inputFileObj.close()