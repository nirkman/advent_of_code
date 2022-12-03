#!/usr/bin/env python3

# Advent of Code 2022
# Day 1, Part 1

import os, time
from datetime import datetime, timedelta

starttime = time.time()

file = "input.txt"

elf = []
highest_calories = 0

with open(file) as input:
    
    for line in input:
        if line == os.linesep:
            current_calories = sum(elf)
            if current_calories > highest_calories:
                highest_calories = current_calories
            elf = []
        else:
            elf.append(int(line.rstrip()))

print("")  
print("Highest Calories: " + str(highest_calories))  
print("Total runtime: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")

'''

Highest Calories: 69310
Total runtime: 0.001 seconds.

'''