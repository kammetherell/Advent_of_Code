from copy import deepcopy

main = ['.##.####',
        '.#.....#',
        '#.###.##',
        '#####.##',
        '#...##.#',
        '#######.',
        '##.#####',
        '.##...#.']

test = [
        '.#.',
        '..#',
        '###',
        ]

def define_start_coords(start_data):
    data = []
    z = 0
    max_x = len(start_data[0])
    max_y = len(start_data)
    for y, row in enumerate(start_data):
        for x, char in enumerate(row):
            temp = {
                'x': x,
                'y': y,
                'z': z,
                'val': char
            }

            data.append(temp)
    
    data_range = [(0,max_x), (0, max_y), (0,1)]

    output = [data_range, data]

    return output

start = define_start_coords(main)

def get_val_from_coords(data, x, y, z):
    val = [i for i in data if (i['x']==x and i['y']==y and i['z']==z)]
    item = '.'
    if len(val) > 0:
        item = val[0]['val']

    return item

def run_cycle(data):
    x_range = data[0][0]
    y_range = data[0][1]
    z_range = data[0][2]

    new_data = []

    for x in range(x_range[0]-1, x_range[1]+1):
        for y in range(y_range[0]-1, y_range[1]+1):
            for z in range(z_range[0]-1, z_range[1]+1):
                curr_val = get_val_from_coords(data[1], x, y, z)

                num_occupied = 0

                for x_n in range(x-1, x+2):
                    for y_n in range(y-1, y+2):
                        for z_n in range(z-1, z+2):
                            if x_n!=x or y_n!=y or z_n!=z:
                                neighbour = get_val_from_coords(data[1], x_n, y_n, z_n)
                                if neighbour == '#':
                                    num_occupied +=1

                if curr_val == '#' and num_occupied not in [2,3]:
                    curr_val = '.'
                elif curr_val == '.' and num_occupied == 3:
                    curr_val = '#'

                new_data.append({
                    'x': x,
                    'y': y,
                    'z': z,
                    'val': curr_val
                })
    data_range = [
        (x_range[0]-1, x_range[1]+1), 
        (y_range[0]-1, y_range[1]+1), 
        (z_range[0]-1, z_range[1]+1)]

    output = [data_range, new_data]
    
    return output

def calc_num_active (data):
    num_active = len([i for i in data[1] if i['val']=='#'])
    return num_active

def plot_layer(data, z):
    x_range = data[0][0]
    y_range = data[0][1]

    for y in range(y_range[0], y_range[1]):
        temp_str=''
        for x in range(x_range[0], x_range[1]):
            temp_str += get_val_from_coords(data[1], x, y, z)
        print(temp_str)

print('===PART 1===')
for i in range(6):
    end = run_cycle(start)
    start = deepcopy(end)

print(calc_num_active(end))

# ===========================================
# PART 2

def define_start_coords_4d(start_data):
    data = []
    z = 0
    w = 0
    max_x = len(start_data[0])
    max_y = len(start_data)
    for y, row in enumerate(start_data):
        for x, char in enumerate(row):
            temp = {
                'x': x,
                'y': y,
                'z': z,
                'w': w,
                'val': char
            }

            data.append(temp)
    
    data_range = [(0,max_x), (0, max_y), (0,1), (0,1)]

    output = [data_range, data]

    return output

def get_val_from_coords_4d(data, x, y, z, w):
    val = [i for i in data if (i['x']==x and i['y']==y and i['z']==z and i['w']==w)]
    item = '.'
    if len(val) > 0:
        item = val[0]['val']

    return item

def run_cycle_4d(data):
    x_range = data[0][0]
    y_range = data[0][1]
    z_range = data[0][2]
    w_range = data[0][3]

    new_data = []

    for x in range(x_range[0]-1, x_range[1]+1):
        for y in range(y_range[0]-1, y_range[1]+1):
            for z in range(z_range[0]-1, z_range[1]+1):
                for w in range(w_range[0]-1, w_range[1]+1):
                    curr_val = get_val_from_coords_4d(data[1], x, y, z, w)

                    num_occupied = 0

                    for x_n in range(x-1, x+2):
                        for y_n in range(y-1, y+2):
                            for z_n in range(z-1, z+2):
                                for w_n in range(w-1, w+2):
                                    if x_n!=x or y_n!=y or z_n!=z or w_n!=w:
                                        neighbour = get_val_from_coords_4d(data[1], x_n, y_n, z_n, w_n)
                                        if neighbour == '#':
                                            num_occupied +=1

                    if curr_val == '#' and num_occupied not in [2,3]:
                        curr_val = '.'
                    elif curr_val == '.' and num_occupied == 3:
                        curr_val = '#'

                    new_data.append({
                        'x': x,
                        'y': y,
                        'z': z,
                        'w': w,
                        'val': curr_val
                    })

    data_range = [
        (x_range[0]-1, x_range[1]+1), 
        (y_range[0]-1, y_range[1]+1), 
        (z_range[0]-1, z_range[1]+1),
        (w_range[0]-1, w_range[1]+1),
        ]

    output = [data_range, new_data]
    
    return output

print('===PART 2===')
start_4d = define_start_coords_4d(main)
for i in range(6):
    print(f'\rStarting Loop {i}\r', end='', flush=True)
    end_4d = run_cycle_4d(start_4d)
    start_4d = deepcopy(end_4d)

print(calc_num_active(end_4d))