#!/usr/bin/env python3

# Advent of Code 2023
# Day 1, Part 1

import re
import time
from datetime import datetime, timedelta

starttime = time.time()

file = "input.txt"

calibrations = []

with open(file) as input:
    
    for line in input:
        numbers = str("".join(re.findall(r"\d+", line)))
        print(numbers)
        calibration = int( str(numbers[0]) + str(numbers[-1]))
        print(calibration)
        calibrations.append(calibration)

print("")  
print("Calibration Sum..: " + str(sum(calibrations)))  
print("Total runtime....: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")


'''
Calibration Sum..: 54940
Total runtime....: 0.005 seconds.
'''