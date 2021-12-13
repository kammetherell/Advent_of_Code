import aoc_helpers

inputs = aoc_helpers.load_data('actual.txt')

# [
#   (
#       {
#           (
#               <
#                   (
#                       ()
#                   )
#                   []
#               >
#               [
#                   [
#                       {
#                           []
#                           {
#                               <
#                                   ()
#                                   <>
#                               >


# [(()[<>])]({[<{<<[]>>(
# {
#   (
#       [
#           (
#               <
#                   {}
#                   [
#                       <>
#                       []
#                   }
#               >{[]{[(<()> - CORRUPT - Expected ], but found } instead
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]] - CORRUPT - Expected ], but found ) instead.
# [{[{({}]{}}([{[{{{}}([] - CORRUPT - Expected ), but found ] instead.
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]() - CORRUPT - Expected >, but found ) instead
# <{([([[(<>()){}]>(<<{{ - CORRUPT - Expected ], but found > instead.
# <
#   {
#       (
#           [
#               {
#                   {}
#               }
#               [
#                   <
#                       [
#                           [
#                               [
#                                   <>
#                                   {}
#                               ]
#                           ]
#                       ]
#                   >
#                   []
#               ]


chunk_open = [
    '(',
    '[',
    '{',
    '<'
]

chunk_close = [
    ')',    
    ']',
    '}',
    '>'
]

def check_line(line):
    scan_complete = False
    while not scan_complete:
        start_length = len(line)

        line = line.replace('()','')
        line = line.replace('[]','')
        line = line.replace('{}','')
        line = line.replace('<>','')

        end_length = len(line)
        if start_length == end_length:
            scan_complete = True

    first_invalid_char = None
    chunk_open_char = None

    for idx, char in enumerate(line):
        if first_invalid_char is None and char in chunk_close:
            first_invalid_char = char
            chunk_open_char = line[idx-1]

    output = {
        'err_type':'Incomplete',
        'first_invalid_char': 'n/a',
        'chunk_open_char': 'n/a',
        'final_line': line
    }

    if first_invalid_char is not None:
        output['err_type'] = 'Corrupt'
        output['first_invalid_char'] = first_invalid_char
        output['chunk_open_char'] = chunk_open_char

    return output

scores = []
corrupt_lines = []
incomplete_opens = []

score_map = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
}

for idx, line in enumerate(inputs):
    scan = check_line(line)
    
    if scan['err_type']=='Corrupt':
        score = score_map[scan['first_invalid_char']]
        scores.append(score)
        corrupt_lines.append(idx)

    else:
        incomplete_opens.append(scan['final_line'])
print('day1')
print(sum(scores))

print('day2')

score_map_2 = {
    ')':1,
    ']':2,
    '}':3,
    '>':4
}

score_2 = []

for line in incomplete_opens:
    reverse = line[::-1]
    reverse = reverse.replace('(',')')
    reverse = reverse.replace('[',']')
    reverse = reverse.replace('{','}')
    reverse = reverse.replace('<','>')

    score = 0

    for char in reverse:
        score = score * 5
        score = score + score_map_2[char]
    
    score_2.append(score)

import statistics

print(statistics.median(score_2))