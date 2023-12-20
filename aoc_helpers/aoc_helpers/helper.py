def get_shape(lst: list) -> tuple:
    '''Function to return the max row and max col in a 2d array (list)

    Args:
      lst: list
        A list of strings or list of lists that you want to find 
        the overall shape of
    
    
    Returns:
      A tuple of form (max_row, max_col) for the given input
    '''
    max_row = len(lst)
    max_col = len(lst[0])

    return max_row, max_col

def list_of_lists(input: str) -> list:
    '''Function convert an AOC input into a list of lists

    Args:
      input: str
        The AoC input as a string, with blank lines between 
        the input sections you want to split up
    
    
    Returns:
      a list of lists. first split is on "\\n\\n", then 
      each section is divided based on splitlines()
    '''
    input  = input.split('\n\n')
    for idx, inp in enumerate(input):
        input[idx] = inp.splitlines()

    return input

def list_of_chars(input:str)->list:
    '''Splits an AoC input into respective lines, and then splits 
    each line into a list of characters

    Args:
      input: str
        The AoC input as a string
    
    Returns:
      a list where each element is a line in the input
    '''
    input = input.splitlines()
    for idx, inp in enumerate(input):
        input[idx] = [char for char in inp]

    return input

def coords_dict(input:list)->dict:
    '''Converts a 2d array (input must have already been split into 
    a list) into a dictionary of coordinates(keys) with the item at 
    that coord the value

    Args:
      input: list
        The list which you want to convert to coordinates

    Returns:
      A Dictionaty with keys of coordinates (row,col) and values (char)
    '''
    coords = {}
    shape = get_shape(input)
    for row, line in enumerate(input):
        for col, char in enumerate(line):
            coords[(row, col)] = char
    return coords, shape