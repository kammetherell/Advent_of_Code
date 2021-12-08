import aoc_helpers

inputs = aoc_helpers.load_data('actual.txt')

inputs = [{"connections":i.split(' | ')[0].split(' '), "display": i.split(' | ')[1].split(' ')} for i in inputs]

print('part1')

num_uniqu_disp = 0

for i in inputs:
    for disp in i['display']:
        if len(disp) in [2,3,4,7]:
            num_uniqu_disp +=1

print(num_uniqu_disp)

print('part2')

#  0:(6)   1:(2)   2:(5)   3:(5)   4:(4)
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#  5:(5)   6:(6)   7:(3)   8:(7)   9:(6)
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

# 1,4,7,8 unique
# 0, 6, 9 - len 6
# 2, 3, 5 - len 5

# #1 = cf
# #4 = bcdf 
# #7 = acf = a + 1 ==> a = 7-1
# #8 = abcdefg 

# len 5 combos

# #2 = acdeg != bf ==> shares 2 with #4
# #3 = acdfg ==> only one to contain #1
# #5 = abdfg != ce ==> Other

#Len 6 combos

# #0 = abcefg ==> only one not to contain #4
# #6 = abdefg ==> only one not to contain #1
# #9 = abcdfg ==> other

import re

def fuzzy_substring(needle, haystack, num_chars_match = None):
    if num_chars_match is None:
        num_chars_match = len(needle)

    num_matched = 0

    for char in needle:
        if bool(re.search(char, haystack)):
            num_matched += 1

    found = num_matched == num_chars_match

    return found
    


def define_nums(connections):
    nums_map = {
        0:None,
        1:None,
        2:None,
        3:None,
        4:None,
        5:None,
        6:None,
        7:None,
        8:None,
        9:None
    }

    nums_map[1] = [i for i in connections if len(i)==2][0]
    nums_map[4] = [i for i in connections if len(i)==4][0]
    nums_map[7] = [i for i in connections if len(i)==3][0]
    nums_map[8] = [i for i in connections if len(i)==7][0]

    #len5 combos
    len5_connections = [i for i in connections if len(i)==5]
    len_5_matched = []

    nums_map[3] = [i for i in len5_connections if fuzzy_substring(nums_map[1], i)][0]
    len_5_matched.append(nums_map[3])

    nums_map[2] = [i for i in len5_connections if fuzzy_substring(nums_map[4], i, 2) and i not in len_5_matched][0]
    len_5_matched.append(nums_map[2])

    nums_map[5] = [i for i in len5_connections if i not in len_5_matched][0]

    #len6 combos
    len6_connections = [i for i in connections if len(i)==6]
    len_6_matched = []

    nums_map[6] = [i for i in len6_connections if not fuzzy_substring(nums_map[1], i)][0]
    len_6_matched.append(nums_map[6])

    nums_map[0] = [i for i in len6_connections if not fuzzy_substring(nums_map[4], i) and i not in len_6_matched][0]
    len_6_matched.append(nums_map[0])

    nums_map[9] = [i for i in len6_connections if i not in len_6_matched][0]

    #reverse dictionary
    output_nums = {}

    for k,v in nums_map.items():
        if v is not None:
            output_nums[''.join(sorted(v))]=k

    return output_nums

def decode(input):
    num_map = define_nums(input['connections'])
    output = ''


    for i in input['display']:
        wires = ''.join(sorted(i))
        num = num_map[wires]
        output = output + str(num)

    return output


sum = 0
for idx, i in enumerate(inputs):
    print(f'Input {idx}', end='\r')
    sum = sum + int(decode(i))

print('#######')
print(sum)

# for i in inputs