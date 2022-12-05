import aoc_helpers
import re

example = aoc_helpers.load_data('test.txt')
actual = aoc_helpers.load_data('actual.txt')

def prep_input(input):
    split_point = input.index('')
    start_posn = input[:split_point]
    steps = input[split_point+1:]

    #Mapping start to lists representing each stack
    start_dict = {i:[] for i in start_posn[-1].split()}

    for i in start_posn[:-1]:
        for k in start_dict.keys():
            crate = i[start_posn[-1].index(k)]
            
            if crate != ' ':
                start_dict[k].insert(0,crate)


    return start_dict, steps

def part_1(input):
    start, steps = prep_input(input)

    for step in steps:
        format = r'move (?P<count>\w+) from (?P<start>\w+) to (?P<end>\w+)'
        m = re.match(format, step)
        step_dict = m.groupdict()

        for i in range(int(step_dict['count'])):
            start[step_dict['end']].append(start[step_dict['start']].pop())

    message = ''
    for v in start.values():
        message += v[-1]

    return message
print(part_1(actual))

# # # # # # # # # # # # # # # # # # # # # # 

def part_2(input):
    start, steps = prep_input(input)

    for step in steps:
        format = r'move (?P<count>\w+) from (?P<start>\w+) to (?P<end>\w+)'
        m = re.match(format, step)
        step_dict = m.groupdict()

        crates_to_move = []
        for i in range(int(step_dict['count'])):
            crates_to_move.append(start[step_dict['start']].pop())
        # reverse crates being lifted
        crates_to_move.reverse()

        start[step_dict['end']] = start[step_dict['end']] + crates_to_move

    message = ''
    for v in start.values():
        message += v[-1]

    return message

print(part_2(actual))