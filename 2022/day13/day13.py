import aoc_helpers
import networkx as nx

example = aoc_helpers.load_data('test.txt')
actual = aoc_helpers.load_data('actual.txt')

class Pair:
    def __init__(self, packet_1, packet_2):
        self.packet_1 = eval(packet_1)
        self.packet_2 = eval(packet_2)
        #print(self.packet_1, self.packet_2)

        self.correct_order = self.compare_list(
            self.packet_1, self.packet_2
        )

        #print(self.correct_order)

    def compare_list(self, list1, list2):
        #Loop through all elements in packet_1 (Left)
        for i in range(len(list1)):
            left_el = list1[i]
            #if right list runs out of elements order is incorrect
            if i > len(list2) - 1:
                return -1 #Incorrect order
            else:
                right_el = list2[i]
                #Check if left item is int
                if type(left_el)==int:
                    if type(right_el)==int:
                        #Left greater than right = incorrect
                        if left_el > right_el:
                            return -1
                        #left el less than right = correct
                        elif left_el < right_el:
                            return 1
                        else:
                            #No decision can be made - continue
                            continue
                    else:
                        compare_subs = self.compare_list(
                            [left_el], right_el
                        )

                        #if 0, no decision made, continue
                        if compare_subs == 0:
                            continue
                        #Else return the order decision
                        else:
                            return compare_subs
                #If left item is list
                elif type(left_el)==list:
                    if type(right_el)==int:
                        compare_subs = self.compare_list(
                            left_el, [right_el]
                        )
                    else:
                        compare_subs = self.compare_list(
                            left_el, right_el
                        )

                    #if 0, no decision made, continue
                    if compare_subs == 0:
                        continue
                    #Else return the order decision
                    else:
                        return compare_subs
        #finished looping, no decision made, but right still has elements - correct
        if len(list1) < len(list2):
            return 1
        #else no decision made, return 0
        return 0

def part_1(input):
    num_pairs = len(list(filter(lambda x: x=='', input))) + 1
    
    pairs = []
    idx_sum = 0


    for i in range(num_pairs):
        pair = Pair(
            input[3*i],
            input[3*i +1]
            )

        if pair.correct_order == 1:
            idx_sum += (i+1)
        
        pairs.append(pair)
    print(idx_sum)
    return pairs


pairs = part_1(actual)

def part_2(input):
    sorted = False
    input = list(filter(lambda x: x!='', input))
    input.append('[[2]]')
    input.append('[[6]]')

    while not sorted:
        changes = 0

        #Bubble Sort
        for i in range(1, len(input)):
            left = input[i-1]
            right = input[i]

            #print(f'Comparing: {left}, {right}')

            pair = Pair(left, right)

            if pair.correct_order == -1:
                #incorrect order - must swap
                input[i] = left
                input[i-1]= right
                changes +=1

        if changes==0:
            sorted = True

    index_2 = input.index('[[2]]')+1
    index_6 = input.index('[[6]]')+1

    print(index_2 * index_6)

part_2(actual)