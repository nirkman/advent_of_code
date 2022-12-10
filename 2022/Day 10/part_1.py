#!/usr/bin/env python3

# Advent of Code 2022
# Day 10, Part 1

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
    global cycles, signal
    
    cycles += 1
    
    if (cycles == 20) or (cycles % 40 == 20):
        signal += (cycles * x)


def noop():
    cycle()


def addx(v):
    global x
    
    cycle()
    cycle()
    x += int(v)


if __name__ == "__main__":

    starttime = time.time()

    #mode = 'test_1'
    #mode = 'test_2'
    mode = 'live'

    x = 1
    cycles = 0
    signal = 0
    
    if mode == 'test_1':
        file = 'input_test_1.txt'

    elif mode == 'test_2':
        file = 'input_test_2.txt'
        
    elif mode == 'live':
        file = 'input.txt'

    
    with open(file) as commands:
        for command in commands:
            execute(command.strip())
        cycle()
    
    print('')
    print('Cycles: ' + str(cycles))
    print('X register: ' + str(x))
    print('Signal: ' + str(signal))
    print('Total runtime: ' + str(round(time.time()-starttime, 3)) + ' seconds.')
    print('')

'''

Cycles: 241
X register: 33
Signal: 11820
Total runtime: 0.0 seconds.

'''