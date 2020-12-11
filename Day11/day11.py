import itertools
from copy import deepcopy

with open("./Day11/input.txt") as f:
    inputs = f.readlines()
inputs = [x.strip('\n') for x in inputs] 

def split(word): 
    return [char for char in word]

inputs = [split(x) for x in inputs]

def find_neighbours(data, row, col):
    refs = [-1,0,1]

    num_occupied = 0
    num_empty = 0
    num_floor = 0

    for i in refs:
        for j in refs:
            if (i != 0 or j != 0) and (row+i >= 0 and col + j >= 0): #Ignore current position
                # print(f'Row: {row + i}; Col: {col + j};')
                
                try:
                    # print(f'Value: {data[row + i][col + j]}')
                    neighbour = data[row + i][col + j]

                    if neighbour == 'L':
                        num_empty += 1
                    elif neighbour == '#':
                        num_occupied += 1
                    elif neighbour == '.':
                        num_floor += 1
                except:
                    # print('Out of range')
                    continue
    # print(num_occupied, num_empty, num_floor)
    
    return num_occupied, num_empty, num_floor

def day11_1():
    changed = True
    start = deepcopy(inputs)
    end = deepcopy(inputs)
    num_loops = 1

    while changed:
        print(f'Starting Loop: {num_loops}')
        end = []
        changed = False
        for r_idx, row in enumerate(start):
            temp_row = []
            for c_idx, col in enumerate(row):
                num_occupied, num_empty, num_floor = find_neighbours(start, r_idx, c_idx)

                if col == 'L' and num_occupied == 0:
                    temp_row.append('#')
                    changed = True
                elif col == '#' and num_occupied > 3:
                    temp_row.append('L')
                    changed = True
                else:
                    temp_row.append(col)
            end.append(temp_row)

        # for line in end:
        #     print(line)
        start = deepcopy(end)
        num_loops +=1

    end_num_occupied = 0
    for r_idx, row in enumerate(end):
            for c_idx, col in enumerate(row):
                if col == '#':
                    end_num_occupied +=1
    
    return end_num_occupied

print(day11_1())



