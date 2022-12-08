#!/usr/bin/env python3

# Advent of Code 2022
# Day 8, Part 1

import time
from datetime import datetime, timedelta

starttime = time.time()
#file = "input_test.txt"
file = "input.txt"


def visible_from_the_north(tree, x, y):
    while x > 0:
        x -= 1
        if tree <= forest[x][y]:
            #print("found a bigger tree")
            return False
        
    return True

def visible_from_the_east(tree, x, y):
    while y < len(forest[x])-1:
        y += 1
        if tree <= forest[x][y]:
            return False
        
    return True
    
def visible_from_the_south(tree, x, y):
    while x < len(forest)-1:
        x += 1
        if tree <= forest[x][y]:
            return False
        
    return True
    
def visible_from_the_west(tree, x, y):
    while y > 0:
        y -= 1
        if tree <= forest[x][y]:
            return False
        
    return True


forest = []

with open(file) as input:
    for line in input:
        forest.append(list(line.strip()))
    

visible_trees = 0
for x, row in enumerate(forest):
    for y, tree in enumerate(row):
        # tree = height
        
        if x not in [0, len(row)-1] and y not in [0, len(forest)-1]:
            '''
            print("TREE: " + str(tree), "; X: " + str(x) + "; Y: " + str(y))
            print("+ visible from the north..?", visible_from_the_north(tree, x, y))
            print("+ visible from the east...?", visible_from_the_east(tree, x, y))
            print("+ visible from the south..?", visible_from_the_south(tree, x, y))
            print("+ visible from the west...?", visible_from_the_west(tree, x, y))
            print("")
            '''
            if visible_from_the_north(tree, x, y) or visible_from_the_east(tree, x, y) or visible_from_the_south(tree, x, y) or visible_from_the_west(tree, x, y):
                visible_trees += 1
        else:
            visible_trees += 1

print("")  
print("Visible trees: " + str(visible_trees))  
print("Total runtime: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")

'''

Visible trees: 1792
Total runtime: 0.019 seconds.

'''