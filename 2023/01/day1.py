import aoc_helpers

example = aoc_helpers.load_data('example.txt')
actual = aoc_helpers.load_data('actual.txt')

def part_1(input):
    calibration_values = []
    for line in input:
        numbers = [i for i in line if i.isdigit()]
        cal_val = numbers[0]+ numbers[-1]
        calibration_values.append(int(cal_val))

    return calibration_values


print(sum(part_1(actual)))

test2 = [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen',
    ]

word_num_map = {
    'one':'o1e',
    'two':'t2o',
    'three':'th3ee',
    'four':'fo4r',
    'five':'fi5e',
    'six':'s6x',
    'seven':'se7en',
    'eight':'ei8ht',
    'nine':'ni9e'
}

def part_2(input):
    for idx,line in enumerate(input):
        for key in word_num_map.keys():
            line = line.replace(key, word_num_map[key])

        input[idx] = line
    
    print(sum(part_1(input)))

part_2(actual)