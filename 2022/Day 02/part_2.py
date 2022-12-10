#!/usr/bin/env python3

# Advent of Code 2022
# Day 2, Part 2

import time
from datetime import datetime, timedelta

starttime = time.time()

file = "input.txt"

score = 0
total = 0

'''
    A = Rock [1 point]
    B = Paper [2 points]
    C = Scissors [3 points]
    
    X = Lose
    Y = Draw
    Z = Win
    
    Loss = 0
    Draw = 3
    Win = 6
'''


shapes = {
    'R' : 1,
    'P' : 2,
    'S' : 3
}

outcomes = {
    'X' : 0,
    'Y' : 3,
    'Z' : 6
}

def battle(result, them):
    
    if them == 'A': #rock
        if result == 'X': #lose
            me = 'S' 
        elif result == 'Y': #draw
            me = 'R'
        elif result == 'Z': #win
            me = 'P'
    elif them == 'B': #paper
        if result == 'X': #lose
            me = 'R'
        elif result == 'Y': #draw
            me = 'P'
        elif result == 'Z': #win
            me = 'S'
    elif them == 'C': #scissors
        if result == 'X': #lose
            me = 'P'
        elif result == 'Y': #draw
            me = 'S'
        elif result == 'Z': #win
            me = 'R'
    return me
    

with open(file) as input:
    for line in input:
        them, result = line.rstrip().split(" ")
        me = battle(result, them)
        score = shapes[me] + outcomes[result]
        total = total + score

print("")  
print("Score Total: " + str(total))  
print("Total runtime: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")

'''

Score Total: 9541
Total runtime: 0.002 seconds.

'''