from os import device_encoding
import aoc_helpers

inputs = aoc_helpers.load_data('actual.txt')

template = inputs[0]
insertions = {i.split(' -> ')[0]:i.split(' -> ')[1] for i in inputs[2:]}

print('part1')
num_loops_1 = 10

for loop in range(num_loops_1):
    output = template[0]
    for i in range(len(template)-1):
        
        pair_to_check = template[i:i+2]
        if pair_to_check in insertions:
            output = output + insertions[pair_to_check] + template[i+1]
        else: 
            output = output + template[i+1]

    template = output

counts = dict()

for char in template:
    if char in counts:
        counts[char]+=1
    else:
        counts[char] = 1

min_char = min(counts, key=counts.get)
max_char = max(counts, key=counts.get)

print(counts[max_char] - counts[min_char])

print('part2')
num_loops_2 = 40

template = inputs[0]

def update_polymer(polymer, insertions, steps):
    result_dict = dict()
    for i in range(len(polymer) - 1):
        #Initial summary
        if polymer[i:i + 2] in result_dict:
            result_dict[polymer[i:i + 2]] += 1
        else:
            result_dict[polymer[i:i + 2]] = 1

    #Loop through steps
    for s in range(steps):
        for k, v in list(filter(lambda x: x[1] > 0, result_dict.items())): # filter through all valid inserts
            pairs_to_add = [k[0] + insertions[k], insertions[k] + k[-1]]

            for pair in pairs_to_add:
                if pair in result_dict:
                    result_dict[pair] += v 
                else:
                    result_dict[pair] = v
            

            result_dict[k] -= v  # minus this insertions as completed
    return result_dict

output = update_polymer(template, insertions, 40)

summary = dict()

summary[template[0]] = 1
summary[template[-1]] = 1
for k,v in output.items():
    if k[0] in summary:
        summary[k[0]] += v
    else:
        summary[k[0]] = v

    if k[1] in summary:
        summary[k[1]] += v
    else:
        summary[k[1]] = v

min_char = min(summary, key=summary.get)
max_char = max(summary, key=summary.get)

print(int(summary[max_char]/2 - summary[min_char]/2))
