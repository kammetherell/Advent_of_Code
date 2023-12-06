import aoc_helpers
import re
import numpy
import pandas as pd
import math
import datetime

example = [
    'Time:      7  15   30',
    'Distance:  9  40  200']

actual = [
    'Time:        41     77     70     96',
    'Distance:   249   1362   1127   1011'
]

def process_input(input):
    times = re.findall(r"(\d+)", input[0])
    distances = re.findall(r"(\d+)", input[1])

    races = []
    for i in range(0,len(times)):
        races.append((int(times[i]), int(distances[i])))

    return races

races_1 = process_input(actual)
input_2 = [i.replace(' ', '') for i in actual]
races_2 = process_input(input_2)

print('BRUTE FORCE')

def run_race(races):
    win_counts = []

    for race in races:
        win_count = 0

        for s in range(1,race[0]):
            #dist = speed * time
            dist = s * (race[0]-s)
            if dist > race[1]:
                win_count +=1

        win_counts.append(win_count)
    
    return math.prod(win_counts)

#PART 1
start = datetime.datetime.now()
output = run_race(races_1)
print(f"PART 1: {output}")

#PART 2
output = run_race(races_2)
print(f"PART 2: {output}")

end = datetime.datetime.now()
runtime_1 = (end - start).microseconds
print(f"Total runtime: {runtime_1}us")

##### Quadratic formula ATTEMPT #######

# Dist = speed * time
# Dist = speed * (race_time - speed)
# Dist = r_t * speed - speed^2
# speed^2 - r_t * speed + Dist = 0  ==> We can use quadratic to find intercepts for dist = win dist
#Quad formula for ax^2 + bx + c = 0
#      -b +/- sqrt(b^2 - 4ac)
# x = ------------------------
#             2a

# sp = ( r_t +- sqrt(r_t^2 - 4Dist) ) / 2

def run_race_quad(races):
    win_counts = []

    for race in races:
        race_time = race[0]
        dist = race[1]

        lower = int((race_time - math.sqrt(race_time**2 - 4*dist))/2)
        upper = int((race_time + math.sqrt(race_time**2 - 4*dist))/2)

        win_counts.append(upper - lower)
    
    return math.prod(win_counts)

print('QUADRATIC')
start = datetime.datetime.now()

#PART 1
output = run_race_quad(races_1)
print(f"PART 1: {output}")

#PART 2
output = run_race_quad(races_2)
print(f"PART 2: {output}")

end = datetime.datetime.now()
runtime_2 = (end - start).microseconds
print(f"Total runtime: {runtime_2}us")