import aoc_helpers

inputs = aoc_helpers.load_data('actual.txt')
numbers = inputs[0].split(',')

def print_card(card):
    for row in card:
        print(row)

cards = []
curr_card = []

for idx, i in enumerate(inputs[2:]):
    if i=='':
        cards.append(curr_card)
        curr_card = []
    else:
        row = i.split(' ')
        row = [i for i in row if i!='']
        curr_card.append(row)
    
    if idx == (len(inputs)-3):
        cards.append(curr_card)

print('part1')
def check_card(card, number):
    for idx_r, row in enumerate(card):
        for idx_el,el in enumerate(row):
            if el==number:
                row[idx_el] = '-'

    winner = False

    if any(row == ['-', '-', '-', '-', '-'] for row in card):
        winner = True

    cols = []
    for i in range(0,5):
        col = [card[0][i],card[1][i],card[2][i],card[3][i],card[4][i]]
        cols.append(col)
    if any(col == ['-', '-', '-', '-', '-'] for col in cols):
        winner = True

    return winner, card

def run_bingo(numbers, cards):
    winner=False

    numbers_idx = 0
    winning_card = []
    last_num = ''

    while not winner:
        last_num = numbers[numbers_idx]

        for idx, card in enumerate(cards):
            winner, card = check_card(card, last_num)
            if winner:
                winning_card = card
                return winning_card, idx, last_num
        
        numbers_idx +=1

def calc_card_score(card, last_num):
    card_score = 0
    for idx_r, row in enumerate(card):
        for idx_el, el in enumerate(row):
            if el!='-':
                card_score+=int(el)

    card_score = card_score * int(last_num)

    return card_score

winning_card, card_idx, last_num = run_bingo(numbers, cards)

print(f'Winning Card Index: {card_idx} with a score of {calc_card_score(winning_card, last_num)}')

print('part2')

def run_bingo_2(numbers, cards):
    numbers_idx = 0
    winning_cards = []
    last_num = ''

    while len(winning_cards) < len(cards):
        last_num = numbers[numbers_idx]

        for idx, card in enumerate(cards):
            if idx not in winning_cards:
                winner, card = check_card(card, last_num)
                if winner:
                    winning_cards.append(idx)
        
        numbers_idx +=1

    last_winner = cards[winning_cards[-1:][0]]

    print_card(last_winner)

    return last_winner, last_num


last_card, last_num = run_bingo_2(numbers, cards)

print(
    f'last with a score of {calc_card_score(last_card, last_num)}')
