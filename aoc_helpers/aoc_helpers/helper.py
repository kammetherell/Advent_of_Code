def get_max_row_col(lst):
    max_row = len(lst)
    max_col = len(lst[0])

    return max_row, max_col

def list_of_lists(input):
    input  = input.split('\n\n')
    for idx, inp in enumerate(input):
        input[idx] = inp.splitlines()

    return input

def list_of_chars(input):
    input = input.splitlines()
    for idx, inp in enumerate(input):
        input[idx] = [char for char in inp]

    return input

def coords_dict(input):
    coords = {}
    max_row = 0
    max_col = 0
    for row, line in enumerate(input):
        max_row = max(max_row, row)
        for col, char in enumerate(line):
            max_col = max(max_col, col)
            coords[(row, col)] = char
    return coords, (max_row, max_col)