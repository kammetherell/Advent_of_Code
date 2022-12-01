import aoc_helpers

example = aoc_helpers.load_data('example.txt')
actual = aoc_helpers.load_data('actual.txt')

def run_part_1(inputs):
    max_cals=0
    temp_cals=0

    for i in inputs:
        if i != '':
            temp_cals += int(i)
        else:
            if temp_cals > max_cals:
                max_cals = temp_cals
            temp_cals = 0

    return max_cals

print(run_part_1(actual))

# # # # # # # # # # # # # # # # # # # # # # # 
def run_part_2(inputs):
    cals=[]
    temp_cals=0

    for i in inputs:
        if i != '':
            temp_cals += int(i)
        else:
            cals.append(temp_cals)
            temp_cals = 0
    cals.append(temp_cals)

    cals.sort(reverse=True)
    
    return sum(cals[:3]), cals[:3]

print(run_part_2(actual))