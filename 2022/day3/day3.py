import aoc_helpers

example = aoc_helpers.load_data('test.txt')
actual = aoc_helpers.load_data('actual.txt')

def get_priority(char):
    priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    priority = priorities.index(char) + 1

    return priority

def part_1(input):
    priorities = []

    for rucksack in input:
        mid_point = int(len(rucksack)/2)
        in_both = list({i for i in rucksack[:mid_point] if i in rucksack[mid_point:]})
        priorities.append(get_priority(in_both[0]))
    
    return priorities

print(sum(part_1(actual)))

# # # # # # # # # # #  # # # # # # # # # 

def part_2(input):
    priorities = []

    idx=0

    while idx < len(input):
        group = input[idx:idx+3]

        group_common = list(
            {
                i for i in group[0] if (i in group[1]) and (i in group[2])
            }
        )
        priorities.append(get_priority(group_common[0]))
        idx +=3
    
    return priorities

print(sum(part_2(actual)))
