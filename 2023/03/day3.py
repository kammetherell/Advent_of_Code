import aoc_helpers
import re

example = aoc_helpers.load_data('example.txt')
actual = aoc_helpers.load_data('actual.txt')

def find_parts(input):
    parts = []

    min_row = min_col = 0
    max_row = len(input)
    max_col = len(input[0])

    for row, line in enumerate(input):
        output = {m.start(0):int(m.group(0)) for m in re.finditer("\d+", line)}
        
        for k,v in output.items():
            part_dict = {
                    'row': row,
                    'col': k,
                    'val': v
                }
            
            range_row = (
                max(min_row, row-1),
                min(max_row, row+2) #range sets last value as exclusive
            )
            part_dict['range_row'] = range_row

            range_col = (
                max(min_col, k-1),
                min(max_col,(k + len(str(v))+1))
            )
            part_dict['range_col'] = range_col

            valid, gear_coord = check_valid_part(part_dict, input)
            part_dict['valid'] = valid
            part_dict['gear_coord'] = gear_coord

            parts.append(part_dict)

    return parts

def check_valid_part(part, input):
    valid = False
    complete=False
    gear_coord = None
    
    while not valid and not complete:
        for row in range(*part['range_row']):
            for col in range(*part['range_col']):
                m = re.match(
                    r"[^0-9|.]",
                    input[row][col]
                )

                if m:
                    valid = True
                    if m.group() == '*':
                        gear_coord = (row,col)

        complete = True

    return valid, gear_coord

parts = find_parts(actual)

#PART 1
parts = [part for part in parts if part['valid']]

sum_of_parts = sum(
    [part['val'] for part in parts]
)

print('Part 1: ', sum_of_parts)

#PART 2
gear_opts = [part for part in parts if part['gear_coord'] is not None]

sum_gear_ratio = 0

for idx, gear in enumerate(gear_opts):
    matches = [
        g for g in gear_opts[idx+1:] 
        if g['gear_coord']==gear['gear_coord']
        ]
    
    if len(matches)>0:
        gear_ratio = gear['val'] * matches[0]['val']

        sum_gear_ratio+=gear_ratio

print('Part 2: ', sum_gear_ratio)