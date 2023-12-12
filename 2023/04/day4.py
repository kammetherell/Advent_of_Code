import aoc_helpers

example = aoc_helpers.load_data('example.txt')
year = 2023
day = 4
actual = aoc_helpers.get_inputs(year,day, True)

def get_point_value(line):
    line =  line.split(': ')[1]

    winning = line.split(' | ')[0].split(' ')

    #remove items when there'd been a double space in list
    invalid_items = True
    while invalid_items:
        try:
            winning.remove('')
        except:
            invalid_items = False

    card = line.split(' | ')[1].split(' ')

    num_matches = sum(el in card for el in winning)
    points=0
    if num_matches>0:
        points = 2**(num_matches-1)

    return (num_matches, points)

#Part 1
total_score = 0
for line in actual:
    score = get_point_value(line)[1]
    total_score += score

print('Part 1: ', total_score)


#Part2
scratchcards = [1]*len(actual)

for idx, line in enumerate(actual):
    num_matches = get_point_value(line)[0]

    if num_matches>0:
        for n in range(scratchcards[idx]):
            for i in range(1,num_matches+1):
                scratchcards[idx+i] = scratchcards[idx+i] +1

print('part 2: ',sum(scratchcards))