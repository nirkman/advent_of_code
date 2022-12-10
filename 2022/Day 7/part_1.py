#!/usr/bin/env python3

# Advent of Code 2022
# Day 7, Part 1

import time, json
from datetime import datetime, timedelta

starttime = time.time()
#file = "input_test.txt"
file = "input.txt"
tree = {}
total = 0


def parse(directive):

    directive = directive.strip()

    # COMMANDS
    if directive.startswith("$"):
        kind = "command"
        
        bash, command = directive.split(' ', 1)
        data = command.split(' ')
        
    # DATA
    else:
        kind = "listing"
        data = directive.split(' ')

    return kind, data


def process(kind, data):

    if kind == 'command':
        return cd()
    else:
        ls(data)


def ls(data):

    while True:
        if kind != "listing":
            break
        kind, data = process(next(directives))
        if data[0] == "dir":
            tree[data[1]] = {}
        else:
            tree[data[1]] = int(data[0])
        
 
def cd():

    cwd = {}

    for directive in directives:

        kind, data = parse(directive)
        
        if kind == "command":
            
            if data[0] == "cd":
            
                if data[1] == "..":
                    break
                else:
                    cwd[data[1]] = cd()
                        
            elif data[0] == "ls":
                pass
                
        elif kind == "listing":
            if data[0] == "dir":
                cwd[data[1]] = {}
            else:
                cwd[data[1]] = int(data[0])

    return cwd


def size(tree):

    global total
    subtotal = 0

    for key, value in tree.items():
        
        if type(value) is dict:
            subtotal += size(value)
        else:
            subtotal += int(value)
    
    if subtotal <= 100000:
        total += subtotal

    return subtotal


with open(file) as directives:
        
    kind, data = parse(next(directives))
    tree.update(process(kind, data))
  
    print(json.dumps(tree, indent=4))
    print("")
    size(tree)
    
    

print("")  
print("Total size of folders less than 100000: " + str(total))  
print("Total runtime: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")

'''

Total size of folders less than 100000: 1454188
Total runtime: 0.003 seconds.

'''