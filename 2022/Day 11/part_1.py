#!/usr/bin/env python3

# Advent of Code 2022
# Day 11, Part 1

import time, json
from datetime import datetime, timedelta


if __name__ == "__main__":

    starttime = time.time()

    #mode = 'test'
    mode = 'live'

    
    
    if mode == 'test':
        file = 'input_test.txt'

    elif mode == 'live':
        file = 'input.txt'


    monkeys = {}
    
    with open(file) as lines:
        
        for line in lines:
            line = line.strip()

            if line.startswith("Monkey"):
                
                monkeys[line.split(' ')[1].strip(":")] = {
                    'Items' : next(lines).split(": ")[1].strip().split(", "),
                    'Operation' : next(lines).strip().split(": ")[-1],
                    'Test' : {
                        'Divisor' : next(lines).strip().split(" ")[-1],
                        'True' : next(lines).strip().split(" ")[-1],
                        'False' : next(lines).strip().split(" ")[-1]
                    },
                    'Inspections' : 0
                }
        

            
        current_round = 1
        total_rounds = 20
        while True:
            if current_round > total_rounds:
                break
                
            print("ROUND #" + str(current_round))
            print("---------")
            
            for i in monkeys:
                print("Monkey " + str(i) + " was holding items " + str(monkeys[i]['Items']))

                # iterate over a copy using [:]
                for item in monkeys[i]['Items'][:]:
                    
                    # get 'new'
                    old = int(item)
                    print("    OLD: " + str(old))
                    
                    # panic.
                    exec(monkeys[i]['Operation'])
                    print("    NEW: " + str(new))
                    
                    # calm...
                    new = int(new / 3)
                    print("    NEW: " + str(new))
                    
                    # fling!
                    if new % int(monkeys[i]['Test']['Divisor']) == 0:
                        throw_to = monkeys[i]['Test']['True']
                    else:
                        throw_to = monkeys[i]['Test']['False']
            
                    print("    THROW: " + str(throw_to))
                    del(monkeys[i]['Items'][0])
                    monkeys[throw_to]['Items'].append(new)
                    
                    monkeys[i]['Inspections'] += 1
                    
                print("Monkey " + str(i) + " is now holding items " + str(monkeys[i]['Items']))
                print("")
            
            current_round += 1
            print("")
    
    activity = []
    for i in monkeys:
        activity.append(monkeys[i]['Inspections'])
    
    activity.sort(reverse=True)    
    print(activity)
    
    
    
    print(json.dumps(monkeys, indent=4))
    
    print('')
    print('Monkey business: ' + str(activity[0] * activity[1]))
    print('Total runtime: ' + str(round(time.time()-starttime, 3)) + ' seconds.')
    print('')

'''

Monkey business: 98280
Total runtime: 0.03 seconds.

'''