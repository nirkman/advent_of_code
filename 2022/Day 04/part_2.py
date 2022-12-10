#!/usr/bin/env python3

# Advent of Code 2022
# Day 4, Part 2

import time
from datetime import datetime, timedelta

starttime = time.time()
file = "input.txt"
total = 0
debug = False

def padding(number):
    if number < 10:
        padding = "."
    else:
        padding = ".."
    return padding

with open(file) as input:

    for line in input:
        
        string1, string2 = line.strip().split(",")

        list1_start, list1_end = map(int,string1.split("-"))
        list1 = list(range(list1_start, list1_end+1))
        
        list2_start, list2_end = map(int,string2.split("-"))
        list2 = list(range(list2_start, list2_end+1))
        
        intersection = list(set(list1) & set(list2))
        intersection.sort() # sets have no sort order
        
        message = "pass"
        if len(intersection) > 0:
            total += 1
            message = "fail"
        
        #################################################################################
        # DEBUGGING VISUAL AID
        #
        if debug:
            while list1_start < list2_start:
                list2.insert(0, padding(list1_start))
                list1_start += 1
        
            while list2_end > list1_end:
                list1.append(padding(list2_end))
                list1_end += 1
            
            while list2_start < list1_start:
                list1.insert(0, padding(list2_start))
                list2_start += 1
        
            while list1_end > list2_end:
                list2.append(padding(list1_end))
                list2_end += 1

            print(line.replace(",","|").strip() + " [" + message + "]")
            line1_string = ', '.join(map(str, list1))
            print (line1_string.replace(".,", "  ").replace(".", " "))
        
            line2_string = ', '.join(map(str, list2))
            print (line2_string.replace(".,", "  ").replace(".", " "))
            print("")
            print("")
        #
        #################################################################################


print("")  
print("Fully Contained Assignment Pairs: " + str(total))  
print("Total runtime: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")

'''

Fully Contained Assignment Pairs: 891
Total runtime: 0.006 seconds.

'''