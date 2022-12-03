#!/usr/bin/env python3

# Advent of Code 2022
# Day 2, Part 1 [revised]

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
    
    ME
    X = Rock [1 point]
    Y = Paper [2 points]
    Z = Scissors [3 points]
    
    Loss = 0
    Draw = 3
    Win = 6
'''

shapes = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3
}

outcomes = {
    'A' : {
        'X' : 3,
        'Y' : 6,
        'Z' : 0
    },
    'B' : {
        'X' : 0,
        'Y' : 3,
        'Z' : 6
    },
    'C' : {
        'X' : 6,
        'Y' : 0,
        'Z' : 3
    }
}

with open(file) as input:
            
    for line in input:
        them, me = line.rstrip().split(" ")
        score = shapes[me] + outcomes[them][me]
        total = total + score
        
        
print("")  
print("Score Total: " + str(total))  
print("Total runtime: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")

'''

Score Total: 10595
Total runtime: 0.001 seconds.

'''