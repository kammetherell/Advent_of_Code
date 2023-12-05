import aoc_helpers
import re
import numpy
import pandas as pd

example = aoc_helpers.load_data('example.txt')
actual = aoc_helpers.load_data('actual.txt')

#PART1
def get_locns(seeds, input):
    locns = []
    for seed in seeds:
        found = False
        #Start at seed, but we'll use s to iterate the current value
        s = seed

        for line in input[2:]:
            #check for blank or text lines
            if line == '' or not line[0].isdigit():
                #Reset mapping when finds blank or text
                found=False
            #only keep checking if we haven't found any map yet
            elif not found:
                [dest_start, source_start, length] = line.split()
                dest_start = int(dest_start)
                source_start = int(source_start)
                length = int(length)

                #Check if value being searched is in target range for line
                if source_start <= s <= source_start + length:
                    #If it is, find dest value
                    s = dest_start + (s-source_start)
                    found=True

        locns.append(s)
    return locns

p1_seeds = [int(s) for s in actual[0][7:].split()]

part1_locns = get_locns(p1_seeds, actual)
print('PART 1: ', min(part1_locns))

#PART 2
class Range:
    def __init__(self, lower, upper) -> None:
        self.lower = lower
        self.upper = upper
    def __repr__(self) -> str:
        return f'Range [{self.lower}:{self.upper})'
    def overlap(self, other):
        #Return the range that represents the overlap of two ranges
        temp_range = Range(
            lower=max(self.lower, other.lower),
            upper=min(self.upper, other.upper)
        )

        if temp_range.lower < temp_range.upper:
            return temp_range
        else:
            return None
    def compare_map(self, map_list):
        output = []
        found = False
        for m in map_list:
            if not found:
                overlap = self.overlap(m[0])

                if overlap is not None:
                    #Musat be some overlap, so process the overlap and add to the output
                    inc = Range(overlap.lower + m[1], overlap.upper+m[1])
                    output.append(inc)
                    found = True


                    if (self.lower == overlap.lower) and (self.upper != overlap.upper) :
                        #remainder is from top of overlap and end of current
                        remainder = Range(overlap.upper, self.upper)
                        #process remainder against map
                        inc_remainder = remainder.compare_map(map_list)
                        output += inc_remainder
                    elif (self.lower != overlap.lower) and (self.upper == overlap.upper):
                        remainder = Range(self.lower, overlap.lower)
                        inc_remainder = remainder.compare_map(map_list)
                        output += inc_remainder
                    elif (self.lower != overlap.lower) and (self.upper != overlap.upper):
                        remainder_1 = Range(self.lower, overlap.lower)
                        remainder_2 = Range(overlap.upper, self.upper)

                        inc_1 = remainder_1.compare_map(map_list)
                        output += inc_1

                        inc_2 = remainder_2.compare_map(map_list)
                        output += inc_2

        
        if not found:
            output.append(Range(self.lower, self.upper))
        
        return output
    
#######
complete = False
first = True

maps = []

while not complete:
    try:
        split_idx = actual.index('')
        if first:
            temp = actual[0:split_idx]
            first = False
        else:
            temp = actual[1:split_idx]
            
        actual = actual[split_idx+1:]
        maps.append(temp)
    except:
        complete = True
        maps.append(actual[1:])

#SEEDS
seeds = maps[0]
m = re.findall(r"(\d+)",seeds[0])
seeds = [int(i) for i in m]

#MAPS
maps = maps[1:]

#Get Seed Ranges
seed_ranges = []

for i in range(0,len(seeds),2):
    lower = seeds[i]
    upper = seeds[i] + seeds[i+1]

    temp_range = Range(lower, upper)

    seed_ranges.append(temp_range)

#Convert maps to tuples of Range and increment
for i, m in enumerate(maps):
    for j, line in enumerate(m):
        dest, source, size = map(int, line.split())
        m[j] = (Range(source, source+size), dest-source)
    maps[i] = m

#Create processing function
def process_step(ranges, map_layer):
    output = []
    for r in ranges:
        #print(r)
        temp = r.compare_map(map_layer)
        #print(temp)
        output +=temp

    return output

#Work ranges through each map
soil_ranges = process_step(seed_ranges, maps[0])
fert_ranges = process_step(soil_ranges, maps[1])
watr_ranges = process_step(fert_ranges, maps[2])
lght_ranges = process_step(watr_ranges, maps[3])
temp_ranges = process_step(lght_ranges, maps[4])
humd_ranges = process_step(temp_ranges, maps[5])
locn_ranges = process_step(humd_ranges, maps[6])

min_locn = min([locn.lower for locn in locn_ranges])

print('PART 2: ',min_locn)