#!/usr/bin/env python3

# Advent of Code 2022
# Day 1, Part 2

import os, time
from datetime import datetime, timedelta

starttime = time.time()

file = "input.txt"

elf = []
elves = []
highest_calories = 0

with open(file) as input:
    
    for line in input:
        if line == os.linesep:
            current_calories = sum(elf)
            elves.append(current_calories)
            if current_calories > highest_calories:
                highest_calories = current_calories
            elf = []
        else:
            elf.append(int(line.rstrip()))
            
elves.sort(reverse=True)
highest_three = elves[0] + elves[1] + elves[2]

print("")  
print("Highest Three (total): " + str(highest_three))  
print("Total runtime: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")

'''

Highest Three (total): 206104
Total runtime: 0.001 seconds.

'''