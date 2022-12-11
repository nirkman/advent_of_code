#!/usr/bin/env python3

# Advent of Code 2022
# Day 11, Part 2

import time, json
import psutil
from datetime import datetime, timedelta
from fractions import gcd


if __name__ == "__main__":

    starttime = time.time()

    #mode = 'test'
    mode = 'live'

    
    
    if mode == 'test':
        file = 'input_test.txt'

    elif mode == 'live':
        file = 'input.txt'


    monkeys = {}
    lowest_common_multiple = None
    with open(file) as lines:
        
        for line in lines:
            line = line.strip()

            if line.startswith("Monkey"):
                i = line.split(' ')[1].strip(":")
                monkeys[i] = {
                    'Items' : next(lines).split(": ")[1].strip().split(", "),
                    'Operation' : next(lines).strip().split(": ")[-1],
                    'Test' : {
                        'Divisor' : next(lines).strip().split(" ")[-1],
                        'True' : next(lines).strip().split(" ")[-1],
                        'False' : next(lines).strip().split(" ")[-1]
                    },
                    'Inspections' : 0
                }
                
                divisor = int(monkeys[i]['Test']['Divisor'])
                try:
                    lowest_common_multiple = lowest_common_multiple * divisor
                except:
                    lowest_common_multiple = divisor
                
            
        current_round = 1
        total_rounds = 10000
        
        while True:
            if current_round > total_rounds:
                break
                
            #print("ROUND #" + str(current_round) + " [" + str(int(psutil.Process().memory_info().rss / (1024 * 1024))) + "]")
            for i in monkeys:
                #print("Monkey " + str(i) + " was holding items " + str(monkeys[i]['Items']))

                # iterate over a copy using [:]
                for item in monkeys[i]['Items'][:]:
                    
                    # modulus
                    mod = int(monkeys[i]['Test']['Divisor'])
                    
                    # get 'new'
                    old = int(item)
                    #print("    OLD: " + str(old))
                    
                    # panic.
                    exec(monkeys[i]['Operation'])
                    
                    
                    # calm...
                    #new = int(new / 3)
                    new = new % lowest_common_multiple
                    #print("    NEW: " + str(new))

                    
                    # fling!
                    if new % mod == 0:
                        throw_to = monkeys[i]['Test']['True']
                    else:
                        throw_to = monkeys[i]['Test']['False']
            
                    #print("    THROW: " + str(throw_to))
                    del(monkeys[i]['Items'][0])
                    monkeys[throw_to]['Items'].append(new)
                    
                    monkeys[i]['Inspections'] += 1
                    
                #print("Monkey " + str(i) + " is now holding items " + str(monkeys[i]['Items']))
                #print("")
                
            current_round += 1
            #print("")
    
    activity = []
    for i in monkeys:
        activity.append(monkeys[i]['Inspections'])
    
    activity.sort(reverse=True)    
    
    print(json.dumps(monkeys, indent=4))
    
    print('')
    print('Monkey business: ' + str(activity[0] * activity[1]))
    print('Total runtime: ' + str(round(time.time()-starttime, 3)) + ' seconds.')
    print('')

'''

Monkey business: 17673687232
Total runtime: 4.53 seconds.

'''