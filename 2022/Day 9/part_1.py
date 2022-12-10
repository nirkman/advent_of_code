#!/usr/bin/env python3

# Advent of Code 2022
# Day 9, Part 1

import os, sys, time, json
from datetime import datetime, timedelta


def draw(width, height):
    
    grid = []
    
    while len(grid) <= height:
        row = []
        while len(row) <= width:
            row.append('.')
        grid.append(row)
    grid[tail_y][tail_x] = 'T'
    grid[head_y][head_x] = 'H'
    
    return grid


def update():
    if mode != 'live':
        time.sleep(.1)
        os.system('clear')
        print('\n'.join([' '.join([str(cell) for cell in row]) for row in grid]))
        print("")
        print("Touching: " + str(touching()) + " | " + "Count: " + str(counter) + " | Head: " + str(head_x) + "," + str(head_y) + " | Tail: " + str(tail_x) + "," + str(tail_y))


def touching():
    
    # same position
    if head_x == tail_x and head_y == tail_y:
        return True
    
    # same row
    if head_x == tail_x and abs(head_y - tail_y) < 2:
        return True
    
    # same column
    if abs(head_x - tail_x) < 2 and head_y == tail_y:
        return True
    
    # diagonal
    if abs(head_x - tail_x) < 2 and abs(head_y - tail_y) < 2:
        return True
    
    return False

def same():
    return head_x == tail_x and head_y == tail_y

def move_head(direction=None, distance=None):
    global head_x, head_y
    
    if direction and distance:

        i = 1
        while i <= int(distance):
        
            coordinates = str(head_x) + "," + str(head_y)
            if coordinates in positions:
                grid[head_y][head_x] = '#'
            else:
                grid[head_y][head_x] = '.'
                
            if direction == 'U':
                head_y -= 1
            elif direction == 'R':
                head_x += 1
            elif direction == 'D':
                head_y += 1
            elif direction == 'L':
                head_x -= 1

            move_tail()            
            grid[head_y][head_x] = 'H'

            update()
            i += 1


def move_tail():
    global tail_x, tail_y
    
    if not same():
        grid[tail_y][tail_x] = '#'
        
    if not touching():
        
        # move diagonally
        if head_x != tail_x and head_y != tail_y:
    
            if head_x > tail_x:
                tail_x += 1
            else:
                tail_x -= 1
            
            if head_y > tail_y:
                tail_y += 1
            else:
                tail_y -= 1
        
        # move left, right, up, or down
        else:
            if head_x > tail_x:   # right
                tail_x += 1
            elif head_y > tail_y: # down
                tail_y += 1
            elif head_x < tail_x: # left
                tail_x -= 1
            elif head_y < tail_y: # up
                tail_y -= 1
                            
    if not same():
        grid[tail_y][tail_x] = 'T'
    
    coordinates = str(tail_x) + "," + str(tail_y)
    if coordinates not in positions:
        positions.append(coordinates)
    
    
if __name__ == "__main__":

    starttime = time.time()

    #mode = 'test_1'
    #mode = 'test_2'
    mode = 'live'

    counter = 0
    positions = []

    if mode == 'test_1':
        file = 'input_test_1.txt'

        head_y = 4
        head_x = 0

        tail_y = 4
        tail_x = 0

        grid = draw(5, 4)

    elif mode == 'test_2':
        file = 'input_test_2.txt'

        head_y = 20
        head_x = 15

        tail_y = 20
        tail_x = 15

        grid = draw(40, 40)
        
    elif mode == 'live':
        file = 'input.txt'

        head_y = 500
        head_x = 500

        tail_y = 500
        tail_x = 500

        grid = draw(1000, 1000)
    
    with open(file) as directives:
    
        try:
            update()
            for directive in directives:
                counter += 1
                direction, distance = list(directive.strip().split(' '))
                move_head(direction,distance)
        
        except:
            print("ERROR!")
    
    print('')
    print('Total postitions: ' + str(len(positions)))
    print('Total runtime: ' + str(round(time.time()-starttime, 3)) + ' seconds.')
    print('')

'''

Total postitions: 6332
Total runtime: 1.011 seconds.

'''