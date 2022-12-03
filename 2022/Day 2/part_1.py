#!/usr/bin/env python3

# Advent of Code 2022
# Day 2, Part 1

import os, time
from datetime import datetime, timedelta

starttime = time.time()

file = "input.txt"

score = 0
total = 0

'''
    A = Rock [1 point]
    B = Paper [2 points]
    C = Scissors [3 points]
    
    X = Rock
    Y = Paper
    Z = Scissors
    
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
    'L' : 0,
    'D' : 3,
    'W' : 6
}

def battle(me, them):
    
    if them == 'A':
        if me == 'X':
            result = 'D'
        elif me == 'Y':
            result = 'W'
        elif me == 'Z':
            result = 'L'
    elif them == 'B':
        if me == 'X':
            result = 'L'
        elif me == 'Y':
            result = 'D'
        elif me == 'Z':
            result = 'W'
    elif them == 'C':
        if me == 'X':
            result = 'W'
        elif me == 'Y':
            result = 'L'
        elif me == 'Z':
            result = 'D'
    return result

with open(file) as input:
            
    for line in input:
        them, me = line.rstrip().split(" ")
        result = battle(me, them)
        score = shapes[me] + outcomes[result]
        total = total + score

print("")  
print("Score Total: " + str(total))  
print("Total runtime: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")

'''

Score Total: 10595
Total runtime: 0.002 seconds.

'''