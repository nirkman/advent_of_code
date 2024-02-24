#!/usr/bin/env python3

# Advent of Code 2023
# Day 5, Part 1

import re
import time
import pprint
from datetime import datetime, timedelta

starttime = time.time()
pretty = pprint.PrettyPrinter(indent=4)

file = "input.txt"

points = 0

mappings = {}

with open(file) as input:
    
    for line in input:
        line = line.strip()
        if line.startswith("seeds: "):
            seeds = [int(x) for x in line.replace("seeds: ", "").split(" ")]
        elif line == "":
            pass
        elif line.endswith(" map:"):
            name = line.replace(" map:", "")
            mappings[name] = []
        else:
            destination, source, length = [int(x) for x in line.split(" ")]
            mappings[name].append({
                'start'       : source,
                'end'         : source+length,
                'destination' : destination
            })

lowest_location = None

for seed in seeds:
    print("seed -> " + str(seed))
    next_mapping = seed
    for key, value in mappings.items():
        for mapping in value:
            if mapping['start'] <= next_mapping < mapping['end']:
                next_mapping = mapping['destination'] + next_mapping - mapping['start']
                break
        print(key + " -> " + str(next_mapping))

    if not lowest_location or next_mapping < lowest_location:
        lowest_location = next_mapping
        
    print("SEED: " + str(seed) + " -> " + "LOCATION: " + str(next_mapping))
    print("")

    
print("")  
print("Lowest Location: " + str(lowest_location))  
print("Total runtime..: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")