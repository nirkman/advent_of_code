#!/usr/bin/env python3

# Advent of Code 2023
# Day 2, Part 1

import re
import time
from datetime import datetime, timedelta

starttime = time.time()

file = "input.txt"

games = []

with open(file) as input:
    
    for line in input:
        
        possible = True
    
        game = int(re.findall(r"Game (\d+):", line)[0])

        reds = re.findall(r"(\d+) red", line)
        for red in reds:
            if int(red) > 12:
                possible = False
                break
        greens = re.findall(r"(\d+) green", line)
        for green in greens:
            if int(green) > 13:
                possible = False
                break
        blues = re.findall(r"(\d+) blue", line)
        for blue in blues:
            if int(blue) > 14:
                possible = False
                break

        if possible:
            games.append(game)        
            print(reds, greens, blues)
        
print("")  
print("Game Sum.......: " + str(sum(games)))  
print("Total runtime..: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")


'''
Game Sum.......: 2771
Total runtime..: 0.002 seconds.
'''