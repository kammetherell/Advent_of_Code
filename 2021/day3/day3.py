import aoc_helpers

inputs = aoc_helpers.load_data('actual.txt')

str_length = len(inputs[0])


print('part1')
summary = {}

for i in range(0,str_length):
    summary[str(i)] = {
        'ones':0,
        'zeros':0,
        'most': None,
        'least': None
    }

for i in inputs:
    for idx, chr in enumerate(i):
        num_ones = summary[str(idx)]['ones']
        num_zeros = summary[str(idx)]['zeros']

        if int(chr)==0:
            num_zeros +=1
        else:
            num_ones+=1

        if num_ones > num_zeros:
            most = 1
            least = 0
        else:
            most = 0
            least = 1

        summary[str(idx)] = {
                'ones':num_ones,
                'zeros':num_zeros,
                'most': most,
                'least': least
            }

gamma = ''
epsilon = ''

for v in summary.values():
    gamma = gamma + str(v['most'])
    epsilon = epsilon + str(v['least'])



print(f'Gamma: {gamma} - {int(gamma, 2)}; Epsilon: {epsilon} - {int(epsilon, 2)}; RESULT = {int(gamma, 2)*int(epsilon, 2)}')


print('part2')

o2_search = summary['0']['most']
co2_search = summary['0']['least']

#O2 calcs
o2_found = False
curr_o2_chr_idx = 0
o2_rating = ''
o2_inputs = inputs

while not o2_found:
    num_opts = len(o2_inputs)
    if num_opts == 1:
        o2_found = True
        o2_rating = o2_inputs[0]
        continue
    else:
        o2_inputs = [i for i in o2_inputs if i[curr_o2_chr_idx]==str(o2_search)]
        curr_o2_chr_idx +=1

        num_ones = 0
        num_zeros = 0

        for i in o2_inputs:
            for idx, chr in enumerate(i):
                if idx == curr_o2_chr_idx:
                    if int(chr)==0:
                        num_zeros +=1
                    else:
                        num_ones+=1

                    if num_ones >= num_zeros :
                        most = 1
                    else:
                        most = 0

                o2_search = most

print(f'O2: {o2_rating} - {int(o2_rating, 2)}')

#CO2 calcs
co2_found = False
curr_co2_chr_idx = 0
co2_rating = ''
co2_inputs = inputs

while not co2_found:
    num_opts = len(co2_inputs)
    if num_opts == 1:
        co2_found = True
        co2_rating = co2_inputs[0]
        continue
    else:
        co2_inputs = [i for i in co2_inputs if i[curr_co2_chr_idx]==str(co2_search)]
        curr_co2_chr_idx +=1

        num_ones = 0
        num_zeros = 0

        for i in co2_inputs:
            for idx, chr in enumerate(i):
                if idx == curr_co2_chr_idx:
                    if int(chr)==0:
                        num_zeros +=1
                    else:
                        num_ones+=1

                    if num_ones >= num_zeros :
                        least = 0
                    else:
                        least = 1

                co2_search = least

print(f'CO2: {co2_rating} - {int(co2_rating, 2)}')

print(f'RESULT - {int(o2_rating, 2) * int(co2_rating, 2)}')