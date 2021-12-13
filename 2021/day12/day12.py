import aoc_helpers
from requests.api import get

inputs = aoc_helpers.load_data('actual.txt')

valid_dests = {
    'start':set()
}

for i in inputs:
    point1, point2 = i.split('-')
    
    if point2 != 'start' and point1 != 'end':
        if point1 in valid_dests:
            valid_dests[point1].add(point2)
        else:
            valid_dests[point1] = {point2}

    if point1 != 'start' and point2 != 'end':
        if point2 in valid_dests:
            valid_dests[point2].add(point1)
        else:
            valid_dests[point2] = {point1}

print('part1')

def get_next_opts(route_so_far):
    last_pos = route_so_far[-1:][0]
    next_opts = valid_dests[last_pos]

    route_opts = set()

    for step in next_opts:
        if not step.islower() or (step.islower() and step not in route_so_far):
            opt = list(route_so_far) + [step]
            route_opts.add(tuple(opt))

    return list(route_opts)

opts = [['start']]
complete = []

all_found = False

while not all_found:
    temp_opts = []
    if len(opts)==0:
        all_found = True
    for opt in opts:
        if opt[-1:][0]!='end':
            op = get_next_opts(opt)
            temp_opts = temp_opts + get_next_opts(opt)
        else:
            complete.append(opt)

    opts = temp_opts

print(len(complete))

print('part2')
