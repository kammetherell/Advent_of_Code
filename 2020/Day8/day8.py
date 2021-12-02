with open("./Advent_of_Code/Day8/input.txt") as f:
    inputs = f.readlines()
inputs = [x.strip('\n') for x in inputs] 
inputs = [i.split(' ') for i in inputs]

print('===PART1===')

def day8_1():
    accumulator = 0
    idx = 0
    
    idx_run = []
    
    while idx not in idx_run:
        step_type = inputs[idx][0]
        val = int(inputs[idx][1])
        idx_run.append(idx)
        
        if step_type == 'acc':
            accumulator += val
            
        if step_type =='jmp':
            idx += val
        else:
            idx+=1
            
    return accumulator
    
print(day8_1())

print('===PART2===')

def day8_2():
    altered = []
    
    finished = False
    
    while not finished:
        accumulator = 0
        idx = 0
        idx_run = []
        
        inst_changed = False
        
        while idx not in idx_run:
            #Add step to run list
            idx_run.append(idx)
            
            #Check if we're at the end
            if idx >= len(inputs):
                # normal termination!#
                finished = True
                break
            
            #decode step
            step_type = inputs[idx][0]
            val = int(inputs[idx][1])
            
            #If acc step type add value and move on
            if step_type == 'acc':
                accumulator += val
                idx+=1
                
            # If jmp type, try swapping to nop only 
            # if we haven't swapped anything before
            if step_type == 'jmp':
                if not inst_changed and idx not in altered:
                    altered.append(idx)
                    inst_changed = True
                    idx +=1
                else:
                    idx += val
            
            if step_type == 'nop':
                if not inst_changed and idx not in altered:
                    altered.append(idx)
                    inst_changed = True
                    idx += val
                else:
                    idx += 1
                    
    return accumulator
    
print(day8_2())
                
        