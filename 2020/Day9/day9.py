import itertools

with open("./Advent_of_Code/Day9/input.txt") as f:
    inputs = f.readlines()
inputs = [x.strip('\n') for x in inputs] 
inputs = [int(i) for i in inputs]

def check_valid(num, preamble):
    combinations = list(itertools.combinations(preamble,2))
    combo_idx = 0
    valid = False
    
    while not valid and combo_idx < len(combinations):
        combination = combinations[combo_idx]
        
        if (combination[0]+combination[1]) == num:
            valid = True
            break
        combo_idx += 1
        
    return valid
    
def day9_1():
    idx = 25
    found = False
    found_idx = 0
    
    while not found and idx < len(inputs):
        # print('foo', end='')
        print(f'\r{idx}\r', end='', flush=True)
        valid = check_valid(inputs[idx], inputs[idx-25:idx])
        
        if not valid:
            found = True
            found_idx = idx
            break
        else:
            idx +=1
    
    if found:
        return found_idx, inputs[found_idx]
    else:
        return 'Nothing Found'
        
print('===PART1===')
invalid_idx, invalid_val = day9_1()
print(invalid_val)

print('===PART2===')

def day9_2():
    preamble = inputs[:invalid_idx]
    contiguous_len = 2
    
    found = False
    found_sum = 0
    
    while not found and contiguous_len < invalid_idx:
        print(f'\rTrying combinations length: {contiguous_len}\r', end='', flush=True)
        combos = []
        
        for i in range(invalid_idx):
            combos.append(preamble[i:i+contiguous_len])
        
        for combo in combos:
            if sum(combo) == invalid_val:
                print(combo)
                found = True
                found_sum = min(combo) + max(combo)
                break
            
        contiguous_len +=1
            
    return found_sum
    
print(day9_2())
