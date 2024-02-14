#!/usr/bin/env python3

# Advent of Code 2023
# Day 1, Part 2

import os
import re
import time
from datetime import datetime, timedelta

starttime = time.time()

file = "input.txt"

calibrations = []
words = {
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9
}  

with open(file) as input:
    
    for line in input:
        line = line.strip(os.linesep)
        
        #RESEARCH: '(?=...)' RegEx lookaheads, via Reddit. Deals with situations like "eightwo"
        numbers = re.findall(r'(?=(\d+|one|two|three|four|five|six|seven|eight|nine))', line)

        print("")
        print(line)
        print(numbers)
        
        try:
            first = words[numbers[0]]
        except:
            first = numbers[0][0]
       
        try:
            last = words[numbers[-1]]
        except:
            last = numbers[-1][-1]
            
        calibration = int( str(first) + str(last) )
        print(calibration)
        calibrations.append(calibration)
        
print("")  
print("Calibration Sum..: " + str(sum(calibrations)))  
print("Total runtime....: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")


'''
Calibration Sum..: 54208
Total runtime....: 0.011 seconds.
'''