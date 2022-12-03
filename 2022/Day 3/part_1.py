#!/usr/bin/env python3

# Advent of Code 2022
# Day 3, Part 1

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
    
# THIS ASSUMES A SINGLE INTERSECTION
def intersection(list1, list2):
    for item in list1:
        if item in list2:
            return item


with open(file) as rucksacks:
    for rucksack in rucksacks:
        compartment1, compartment2 = list(rucksack[:len(rucksack)//2]), list(rucksack[len(rucksack)//2:])
        misplaced_item = intersection(compartment1, compartment2)
        total = total + character_to_number(misplaced_item)

print("")  
print("Sum of Priorities: " + str(total))  
print("Total runtime: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")

'''

Sum of Priorities: 7967
Total runtime: 0.003 seconds.

'''