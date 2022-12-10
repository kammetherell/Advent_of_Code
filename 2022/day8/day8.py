import aoc_helpers
import sys
sys.path.append('..')
from comms_device import Elf_Handheld

example = aoc_helpers.load_data('test.txt')
actual = aoc_helpers.load_data('actual.txt')

def prep_data(input):
    output = []
    for y_idx, line in enumerate(input):
        for x_idx, val in enumerate([int(x) for x in line]):
            output.append(
                (x_idx, y_idx, val)
            )

    return output

example = prep_data(example)
actual = prep_data(actual)

def part_1(input):
    max_x = max([i[0] for i in input])
    max_y = max([i[1] for i in input])

    count_visible = 0

    for x in range(max_x+1):
        for y in range(max_y+1):
            if x in [0, max_x] or y in [0,max_y]:
                count_visible+=1
                #print(f'Tree at ({x},{y}), is visible (edge)')
            else:
                val = [tree[2] for tree in input if tree[0]==x and tree[1]==y][0]

                left = max([tree[2] for tree in input if tree[0]<x and tree[1]==y])
                right = max([tree[2] for tree in input if tree[0]>x and tree[1]==y])
                up = max([tree[2] for tree in input if tree[0]==x and tree[1]<y])
                down = max([tree[2] for tree in input if tree[0]==x and tree[1]>y])

                if val > left or val > right or val > up or val > down:
                    count_visible+=1
                    #print(f'Tree at ({x},{y}), height {val} is visible')

    print(count_visible)

#part_1(actual)

def get_view_distance(height, direction_list):
    count = 0
    stop = False
    i=0

    while not stop and i<len(direction_list):
        count+=1
        if height > direction_list[i]:    
            i+=1
        else:
            stop = True

    return count



def part_2(input):
    max_x = max([i[0] for i in input])
    max_y = max([i[1] for i in input])

    max_score = 0

    for x in range(1,max_x):
        for y in range(1,max_y):
            val = [tree[2] for tree in input if tree[0]==x and tree[1]==y][0]

            left = [tree[2] for tree in input if tree[0]<x and tree[1]==y]
            right = [tree[2] for tree in input if tree[0]>x and tree[1]==y]
            up = [tree[2] for tree in input if tree[0]==x and tree[1]<y]
            down = [tree[2] for tree in input if tree[0]==x and tree[1]>y]


            left.reverse()
            up.reverse()

            left_score = get_view_distance(val, left)
            right_score = get_view_distance(val, right)
            up_score = get_view_distance(val, up)
            down_score = get_view_distance(val, down)

            score = left_score * right_score * up_score * down_score
            if score > max_score:
                max_score = score

            if x==2 and y==1:
                print(left_score, right_score, up_score, down_score, score)

    
    print(max_score)

part_2(actual)