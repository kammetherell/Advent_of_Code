with open("./inputs/day3.txt") as f:
    inputs = f.readlines()
inputs = [x.strip('\n') for x in inputs] 

def day3(right, down):
    row_num = 0
    posn = 0
    
    row_len = len(inputs[0])
    
    num_trees = 0
    
    while row_num < len(inputs) - 1:
        posn = posn + right
        row_num = row_num + down
        
        if posn > row_len -1:
            posn = posn - row_len
        
        row = inputs[row_num]
        locn = row[posn]
        
        if locn =='#':
            num_trees = num_trees + 1
            
    return num_trees
    
if __name__ == '__main__':
    print(day3(3,1))