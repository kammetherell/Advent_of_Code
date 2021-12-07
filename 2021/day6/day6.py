from datetime import datetime
import numpy as np
start = datetime.now()

test = [3,4,3,1,2]
actual = [5,1,1,4,1,1,4,1,1,1,1,1,1,1,1,1,1,1,4,2,1,1,1,3,5,1,1,1,5,4,1,1,1,2,2,1,1,1,2,1,1,1,2,5,2,1,2,2,3,1,1,1,1,1,1,1,1,5,1,1,4,1,1,1,5,4,1,1,3,3,2,1,1,1,5,1,1,4,1,1,5,1,1,5,1,2,3,1,5,1,3,2,1,3,1,1,4,1,1,1,1,2,1,2,1,1,2,1,1,1,4,4,1,5,1,1,3,5,1,1,5,1,4,1,1,1,1,1,1,1,1,1,2,2,3,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,5,1,1,1,1,4,1,1,1,1,4,1,1,1,1,3,1,2,1,2,1,3,1,3,4,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,4,1,1,2,2,1,2,4,1,1,3,1,1,1,5,1,3,1,1,1,5,5,1,1,1,1,2,3,4,1,1,1,1,1,1,1,1,1,1,1,1,5,1,4,3,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,3,3,1,2,2,1,4,1,5,1,5,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,4,3,1,1,4]

num_days = 80
day = 1

fishes = np.array(actual)

def count_fishes(start, num_days):
    day = 1

    fish_count = {}

    for life in range(9):
        fish_count[life] = len([i for i in start if i==life])

    while day <= num_days:
        print(f'Day {day}', end='\r')

        new_fish_count = {
            0:0,
            1:0,
            2:0,
            3:0,
            4:0,
            5:0,
            6:0,
            7:0,
            8:0
        }
        
        for l in range(9):
            if l==0:
                new_fish_count[6] = new_fish_count[8] = fish_count[0]
            else:
                new_fish_count[l-1] = new_fish_count[l-1] + fish_count[l]

        fish_count = new_fish_count

        day+=1
    
    sum_fishes = sum([v for v in fish_count.values()])
    
    return sum_fishes

print('part1')
print(count_fishes(fishes, 80))
print('part2')
print(count_fishes(fishes, 256))

end = datetime.now()

print(f'took {end-start}')
