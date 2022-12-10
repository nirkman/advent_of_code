#!/usr/bin/env python3

# Advent of Code 2022
# Day 5, Part 1

import time
from datetime import datetime, timedelta
from textwrap import wrap

starttime = time.time()
#file = "input_test.txt"
file = "input.txt"
final = 0


stacks = []
stack_lines = []

def move(directive):
    
    directives = directive.split(" ")
    count = int(directives[1])
    source = int(directives[3]) - 1      # I don't like these assumptions. Should be using
    destination = int(directives[5]) - 1 # the provided stack numbers instead.
    
    while count > 0:
        stacks[destination].append(stacks[source].pop())
        count -= 1

with open(file) as input:

    parse_crates = True
    
    for line in input:
        
        line = line.strip("\n")
        
        # build stacks
        if parse_crates:
            
            # blank line means we're moving from initial stacks to movement orders
            if line.strip() == "":
                parse_crates = False
                
                # pop the numer line - we don't need it
                stack_lines.pop()
                
                # build initial stacks
                for stack_line in stack_lines:
                    crates = wrap(stack_line, 4, replace_whitespace=False, drop_whitespace=False)

                    for index, crate in enumerate(crates):

                        crate = crate.strip()
                        try:
                            stacks[index].insert(0, crate)
                        except:
                            stacks.append([crate])
                
                # remove placeholders from top of stack(s)
                for stack in stacks:
                    while("" in stack):
                        stack.remove("")
                        
                print(stacks)

            else:
                # store these up and process later so we can pop the number row
                stack_lines.append(line)
        
        # move crates
        else:
            print(line)
            move(line)
                          
#print(stacks)
output = ""
for stack in stacks:
    output = output + str(stack.pop())


print("")  
print("Final Order: " + output.replace("[", "").replace("]", ""))  
print("Total runtime: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")

'''

Final Order: CNSZFDVLJ
Total runtime: 0.003 seconds.

'''