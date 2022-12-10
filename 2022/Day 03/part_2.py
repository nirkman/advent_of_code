#!/usr/bin/env python3

# Advent of Code 2022
# Day 3, Part 2

import time
from datetime import datetime, timedelta

starttime = time.time()

file = "input.txt"

total = 0

# CONVERT CHARACTER TO ASCII VALUE
def character_to_number(character):

    # LOWERCASE
    number = ord(character) - 96
    
    # UPPERCASE
    if number < 0:
        number = number + 58
    return number

with open(file) as rucksacks:

    line_count = 0
    group = []
    for rucksack in rucksacks:
        
        line_count += 1
        group.append(rucksack.strip())
        
        if line_count == 3:    
            badges = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
            total = total + character_to_number(badges)
            group = []
            line_count = 0

print("")  
print("Sum of Badges: " + str(total))  
print("Total runtime: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")

'''

Sum of Badges: 2716
Total runtime: 0.001 seconds.

'''