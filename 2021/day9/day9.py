import aoc_helpers
inputs = aoc_helpers.load_data('actual.txt')
inputs = [list(i) for i in inputs]

num_cols = len(inputs[0])
num_rows = len(inputs)

def get_low_points(heightmap):
    low_points = []

    num_cols = len(heightmap[0])
    num_rows = len(heightmap)

    for r in range(num_rows):
        for c in range(num_cols):
            coords_to_check = [
                (0,-1), #Up
                (-1,0), #Left
                (1,0), #Right
                (0,1) #Down
                ]

            curr_val = int(heightmap[r][c])
            
            low_point = True
            for coord in coords_to_check:
                r_check = r + coord[0]
                c_check = c + coord[1]

                if low_point and r_check >= 0 and c_check >= 0 and r_check < num_rows and c_check < num_cols:
                    low_point = curr_val < int(heightmap[r_check][c_check])

            if low_point:
                low_points.append((r,c,curr_val))

    return low_points

print('day1')
low_points = get_low_points(inputs)

risk_level = 0
for i in low_points:
    risk_level += i[2]+1

print(risk_level) 

print('day2')

def find_flow_neighbours(coord):
    coords_to_check = [
        (0,-1), #Up
        (-1,0), #Left
        (1,0), #Right
        (0,1) #Down
        ]
    
    flow_neighbours = set()

    for check in coords_to_check:
        r_check = coord[0] + check[0]
        c_check = coord[1] + check[1]

        if r_check >= 0 and c_check >= 0 and r_check < num_rows and c_check < num_cols:
            if coord[2] < int(inputs[r_check][c_check]) and int(inputs[r_check][c_check])!=9:
                flow_neighbours.add((r_check, c_check, int(inputs[r_check][c_check])))

    return flow_neighbours

def find_basin_size(low_point):
    basin = {low_point}

    basin_found = False
    while not basin_found:
        len_basin_start = len(basin)
        for coord in basin:
            basin = basin.union(find_flow_neighbours(coord))
        
        #If start length and end length are same, no more to find
        if len_basin_start == len(basin):
            basin_found = True

    return len(basin)

basins = []

for lp in low_points:
    basins.append(find_basin_size(lp))

basins.sort(reverse=True)

score = basins[0]*basins[1]*basins[2]

print(score)

    

