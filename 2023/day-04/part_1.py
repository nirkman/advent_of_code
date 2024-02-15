#!/usr/bin/env python3

# Advent of Code 2023
# Day 4, Part 1

import re
import time
from datetime import datetime, timedelta

starttime = time.time()

file = "input.txt"

points = 0

with open(file) as input:
    
    for line in input:
        
        value = 0
        possible = True
    
        winning_numbers = re.findall(r"(\d+)", line[10:39])
        my_numbers = re.findall(r"(\d+)", line[42:116])
        
        for my_number in my_numbers:
            if my_number in winning_numbers:
                if value:
                    value *= 2
                else:
                    value = 1
        points += value        
        
print("")  
print("Points.......: " + str(points))  
print("Total runtime..: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")


'''
Points.......: 24160
Total runtime..: 0.002 seconds.
'''