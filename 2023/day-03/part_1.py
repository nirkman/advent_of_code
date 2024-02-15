#!/usr/bin/env python3

# Advent of Code 2023
# Day 3, Part 1

import time
from datetime import datetime, timedelta

class Schematic:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.parts = []
        self.data = []
        
        with open("input.txt") as input:
            for line in input:
                self.data.append(list(line.strip()))
        
    def read(self):
        for y, row in enumerate(self.data):
            self.y = y
            for x, cell in enumerate(row):
                self.x = x
                if not cell.isdigit() and cell != ".":
                    self.look_around()
        
    def look_around(self):
        print(str(self.x) + "," + str(self.y) + " -> " + self.data[self.y][self.x])
        print(schematic.data[self.y-1][self.x-1],schematic.data[self.y-1][self.x],schematic.data[self.y-1][self.x+1])
        print(schematic.data[self.y][self.x-1],schematic.data[self.y][self.x],schematic.data[self.y][self.x+1])
        print(schematic.data[self.y+1][self.x-1],schematic.data[self.y+1][self.x],schematic.data[self.y+1][self.x+1])
        print("")
        for y in [self.y-1, self.y, self.y+1]:
            for x in [self.x-1, self.x, self.x+1]:
                if self.data[y][x].isdigit():
                    self.parts.append(int(self.look_back(x,y) + self.data[y][x] + self.look_forward(x,y)))
   
    def look_back(self, x, y):
        
        value = ''
        x = x-1
        
        if self.data[y][x].isdigit():
            value = str(self.look_back(x, y)) + str(self.data[y][x])
        
        return value
        
        
    def look_forward(self, x, y):
        
        value = ''
        x = x+1
        
        if x < 140 and self.data[y][x].isdigit():
            value = str(self.data[y][x]) + str(self.look_forward(x, y))
            self.data[y][x] = '.'
        
        return value

starttime = time.time()

schematic = Schematic()
schematic.read()
        
print("")  
print("Parts Sum......: " + str(sum(schematic.parts)))  
print("Total runtime..: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")


'''
Parts Sum......: 544433
Total runtime..: 0.005 seconds.
'''