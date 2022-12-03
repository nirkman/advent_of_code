#!/usr/bin/env python3

# Advent of Code 2022
# Day 3, Part 2 [revised]

import time
from datetime import datetime, timedelta

starttime = time.time()
file = "input.txt"
total = 0


# convert character to ascii value
def character_to_number(character):

    # lowercase
    number = ord(character) - 96
    
    # UPPERCASE
    if number < 0:
        number = number + 58
        
    return number


with open(file) as rucksacks:

    count = 0
    group = []
    
    for rucksack in rucksacks:
        
         # remove line endings
        rucksack = rucksack.strip()
        
        # track group
        count += 1
        group.append(set(rucksack))
        
        if count == 3:
        
            # find intersection of all sets and convert back to list 
            badges = list(group[0] & group[1] & group[2])
            
            # convert badges to number and add to total (assumes a single result)
            total = total + character_to_number(badges[0])
            
            # reset group
            group = []
            count = 0


print("")  
print("Sum of Badges: " + str(total))  
print("Total runtime: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")

'''

Sum of Badges: 2716
Total runtime: 0.001 seconds.

'''