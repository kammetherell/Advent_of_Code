from itertools import product
with open("./Day14/input.txt") as f:
    inputs = f.readlines()
inputs = [x.strip('\n') for x in inputs]

def mask_num(mask, num):
    mask_len = len(mask)
    num_bin = str(format(num, f'#038b')[2:])

    result_masked = ''

    for idx, char in enumerate(mask):
        if char == 'X':
            result_masked += num_bin[idx]
        else:
            result_masked += char

    return result_masked

def day14_1():
    mem = {}
    mask = ''

    for input in inputs:
        ins_type, ins_val = input.split(' = ')
        if ins_type == 'mask':
            mask = ins_val
        else:
            mem_pos = ins_type[4:-1]
            mem[mem_pos] = int(mask_num(mask, int(ins_val)),2)

    return sum(mem.values())

print(day14_1())

def get_mem_options(mask, num):
    num_bin = str(format(num, f'#038b')[2:])
    result_masked = ''
    mem_opts = []

    for idx, char in enumerate(mask):
        if char == '0':
            result_masked += num_bin[idx]
        else:
            result_masked += char

    num_x = result_masked.count('X')
    
    iterations = []
    for i in product([0, 1], repeat=num_x):
        iterations.append(i)

    for iteration in iterations:
        temp_opt_bin = result_masked
        for i in range(len(iteration)):
            temp_opt_bin = temp_opt_bin.replace('X', str(iteration[i]), 1)
        
        temp_opt_dec = int(temp_opt_bin, 2)

        mem_opts.append(temp_opt_dec)
        
    return mem_opts

def day14_2():
    mem = {}
    mask = ''

    for input in inputs:
        ins_type, ins_val = input.split(' = ')
        if ins_type == 'mask':
            mask = ins_val
        else:
            mem_pos = ins_type[4:-1]
            mem_opts = get_mem_options(mask, int(mem_pos))
            for pos in mem_opts:
                mem[pos] = int(ins_val)

    return sum(mem.values())

print(day14_2())