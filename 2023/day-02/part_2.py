#!/usr/bin/env python3

# Advent of Code 2023
# Day 2, Part 2

import re
import time
from datetime import datetime, timedelta

starttime = time.time()

file = "input.txt"

games = []

with open(file) as input:
    
    for line in input:
        
        game = int(re.findall(r"Game (\d+):", line)[0])
        
        reds = re.findall(r"(\d+) red", line)
        reds = [int(x) for x in reds]
        red = max(reds)

        greens = re.findall(r"(\d+) green", line)
        greens = [int(x) for x in greens]
        green = max(greens)
        
        blues = re.findall(r"(\d+) blue", line)
        blues = [int(x) for x in blues]
        blue = max(blues)
        
        games.append(red * green * blue)        

        
print("")  
print("Game Sum.......: " + str(sum(games)))  
print("Total runtime..: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")


'''
Game Sum.......: 70924
Total runtime..: 0.002 seconds.
'''