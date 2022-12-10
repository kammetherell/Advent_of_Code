import aoc_helpers
import sys
# sys.path.append('..')
# from comms_device import Elf_Handheld

example = aoc_helpers.load_data('test.txt')
actual = aoc_helpers.load_data('actual.txt')


def part_1(input):
    head_coord=tail_coord = (0,0)

    tail_visited = {
        (0,0)
    }

    for i in input:
        [dir, amt] = i.split()

        if dir =='R':
            head_coords = [(head_coord[0]+i,head_coord[1]) for i in range(1,int(amt)+1)]
            head_coord = head_coords[-1]

            for h in head_coords:
                if (tail_coord[0] in [h[0]-1, h[0], h[0]+1]) and \
                    (tail_coord[1] in [h[1]-1, h[1], h[1]+1]):
                    continue
                else:
                    #Check if in same row as head
                    if tail_coord[1]==h[1]:
                        tail_coord = (tail_coord[0]+1, tail_coord[1])
                        tail_visited.add(tail_coord)
                    else:
                        tail_coord = (tail_coord[0]+1, h[1])
                        tail_visited.add(tail_coord)

        elif dir =='L':
            head_coords = [(head_coord[0]-i,head_coord[1]) for i in range(1,int(amt)+1)]
            head_coord = head_coords[-1]

            for h in head_coords:
                if (tail_coord[0] in [h[0]-1, h[0], h[0]+1]) and \
                    (tail_coord[1] in [h[1]-1, h[1], h[1]+1]):
                    continue
                else:
                    #Check if in same row as head
                    if tail_coord[1]==h[1]:
                        tail_coord = (tail_coord[0]-1, tail_coord[1])
                        tail_visited.add(tail_coord)
                    else:
                        tail_coord = (tail_coord[0]-1, h[1])
                        tail_visited.add(tail_coord)
        elif dir =='U':
            head_coords = [(head_coord[0],head_coord[1]+i) for i in range(1,int(amt)+1)]
            head_coord = head_coords[-1]

            for h in head_coords:
                if (tail_coord[0] in [h[0]-1, h[0], h[0]+1]) and \
                    (tail_coord[1] in [h[1]-1, h[1], h[1]+1]):
                    continue
                else:
                    #Check if in same col as head
                    if tail_coord[0]==h[0]:
                        tail_coord = (tail_coord[0], tail_coord[1]+1)
                        tail_visited.add(tail_coord)
                    else:
                        tail_coord = (h[0], tail_coord[1]+1)
                        tail_visited.add(tail_coord)
        elif dir =='D':
            head_coords = [(head_coord[0],head_coord[1]-i) for i in range(1,int(amt)+1)]
            head_coord = head_coords[-1]

            for h in head_coords:
                if (tail_coord[0] in [h[0]-1, h[0], h[0]+1]) and \
                    (tail_coord[1] in [h[1]-1, h[1], h[1]+1]):
                    continue
                else:
                    #Check if in same col as head
                    if tail_coord[0]==h[0]:
                        tail_coord = (tail_coord[0], tail_coord[1]-1)
                        tail_visited.add(tail_coord)
                    else:
                        tail_coord = (h[0], tail_coord[1]-1)
                        tail_visited.add(tail_coord)

    print(len(tail_visited))
part_1(actual)


class Rope:
    def __init__(self, length):
        self.coords = [(0,0)] * length

    def move(self, dir):
        head = self.coords[0]

        h_new_x = head[0]
        h_new_y = head[1]

        h_new_x += 1 if dir =='R' else -1 if dir =='L' else 0
        h_new_y += 1 if dir =='U' else -1 if dir =='D' else 0

        new_coords = []

        new_coords.append((h_new_x, h_new_y))

        for i in range(1,len(self.coords)):
            prev_knot = new_coords[i-1]
            curr_knot = self.coords[i]

            diff_x = abs(prev_knot[0]-curr_knot[0])
            diff_y = abs(prev_knot[1]-curr_knot[1])

            if diff_x > 1 or diff_y > 1:
                #curr_knot neeeds to move
                curr_knot = (curr_knot[0], curr_knot[1])

                #Check if in same col (must be up or down)
                if diff_x==0:
                    if curr_knot[1] < prev_knot[1]:
                        curr_knot = (curr_knot[0], curr_knot[1]+1)
                    else:
                        curr_knot = (curr_knot[0], curr_knot[1]-1)
                        
                #Check if in same col (must be L or R)
                elif diff_y==0:
                    if curr_knot[0] < prev_knot[0]:
                        curr_knot = (curr_knot[0]+1, curr_knot[1])
                    else:
                        curr_knot = (curr_knot[0]-1, curr_knot[1])
                
                else:
                    # Tail must move diagonally
                    if curr_knot[0] < prev_knot[0]:
                        curr_knot_new_x = curr_knot[0] + 1
                    else:
                        curr_knot_new_x = curr_knot[0] - 1

                    if curr_knot[1] < prev_knot[1]:
                        curr_knot_new_y = curr_knot[1] + 1
                    else:
                        curr_knot_new_y = curr_knot[1] - 1

                    curr_knot = (curr_knot_new_x, curr_knot_new_y)

            new_coords.append(curr_knot)

        self.coords = new_coords.copy()




def part_2(input):
    rope = Rope(10)

    tail_visited = set()

    tail_visited.add(rope.coords[-1])

    for i in input:
        [dir, amt] = i.split()

        for n in range(int(amt)):
            rope.move(dir)
            tail_visited.add(rope.coords[-1])


    print(len(tail_visited))
    

example_2 = aoc_helpers.load_data('test2.txt')
part_2(actual)