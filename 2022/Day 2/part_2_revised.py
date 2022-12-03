#!/usr/bin/env python3

# Advent of Code 2022
# Day 2, Part 2 [revised]

import os, time
from datetime import datetime, timedelta

starttime = time.time()

file = "input.txt"

score = 0
total = 0

'''
    THEM
    A = Rock
    B = Paper
    C = Scissors
    
    RESULT
    X = Lose 
    Y = Draw
    Z = Win
    
    ME
    Rock = 1 point
    Paper = 2 points
    Scissors = 3 points
'''

results = {
    'X' : 0,
    'Y' : 3,
    'Z' : 6
}

me = {
    'A' : {
        'X' : 3,
        'Y' : 1,
        'Z' : 2
    },
    'B' : {
        'X' : 1,
        'Y' : 2,
        'Z' : 3
    },
    'C' : {
        'X' : 2,
        'Y' : 3,
        'Z' : 1
    }
}

with open(file) as input:
    for line in input:
        them, result = line.rstrip().split(" ")
        score = results[result] + me[them][result]
        total = total + score

print("")  
print("Score Total: " + str(total))  
print("Total runtime: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")

'''

Score Total: 9541
Total runtime: 0.001 seconds.

'''