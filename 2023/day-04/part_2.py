#!/usr/bin/env python3

# Advent of Code 2023
# Day 4, Part 2

import re
import time
from datetime import datetime, timedelta

def process(card, indent):
    global cards

    number = card['number']
    print(indent + "CARD " + str(number))
    if number not in counts:
        counts[number] = 1
    else:
        counts[number] += 1

    for my_number in card['my_numbers']:
        
        if my_number in card['winning_numbers']:
            number += 1
            process(cards[number], indent + "...")

starttime = time.time()

file = "input.txt"

cards = {}
counts = {}

with open(file) as input:
    
    for line in input:
    
        number, winning_numbers, my_numbers = line.strip().replace(": ", " | ").split(" | ")
    
        number = int(re.findall(r"\d+", number)[0])
        winning_numbers = re.findall(r"\d+", winning_numbers)
        my_numbers = re.findall(r"\d+", my_numbers)

        cards[number] = {
            'number' : number,
            'winning_numbers' : winning_numbers,
            'my_numbers' : my_numbers
        }

for number in cards:
    process(cards[number], "")
         
print("")
print("EXPECTED: {1: 1, 2: 2, 3: 4, 4: 8, 5: 14, 6: 1}")
print("ACTUAL..: " + str(counts))

print("")  
print("Total cards....: " + str(sum(counts.values())))  
print("Total runtime..: " + str(round(time.time()-starttime, 3)) + " seconds.")
print("")

'''
SAMPLE DATA

CARD 1
...CARD 2
......CARD 3
.........CARD 4
............CARD 5
.........CARD 5
......CARD 4
.........CARD 5
...CARD 3
......CARD 4
.........CARD 5
......CARD 5
...CARD 4
......CARD 5
...CARD 5
CARD 2
...CARD 3
......CARD 4
.........CARD 5
......CARD 5
...CARD 4
......CARD 5
CARD 3
...CARD 4
......CARD 5
...CARD 5
CARD 4
...CARD 5
CARD 5
CARD 6

EXPECTED: {1: 1, 2: 2, 3: 4, 4: 8, 5: 14, 6: 1}
ACTUAL..: {1: 1, 2: 2, 3: 4, 4: 8, 5: 14, 6: 1}

Total cards....: 30
Total runtime..: 0.0 seconds.
'''

'''
LIVE DATA
Total cards....: 5659035
Total runtime..: 30.878 seconds.
'''