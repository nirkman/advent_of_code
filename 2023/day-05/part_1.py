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

#pretty.pprint(mappings['seed-to-soil'])


lowest_location = None

for seed in seeds:
    print("seed -> " + str(seed))
    next_mapping = seed
    for key, value in mappings.items():
        for mapping in value:
            #pretty.pprint(mapping)
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


'''
146416131
TOO LOW
'''

'''
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''

'''

with open(file) as input:
    
    for line in input:
        line = line.strip()
        if line.startswith("seeds: "):
            seeds = [int(x) for x in line.replace("seeds: ", "").split(" ")]
        elif line == "":
            pass
        elif line.endswith(" map:"):
            name = line.replace(" map:", "")
            mappings[name] = {}
        else:
            destination, source, length = [int(x) for x in line.split(" ")]
            for i in range(length):
                destination += 1
                source += 1
                mappings[name][source] = destination

#pretty.pprint(mappings)

lowest_location = None

for seed in seeds:
    next_mapping = seed
    #print("seed -> " + str(seed))
    for mapping in mappings:
        #pretty.pprint(mappings[mapping])
        if next_mapping in mappings[mapping]:
            next_mapping = mappings[mapping][next_mapping]
            #print("DEBUG: seed="+str(seed)+", next="+str(next_mapping))
        #print(mapping + " -> " + str(next_mapping))

    if not lowest_location or next_mapping < lowest_location:
        lowest_location = next_mapping
        
    #print("SEED: " + str(seed) + " -> " + "LOCATION: " + str(next_mapping))
    #print("")

    
print("")  
print("Lowest Location: " + str(lowest_location))  
print("Total runtime..: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")
'''