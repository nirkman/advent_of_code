#!/usr/bin/env python3

# Advent of Code 2022
# Day 10, Part 2

import os, sys, time, json
from datetime import datetime, timedelta


def execute(command):
    command = command.split(' ', 1)
    
    if command[0] == 'noop':
        noop()
    else:
        if command[0] == 'addx':
            addx(command[1])


def cycle():
    global x, y
    
    # current column on the CRT
    if x > 39:
        x = 0
        y += 1
    
    # current row on the CRT
    if y > 5:
        y = 0
    
    # show the sprite position
    for i in range(len(sprite[0])):
        sprite[0][i] = '.'
    
    # ... because apparently it's possible for the sprite to extend past the monitor
    try:
        sprite[0][register-1] = '#'
    except:
        pass
    
    sprite[0][register] = '#'
    
    try:
        sprite[0][register+1] = '#'
    except:
        pass
        
    # show the clock
    for i in range(len(clock[0])):
        clock[0][i] = '.'
    clock[0][x] = '+'
    
    # set pixels
    if (x == register - 1) or (x == register) or (x == register + 1):
        crt[y][x] = '#'
    
    update()
    x += 1
    
    if mode != 'live':
        time.sleep(.1)


def noop():
    cycle()


def addx(v):
    global register
    
    cycle()
    cycle()
    register += int(v)


def draw(width, height):
    
    grid = []
    
    while len(grid) <= height:
        row = []
        while len(row) <= width:
            row.append('.')
        grid.append(row)
    
    return grid


def update():
    time.sleep(0)
    os.system('clear')
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in sprite]))
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in clock]))
    print("")
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in crt]))
    print("")


if __name__ == "__main__":

    starttime = time.time()

    #mode = 'test_1'
    mode = 'test_2'
    #mode = 'live'

    register = 1
    x = 0
    y = 0
    
    sprite = draw(39, 0)
    clock = draw(39, 0)
    crt = draw(39, 5)


    if mode == 'test_1':
        file = 'input_test_1.txt'

    elif mode == 'test_2':
        file = 'input_test_2.txt'
        
    elif mode == 'live':
        file = 'input.txt'

    
    with open(file) as commands:
        update()
        for command in commands:
            execute(command.strip())
        cycle()
    
    print('')
    print('Total runtime: ' + str(round(time.time()-starttime, 3)) + ' seconds.')
    print('')

'''

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . # # # . . . . .
+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# # # # . # # # . . . . # # . # # # . . # # # . . # . . # . . # # . . # . . # .
# . . . . # . . # . . . . # . # . . # . # . . # . # . # . . # . . # . # . . # .
# # # . . # . . # . . . . # . # # # . . # . . # . # # . . . # . . # . # # # # .
# . . . . # # # . . . . . # . # . . # . # # # . . # . # . . # # # # . # . . # .
# . . . . # . . . . # . . # . # . . # . # . # . . # . # . . # . . # . # . . # .
# # # # . # . . . . . # # . . # # # . . # . . # . # . . # . # . . # . # . . # .


Total runtime: 2.379 seconds.

'''