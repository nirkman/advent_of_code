#!/usr/bin/env python3

# Advent of Code 2022
# Day 3, Part 1 [revised]

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
    for rucksack in rucksacks:
        #                            slice string beg to half of string length  slice string half of string length to end
        compartment1, compartment2 = list(rucksack[:len(rucksack)//2].strip()), list(rucksack[len(rucksack)//2:].strip())
        
        # convert strings to sets and find intersection - assume single result
        misplaced_item = list(set(compartment1) & set(compartment2))[0]
        
        # convert misplaced item to number and add to total
        total = total + character_to_number(misplaced_item)

print("")  
print("Sum of Priorities: " + str(total))  
print("Total runtime: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")

'''

Sum of Priorities: 7967
Total runtime: 0.001 seconds.

'''