import aoc_helpers

example = aoc_helpers.load_data('test.txt')
actual = aoc_helpers.load_data('actual.txt')

p1_win_map = ['A Y', 'B Z', 'C X']
p1_draw_map = ['A X', 'B Y', 'C Z']

p1_score_map = {
    'X':1,
    'Y':2,
    'Z':3
}

def part_1(input):
    scores = []
    for i in input:
        round_score = 0
        if i in p1_win_map:
            round_score +=6
        elif i in p1_draw_map:
            round_score += 3

        round_score += p1_score_map[i[-1:]]

        scores.append(round_score)

    return scores

print(sum(part_1(actual)))

# # # # # # # # # # # # # # # # # # # # # # # # # # # #  

# A = Rock (1pt)
# B = paper (2pt)
# C = Scissors (3pt)


p2_score_map = {
    'X': {          #Lose
        'A': 3,         # Rock beats Scissors
        'B': 1,         # Paper beats Rock
        'C': 2,         # Scissors beats Paper
    },
    'Y': {          #Draw (plus 3pts for draw)
        'A': 4,         # Rock
        'B': 5,         # Paper
        'C': 6,         # Scissors
    }, 
    'Z':{           #Win (plus 6pts for win)
        'A': 8,         # Paper beats Rock
        'B': 9,         # Scissors beats Paper
        'C': 7,         # Rock beats Scissors
    }
}

def part_2(input):
    scores = []
    for i in input:
        outcome = p2_score_map[i[-1:]]
        round_score = outcome[i[:1]]

        scores.append(round_score)

    return scores

print(sum(part_2(actual)))