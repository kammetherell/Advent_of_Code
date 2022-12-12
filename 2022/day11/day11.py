import aoc_helpers
import sys
import math
# sys.path.append('..')
# from comms_device import Elf_Handheld

example = aoc_helpers.load_data('test.txt')
actual = aoc_helpers.load_data('actual.txt')

class Monkey:
    def __init__(self):
        self.items_inspected = 0
        self.name = 'No Name'
        self.items = []
        self.limiter = None

    def __str__(self):
        return f'Monkey name is {self.name}; items: {self.items}'
    def __repr__(self):
        return f'Monkey(name={self.name}; items: {self.items})'

    def inspect_item(self):
        old = int(self.items.pop(0))


        new = eval(self.oper)

        if self.limiter is not None:
            new %= self.limiter
        else:
            new = new/3

        test_outcome = (new%self.test == 0)

        if test_outcome:
            #print(f'item of worry {new} thrown from {self.name} to {self.true_dest.name}')
            self.true_dest.items.append(new)
        else:
            #print(f'item of worry {new} thrown from {self.name} to {self.false_dest.name}')
            self.false_dest.items.append(new)

        self.items_inspected += 1

    def inspect_all(self):
        for _ in range(len(self.items)):
            self.inspect_item()



def prep_monkeys(input, limiter=False):
    input = list(filter(lambda i: (i!=''),input))
    num_monkeys = int(len(input)/6)

    tests = []

    monkeys = []
    for i in range(num_monkeys):
        monkeys.append(Monkey())

    for i in range(num_monkeys):
        start_row = i*6

        monkeys[i].name = f'Monkey {i}'

        start_items = input[start_row+1].split(': ')[1].split(', ')
        start_items = [int(i) for i in start_items]
        monkeys[i].items = start_items

        oper = input[start_row+2].split(' = ')[1]
        monkeys[i].oper = oper

        test = int(input[start_row+3].split('divisible by ')[1])
        tests.append(test)
        monkeys[i].test = test

        true_dest = int(input[start_row+4].split('monkey ')[1])
        false_dest = int(input[start_row+5].split('monkey ')[1])

        monkeys[i].true_dest = monkeys[true_dest]
        monkeys[i].false_dest = monkeys[false_dest]

    if limiter:
        factor = math.lcm(*tests)
        for i in range(num_monkeys):
            monkeys[i].limiter = factor

    return monkeys

monkeys = prep_monkeys(actual)
print(monkeys)

num_rounds = 20
for round in range(num_rounds):
    for monkey in monkeys:
        monkey.inspect_all()

item_counts = [m.items_inspected for m in monkeys]
item_counts.sort(reverse=True)
print(item_counts[0]*item_counts[1])

monkeys = prep_monkeys(actual, True)
num_rounds = 10000
for round in range(num_rounds):
    for monkey in monkeys:
        monkey.inspect_all()

item_counts = [m.items_inspected for m in monkeys]
item_counts.sort(reverse=True)
print(item_counts[0]*item_counts[1])
