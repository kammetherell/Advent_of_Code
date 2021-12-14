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
            temp_opts = temp_opts + get_next_opts(opt)
        else:
            complete.append(opt)

    opts = temp_opts

print(len(complete))

print('part2')

def check_route_valid(route):
    small_caves = {
        'start':0,
        'end':0
    }

    for step in route:
        if step.islower():
            if step in small_caves:
                small_caves[step] += 1
            else:
                small_caves[step] = 1

    #check conditions
    one_start = small_caves['start']==1
    one_end = small_caves['end']<=1

    one_multi_visit = len({k:v for k,v in small_caves.items() if (v>1 and k not in ['start','end'])}) <= 1
    no_triple_plus = not len({k:v for k,v in small_caves.items() if (v>2 and k not in ['start','end'])}) > 0

    valid = one_start * one_end * one_multi_visit * no_triple_plus

    return bool(valid)#, (one_start , one_end , one_multi_visit , no_triple_plus)


def get_next_opts_2(route_so_far):
    last_pos = route_so_far[-1:][0]
    next_opts = valid_dests[last_pos]

    route_opts = set()

    for step in next_opts:
        opt = list(route_so_far) + [step]
        if check_route_valid(opt):
            route_opts.add(tuple(opt))

    return list(route_opts)

# print(check_route_valid(['start', 'ab', 'ab', 'cd', 'end']))
# print(check_route_valid(['start', 'ab', 'ab', 'ab', 'end']))
# print(check_route_valid(['start', 'ab', 'ab', 'cd', 'cd','end']))
# print(check_route_valid(['start', 'ab', 'ab', 'start', 'cd', 'end']))

opts = [['start']]
complete = []

all_found = False
i = 0

while not all_found:
    print(f'loop {i}', end='\r')
    temp_opts = []
    if len(opts)==0:
        all_found = True
    for opt in opts:
        if opt[-1:][0]!='end':
            op = get_next_opts_2(opt)
            temp_opts = temp_opts + get_next_opts_2(opt)
        else:
            complete.append(opt)

    opts = temp_opts
    i+=1

print()
print(len(complete))
