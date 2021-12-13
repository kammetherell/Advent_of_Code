import aoc_helpers

inputs = aoc_helpers.load_data('actual.txt')
inputs = [[int(char) for char in i] for i in inputs]

steps_to_run = 100

print('part1')

part1_inp = inputs

num_flashes = 0

for step in range(steps_to_run):
    print(f'starting step {step}', end='\r')
    temp_inpt = [[col+1 for col in row] for row in part1_inp]

    impacted_range = [
        (-1,-1), (0,-1), (1,-1),
        (-1,0), (1,0),
        (-1,1), (0,1), (1,1)
        ]

    flashes = set()

    all_flashes_found = False
    while not all_flashes_found:
        start_len = len(flashes)
        for r_idx, row in enumerate(temp_inpt):
            for c_idx, col in enumerate(row):
                if col > 9 and (((r_idx, c_idx) not in flashes) or not (bool(flashes))): # 
                    flashes.add((r_idx, c_idx))

                    for i in impacted_range:
                        r_imp = r_idx + i[0]
                        c_imp = c_idx + i[1]

                        if r_imp >= 0 and r_imp < 10 and c_imp>=0 and c_imp<10:
                            temp_inpt[r_imp][c_imp] +=1
        
        end_len = len(flashes)

        if end_len == start_len:
            all_flashes_found = True

    for fsh in flashes:
        temp_inpt[fsh[0]][fsh[1]] = 0

    part1_inp = temp_inpt

    num_flashes = num_flashes + len(flashes)
print('')
print(num_flashes)

print('part2')

all_flashed = False
part2_inp = inputs
step = 0
while not all_flashed:
    step = step+1
    print(f'starting step {step}', end='\r')
    temp_inpt = [[col+1 for col in row] for row in part2_inp]

    impacted_range = [
        (-1,-1), (0,-1), (1,-1),
        (-1,0), (1,0),
        (-1,1), (0,1), (1,1)
        ]

    flashes = set()

    all_flashes_found = False
    while not all_flashes_found:
        start_len = len(flashes)
        for r_idx, row in enumerate(temp_inpt):
            for c_idx, col in enumerate(row):
                if col > 9 and (((r_idx, c_idx) not in flashes) or not (bool(flashes))): # 
                    flashes.add((r_idx, c_idx))

                    for i in impacted_range:
                        r_imp = r_idx + i[0]
                        c_imp = c_idx + i[1]

                        if r_imp >= 0 and r_imp < 10 and c_imp>=0 and c_imp<10:
                            temp_inpt[r_imp][c_imp] +=1
        
        end_len = len(flashes)

        if end_len == start_len:
            all_flashes_found = True

    for fsh in flashes:
        temp_inpt[fsh[0]][fsh[1]] = 0

    if len(flashes)==100:
        all_flashed = True

    part2_inp = temp_inpt