import aoc_helpers

inputs = aoc_helpers.load_data('actual.txt')
inputs = [int(i) for i in inputs]

print('part1')
num_increases = 0
for idx, i in enumerate(inputs):
    if idx > 0 and i>inputs[idx-1]:
        num_increases +=1

print(num_increases)

print('part2')
num_increases = 0
for idx, i in enumerate(inputs):
    if idx > 2:
        cur_sum = sum(inputs[idx-2:idx+1])
        prev_sum = sum(inputs[idx-3:idx])

        # print(f'index:{idx}; cur_sum:{cur_sum}; prev_sum:{prev_sum}')

        if cur_sum > prev_sum:
            num_increases +=1

print(num_increases)