import aoc_helpers
import networkx as nx

example = aoc_helpers.load_data('test.txt')
actual = aoc_helpers.load_data('actual.txt')

# Plan: build list of lists that branch at each point until a list gets to 'E'
heights='abcdefghijklmnopqrstuvwxyz'


def prep_data(input):
    coords = []
    data = {
        'start':(),
        'end':(),
        'map': []
    }

    for y, line in enumerate(input):
        for x, height in enumerate(line):
            if height =='S':
                data['start'] = (x,y,'a')
                height='a'

            if height =='E':
                data['end'] = (x,y,'z')
                height='z'

            coords.append((x,y,height))

    data['map']= coords

    return data


def run(data):
    G = nx.DiGraph()

    G.add_nodes_from(data['map'])

    for coord in data['map']:      
        opts = [
            (coord[0]+1, coord[1]), #Right
            (coord[0]-1, coord[1]), #left
            (coord[0], coord[1]+1), #Down
            (coord[0], coord[1]-1), #Up
            ]

        for opt in opts:
            opt_data = list(
                filter(
                    lambda x: (x[0]==opt[0]) and (x[1]==opt[1]), 
                    data['map']
                ))

            #Check if coord found in map
            if len(opt_data)==1:
                opt_data = opt_data[0]

                valid = (
                    (heights.index(coord[2])+1)>=heights.index(opt_data[2])
                    )
                if valid:
                    G.add_edge(coord, opt_data)

    part_1 = nx.shortest_path_length(
        G,
        source=data['start'],
        target=data['end'])

    
    part_2_shortest = part_1

    start_opts = list(
                filter(
                    lambda x: x[2]=='a', 
                    data['map']
                ))
    
    for opt in start_opts:
        try:
            opt_len = nx.shortest_path_length(
                G,
                source=opt,
                target=data['end'])

            if opt_len < part_2_shortest:
                part_2_shortest = opt_len
        except:
            continue


    return part_1, part_2_shortest


data = prep_data(actual)
print(run(data))
