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

            valid = check_valid_part(part_dict, input)
            part_dict['valid'] = valid

            parts.append(part_dict)

    return parts

def check_valid_part(part, input):
    valid = False
    complete=False
    
    while not valid and not complete:
        for row in range(*part['range_row']):
            for col in range(*part['range_col']):
                m = re.match(
                    r"[^0-9|.]",
                    input[row][col]
                )

                if m:
                    valid = True

        complete = True

    return valid

parts = find_parts(actual)
parts = [part for part in parts if part['valid']]

sum_of_parts = sum(
    [part['val'] for part in parts]
)

print('Part 1: ', sum_of_parts)