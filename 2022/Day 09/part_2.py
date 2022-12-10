#!/usr/bin/env python3

# Advent of Code 2022
# Day 9, Part 2

import os, sys, time, json
from datetime import datetime, timedelta


def draw(width, height, knot):
    
    grid = []
    
    while len(grid) <= height:
        row = []
        while len(row) <= width:
            row.append('.')
        grid.append(row)
    grid[knots[knot][1]][knots[knot][0]] = 'T'
    grid[knots[knot-1][1]][knots[knot-1][0]] = 'H'
    
    return grid


def update():

    if mode != 'live':
        time.sleep(.1)
        os.system('clear')
        print('\n'.join([' '.join([str(cell) for cell in row]) for row in grid]))
        print("")
        print("Count: " + str(counter))


def touching(knot):
    
    # same position
    if knots[knot-1][0] == knots[knot][0] and knots[knot-1][1] == knots[knot][1]:
        return True
    
    # same row
    if knots[knot-1][0] == knots[knot][0] and abs(knots[knot-1][1] - knots[knot][1]) < 2:
        return True
    
    # same column
    if abs(knots[knot-1][0] - knots[knot][0]) < 2 and knots[knot-1][1] == knots[knot][1]:
        return True
    
    # diagonal
    if abs(knots[knot-1][0] - knots[knot][0]) < 2 and abs(knots[knot-1][1] - knots[knot][1]) < 2:
        return True
    
    return False


def same(knot):
    return knots[knot-1][0] == knots[knot][0] and knots[knot-1][1] == knots[knot][1]


def move_head(direction=None, distance=None):
    
    if direction and distance:

        i = 1
        while i <= int(distance):
        
            coordinates = str(knots[0][0]) + "," + str(knots[0][1])
            if coordinates in positions:
                grid[knots[0][1]][knots[0][0]] = tracers
            else:
                grid[knots[0][1]][knots[0][0]] = '.'
                        
            if direction == 'U':
                knots[0][1] -= 1
            elif direction == 'R':
                knots[0][0] += 1
            elif direction == 'D':
                knots[0][1] += 1
            elif direction == 'L':
                knots[0][0] -= 1
            
            # tail reacts to movement starting with knot 1
            move_tail(1)
            
            # set head after tail move to keep H on top            
            grid[knots[0][1]][knots[0][0]] = 'H'
            
            update()
            i += 1


def move_tail(knot):

    if knot < len(knots):    
        
        if not same(knot):
            #grid[knots[knot][1]][knots[knot][0]] = "." 
            
            coordinates = str(knots[knot][0]) + "," + str(knots[knot][1])
            if coordinates in positions:
                grid[knots[knot][1]][knots[knot][0]] = tracers
            else:
                grid[knots[knot][1]][knots[knot][0]] = '.'
        
        if not touching(knot):
        
            # move diagonally
            if knots[knot-1][0] != knots[knot][0] and knots[knot-1][1] != knots[knot][1]:
    
                if knots[knot-1][0] > knots[knot][0]:
                   knots[knot][0] += 1
                else:
                   knots[knot][0] -= 1
            
                if knots[knot-1][1] > knots[knot][1]:
                   knots[knot][1] += 1
                else:
                   knots[knot][1] -= 1
        
            # move left, right, up, or down
            else:
                if knots[knot-1][0] > knots[knot][0]:   # right
                   knots[knot][0] += 1
                elif knots[knot-1][1] > knots[knot][1]: # down
                   knots[knot][1] += 1
                elif knots[knot-1][0] < knots[knot][0]: # left
                   knots[knot][0] -= 1
                elif knots[knot-1][1] < knots[knot][1]: # up
                   knots[knot][1] -= 1
                
        if not same(knot):
            grid[knots[knot][1]][knots[knot][0]] = knot

        if knot == 9:
            coordinates = str(knots[knot][0]) + "," + str(knots[knot][1])
            if coordinates not in positions:
                positions.append(coordinates)

        knot += 1
        move_tail(knot)
    
    
if __name__ == "__main__":

    starttime = time.time()

    #mode = 'test_1'
    mode = 'test_2'
    #mode = 'live'
    
    tracers = '#'
    #tracers = '.'
    
    counter = 0
    positions = []

    if mode == 'test_1':
        file = 'input_test_1.txt'

        head_y = 4
        head_x = 0

        tail_y = 4
        tail_x = 0
        
        width = 5
        height = 4
        
    elif mode == 'test_2':
        file = 'input_test_2.txt'

        head_y = 15
        head_x = 11

        tail_y = 15
        tail_x = 11

        width = 25
        height = 25
                
    elif mode == 'live':
        file = 'input.txt'

        head_y = 500
        head_x = 500

        tail_y = 500
        tail_x = 500

        width = 1000
        height = 1000
        
    knots = {
        0 : [head_x,head_y],
        1 : [head_x,head_y],
        2 : [head_x,head_y],
        3 : [head_x,head_y],
        4 : [head_x,head_y],
        5 : [head_x,head_y],
        6 : [head_x,head_y],
        7 : [head_x,head_y],
        8 : [head_x,head_y],
        9 : [head_x,head_y]
    }
    
    grid = draw(width, height, 1)
        
    with open(file) as directives:
    
        update()
        for directive in directives:
            counter += 1
            direction, distance = list(directive.strip().split(' '))
            move_head(direction,distance)
     
    print('')
    print('Total postitions: ' + str(len(positions)))
    print('Total runtime: ' + str(round(time.time()-starttime, 3)) + ' seconds.')
    print('')

'''

Total postitions: 2511
Total runtime: 0.477 seconds.

'''