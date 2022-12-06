#!/usr/bin/env python3

# Advent of Code 2022
# Day 6, Part 2

import time
from datetime import datetime, timedelta
from textwrap import wrap

starttime = time.time()
#file = "input_test.txt"
file = "input.txt"
position = 0

buffer = []
with open(file) as input:
 
    for line in input:
        
        line = list(line.strip("\n"))
        
        for char in line:
            position += 1
            buffer.append(char)     
            
            if len(buffer) >= 14:
                if len(set(buffer)) == len(buffer):
                    break
                del buffer[0]

            
        
        


print("")  
print("Pointer: " + str(position))  
print("Total runtime: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")

'''

Pointer: 1833
Total runtime: 0.001 seconds.

'''