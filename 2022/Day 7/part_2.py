#!/usr/bin/env python3

# Advent of Code 2022
# Day 7, Part 2

import time, json
from datetime import datetime, timedelta

starttime = time.time()
file = "input_test.txt"
file = "input.txt"
tree = {}
available = 70000000
needed = 30000000
deleted = 0


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

    global used, deleted
    subtotal = 0

    for key, value in tree.items():
        
        if type(value) is dict:
            subtotal += size(value)
        else:
            subtotal += int(value)
    return subtotal


def find(tree):

    global deleted
    subtotal = 0

    for key, value in tree.items():
        
        if type(value) is dict:
            subtotal += find(value)
        else:
            subtotal += int(value)
            
    if subtotal + unused >= needed:
        if subtotal <= deleted or deleted == 0:
            deleted = subtotal    

    return subtotal
    
with open(file) as directives:
        
    kind, data = parse(next(directives))
    tree.update(process(kind, data))
  
    print(json.dumps(tree, indent=4))
    print("")
    used = size(tree)
    unused = available - used
    find(tree)


print("")  
print("Total disk space.......: " + str(available))
print("Used disk space........: " + str(used))
print("Unused disk space......: " + str(unused))
print("Needed disk space......: " + str(needed))
print("")
print("Folder to be deleted...: " + str(deleted))
print("Unused disk space......: " + str(unused+deleted))
print("")
print("Total runtime: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")

'''

Total disk space.......: 70000000
Used disk space........: 43837783
Unused disk space......: 26162217
Needed disk space......: 30000000

Folder to be deleted...: 4183246
Unused disk space......: 30345463

Total runtime: 0.003 seconds.


'''