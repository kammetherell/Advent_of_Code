import aoc_helpers

example = aoc_helpers.load_data('test.txt')
actual = aoc_helpers.load_data('actual.txt')

start_point=500

def place_rocks(input, plot=False):
    rocks = set()
    for shape in input:
        corners = shape.split(' -> ')
        corners = [tuple(map(int,c.split(','))) for c in corners]

        for i in range(1, len(corners)):
            prev_c = corners[i-1]
            curr_c = corners[i]

            dir_x = (curr_c[0]-prev_c[0])/max([abs(curr_c[0]-prev_c[0]),1])
            dir_y = (curr_c[1]-prev_c[1])/max([abs(curr_c[1]-prev_c[1]),1])

            x,y = prev_c
            while (x,y) != curr_c:
                rocks.add((x,y))
                x += dir_x
                y += dir_y
            rocks.add((x,y))

    if plot:
        plot_grid(rocks)

    return rocks

def plot_grid(rocks, sand=None):
    min_x = int(min([
        rock[0] for rock in rocks
    ]))

    max_x = int(max([
        rock[0] for rock in rocks
    ]))

    if sand is not None:
        min_x_sand = int(min([
            s[0] for s in sand
        ]))

        max_x_sand = int(max([
            s[0] for s in sand
        ]))

        min_x = min([min_x, min_x_sand])
        max_x = max([max_x, max_x_sand])

    max_y = int(max([
        rock[1] for rock in rocks
    ])) + 2

    min_y=0

    grid=[]
    for y in range(min_y, max_y+1):
        grid.append(
            ['.'] * (max_x - min_x + 1)
        )

    #set fill point
    grid[0][500-min_x] = '+'

    #update rocks
    for r in rocks:
        grid[int(r[1])][int(r[0])-min_x] = '#'

    if sand is not None:
        for s in sand:
            grid[int(s[1])][int(s[0])-min_x] = 'o'


    for line in grid:
        print(''.join(line))

def drop_sand(rocks, sand, y_lim):
    (x,y) = (500,0)

    blocked = rocks.union(sand)

    while y < y_lim:

        #check if immediate drop is already blocked
        if (x,y+1) in blocked:
            #cell below is blockd, try left
            if(x-1,y+1) in blocked:
                #left blocked, try right
                if (x+1, y+1) in blocked:
                    #can't go anywhere - final resting place
                    return (x,y)
                #diagonal right empty, drop there
                else:
                    x = x+1
                    y +=1
            #diagonal left empty, drop there
            else:
                x = x-1
                y+=1
        
        #Nothing below, keep dropping
        else:
            y+=1

    return(x,y_lim+1)

def part_1(input, plot=False):
    rocks = place_rocks(input, plot)

    max_y = int(max([
        rock[1] for rock in rocks
    ]))


    sand = set()
    abyss = False

    while not abyss:
        #print(f'Sand Drop {len(sand) + 1}')
        drop = drop_sand(rocks, sand, max_y + 1) 

        if drop[1]>max_y:
            #sand fallen into abyss
            abyss=True
        else:
            sand.add(drop)

            if plot:
                plot_grid(rocks, sand)

    print(len(sand))
    
part_1(actual, False)

def part_2(input, plot=False):
    rocks = place_rocks(input, plot)



    max_y = int(max([
        rock[1] for rock in rocks
    ]))

    #Add floor rocks
    for i in range(-500,500):
        rocks.add((500+i,max_y + 2))


    sand = set()
    blocked = False
    last = (0,0)

    while not blocked:
        drop = drop_sand(rocks, sand, max_y+2) 
        print(f'Sand Drop {len(sand) + 1}: {drop}', end = '\r')

        if drop == (500,0):
            #sand drop blocked
            blocked=True
        else:
            if drop not in sand:
                sand.add(drop)

                if plot:
                    plot_grid(rocks, sand)
            else:
                plot_grid(rocks, sand)
                raise Exception('Entering infinite loop')

    print(f'\n{len(sand)+1}')

part_2(actual, False)

