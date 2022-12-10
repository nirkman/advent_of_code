#!/usr/bin/env python3

# Advent of Code 2022
# Day 8, Part 2

import time
from datetime import datetime, timedelta

starttime = time.time()
file = "input_test.txt"
file = "input.txt"


def view_to_the_north(tree, x, y):
    view = 0
    while x > 0:
        x -= 1
        view += 1
        if tree <= forest[x][y]:
            return view
        
    return view

def view_to_the_east(tree, x, y):
    view = 0
    while y < len(forest[x])-1:
        y += 1
        view += 1
        if tree <= forest[x][y]:
            return view
        
    return view
        
def view_to_the_south(tree, x, y):
    view = 0
    while x < len(forest)-1:
        x += 1
        view += 1
        if tree <= forest[x][y]:
            return view
        
    return view
        
def view_to_the_west(tree, x, y):
    view = 0
    while y > 0:
        view += 1
        y -= 1
        if tree <= forest[x][y]:
            return view
        
    return view

forest = []

with open(file) as input:
    for line in input:
        forest.append(list(line.strip()))
    

highest_scenic_score = 0
for x, row in enumerate(forest):
    for y, tree in enumerate(row):
        # tree = height
        if x not in [0, len(row)-1] and y not in [0, len(forest)-1]:
            print(view_to_the_north(tree, x, y), view_to_the_east(tree, x, y), view_to_the_south(tree, x, y), view_to_the_west(tree, x, y))
            current_scenic_score = view_to_the_north(tree, x, y) * view_to_the_east(tree, x, y) * view_to_the_south(tree, x, y) * view_to_the_west(tree, x, y)
            if current_scenic_score > highest_scenic_score:
                highest_scenic_score = current_scenic_score


print("")  
print("Highest Scenic Score: " + str(highest_scenic_score))  
print("Total runtime: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")

'''

Highest Scenic Score: 334880
Total runtime: 0.077 seconds.

'''