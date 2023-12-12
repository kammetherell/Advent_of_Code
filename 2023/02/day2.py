import aoc_helpers
import re

example = aoc_helpers.load_data('example.txt')
year = 2023
day = 2
actual = aoc_helpers.get_inputs(year,day, True)

limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def process_input(input):
    games = []
    for line in input:
        game_dict = {
            'str': line
        }


        game_id, rounds = line.split(': ')
        
        game_id = int(game_id.split(' ')[1])
        game_dict['game_id'] = game_id

        rounds = rounds.split('; ')
        game_dict['rounds'] = rounds

        games.append(game_dict)

    return(games)


games = process_input(actual)

#Part1:

re_red = r" (\d+) red"
re_green = r" (\d+) green"
re_blue = r" (\d+) blue"

valid_count = 0
power_sum = 0

for game in games:
    reds = re.findall(re_red, game['str'])
    max_reds = max([int(i) for i in reds])

    greens = re.findall(re_green, game['str'])
    max_greens = max([int(i) for i in greens])

    blues = re.findall(re_blue, game['str'])
    max_blues = max([int(i) for i in blues])

    valid = True
    if max_reds>limits['red'] or \
        max_blues > limits['blue'] or \
        max_greens > limits['green']:

        valid=False

    if valid:
        valid_count+=game['game_id']

    power = max_reds * max_greens * max_blues
    power_sum += power

print('Part 1: ', valid_count)
print('Part 2: ', power_sum)