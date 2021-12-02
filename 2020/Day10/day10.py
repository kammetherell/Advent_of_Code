with open("./Advent_of_Code/Day10/input.txt") as f:
    inputs = f.readlines()
inputs = [x.strip('\n') for x in inputs] 
inputs = [int(x) for x in inputs] 
inputs.sort()

def day10_1():
    num_1_gap = 0
    num_3_gap = 1 # For end gap to device
    
    for idx, i in enumerate(inputs):
        if idx == 0:
            gap = i - 0
        else:
            gap = i - inputs[idx-1]
            
        if gap == 1:
            num_1_gap +=1
        if gap == 3:
            num_3_gap +=1
                
    return num_1_gap, num_3_gap
    
num1, num2 = day10_1()

print('===PART1===')

print(num1, num2)
print(num1 * num2)

print('===PART2===')

def day10_2():
    num_path_adapters = {
        0: 1
    }

    for adapter in inputs:
        num_path_adapters[adapter] = 0
        for possible_adapter in range(adapter - 3, adapter):
            if possible_adapter == 0 or possible_adapter in inputs:
                num_path_adapters[adapter] += num_path_adapters[possible_adapter]
    
    return num_path_adapters[max(inputs)]

print(day10_2())