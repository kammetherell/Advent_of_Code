import aoc_helpers

inputs = aoc_helpers.load_data('actual.txt')
inputs = [i.split(' -> ') for i in inputs]

print('day1')

line_counts = {

}

for line in inputs:
    x1,y1 = line[0].split(',')
    x2,y2 = line[1].split(',')

    #Only process straight lines
    if x1==x2 or y1==y2:
        start_x = min([int(x1),int(x2)])
        end_x = max([int(x1),int(x2)])
        start_y = min([int(y1),int(y2)])
        end_y = max([int(y1),int(y2)])

        for x in range(int(start_x), int(end_x)+1):
            for y in range(int(start_y), int(end_y)+1):
                try:
                    line_counts[(x,y)]+=1
                except:
                    line_counts[(x,y)] = 1

num_greater_1 = sum(count > 1 for count in line_counts.values())

print(num_greater_1)

print('day2')

line_counts = {

}

for line in inputs:
    x1,y1 = line[0].split(',')
    x2,y2 = line[1].split(',')
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    start_x = min([x1,x2])
    end_x = max([x1,x2])
    start_y = min([y1,y2])
    end_y = max([y1,y2])

    #Only process straight lines
    if x1==x2 or y1==y2:
        for x in range(start_x, end_x+1):
            for y in range(start_y, end_y+1):
                try:
                    line_counts[(x,y)]+=1
                except:
                    line_counts[(x,y)] = 1

    #Process 45 deg diagonals
    if (end_y - start_y) == (end_x - start_x):
        x_increment = +1
        y_increment = +1
        if x2 < x1:
            x_increment = -1
        if y2 < y1:
            y_increment = -1

        coords = []
        for i in range(0,end_x-start_x+1):
            coord = (x1+i*x_increment, y1+i*y_increment)
            coords.append(coord)

        for coord in coords:
            try:
                line_counts[(coord[0],coord[1])]+=1
            except:
                line_counts[(coord[0],coord[1])] = 1

num_greater_1 = sum(count > 1 for count in line_counts.values())

print(num_greater_1)