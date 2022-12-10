#!/usr/bin/env python3

# Advent of Code 2022
# Day 3, Part 1 [revised]

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

    for rucksack in rucksacks:
    
        # remove line endings
        rucksack = rucksack.strip()

        # slice string from its start to half of its length; convert to set
        compartment1 = set(rucksack[:len(rucksack)//2]) 
        
        # slice string from half of its length to its end; convert to set
        compartment2 = set(rucksack[len(rucksack)//2:])
        
        # find intersection of both sets and convert back to list
        misplaced_items = list(compartment1 & compartment2)
        
        # convert misplaced item to number and add to total (assumes a single result)
        total = total + character_to_number(misplaced_items[0])


print("")  
print("Sum of Priorities: " + str(total))  
print("Total runtime: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")

'''

Sum of Priorities: 7967
Total runtime: 0.001 seconds.

'''