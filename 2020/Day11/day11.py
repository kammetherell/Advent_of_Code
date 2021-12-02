import itertools
from copy import deepcopy

with open("./Day11/input.txt") as f:
    inputs = f.readlines()
inputs = [x.strip('\n') for x in inputs] 

def split(word): 
    return [char for char in word]

inputs = [split(x) for x in inputs]

with open("./Day11/test2.txt") as f:
    test = f.readlines()
test = [x.strip('\n') for x in test] 

test = [split(x) for x in test]

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
    
    return num_occupied

def count_occupied(data):
    num_occupied = 0

    for row in data:
            for col in row:
                if col == '#':
                    num_occupied +=1

    return num_occupied


def day11_1():
    changed = True
    start = deepcopy(inputs)
    end = deepcopy(inputs)
    num_loops = 1

    while changed:
        print(f'\rStarting Loop: {num_loops}\r', end='', flush=True)
        end = []
        changed = False
        for r_idx, row in enumerate(start):
            temp_row = []
            for c_idx, col in enumerate(row):
                
                num_occupied = find_neighbours(start, r_idx, c_idx)

                if col == 'L' and num_occupied == 0:
                    temp_row.append('#')
                    changed = True
                elif col == '#' and num_occupied > 3:
                    temp_row.append('L')
                    changed = True
                else:
                    temp_row.append(col)
            end.append(temp_row)

        start = deepcopy(end)
        num_loops +=1

    end_num_occupied = count_occupied(end)
    
    return end_num_occupied

print('===PART1===')
day11_pt1 = day11_1()
print(f'\r')
print(day11_pt1)

print('===PART2===')

def find_visible_seats(data, row, col):
    transformations = [
            (-1,-1),
            (-1,0),
            (-1,1),
            (0,-1),
            (0,1),
            (1,-1),
            (1,0),
            (1,1)
        ]

    num_occupied = 0

    for t in transformations:
        # print(f'Transformation: {t}')
        seat_found = False
        # start at current seat
        try_seat_row = row
        try_seat_col = col
        try_seat = '.' #Default to floor in case we don't find any seat at all

        #Loop over transformation until we find a seat
        while not seat_found:
            
            try_seat_row += t[0]
            try_seat_col += t[1]

            # Check location we are trying actually exists
            row_in_range = try_seat_row >= 0 and try_seat_row < len(data) 
            col_in_range = try_seat_col >= 0 and try_seat_col < len(data[0])

            #If it does, find the value
            if row_in_range and col_in_range:
                try_seat = data[try_seat_row][try_seat_col]

                # If not floor, set Seat found to True
                if try_seat != '.':
                    # print(f'Seat Found at row: {try_seat_row}, col {try_seat_col}')
                    seat_found = True
            else: #Invoked if we go off edge of seat map - treat as floor
                seat_found = True
        
        if try_seat =='#':
            num_occupied += 1

    return num_occupied

def day11_2():
    changed = True
    start = deepcopy(inputs)
    end = deepcopy(inputs)
    num_loops = 1

    while changed:
        print(f'\rStarting Loop: {num_loops}\r', end='', flush=True)
        end = []
        changed = False
        for r_idx, row in enumerate(start):
            temp_row = []
            for c_idx, col in enumerate(row):
                num_occupied = find_visible_seats(start, r_idx, c_idx)

                if col == 'L' and num_occupied == 0:
                    temp_row.append('#')
                    changed = True
                elif col == '#' and num_occupied > 4:
                    temp_row.append('L')
                    changed = True
                else:
                    temp_row.append(col)
            end.append(temp_row)

        start = deepcopy(end)
        num_loops +=1

    end_num_occupied = count_occupied(end)
    
    return end_num_occupied

day11pt2 = day11_2()
print(f'\r')
print(day11pt2)