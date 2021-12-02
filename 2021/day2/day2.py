import aoc_helpers

inputs = aoc_helpers.load_data('actual.txt')

inputs = [{'dir':i.split(' ')[0],'quant':int(i.split(' ')[1])} for i in inputs]
# print(inputs)
print('part1')
depth=0
x=0

for i in inputs:
    if i['dir']=='forward':
        x+=i['quant']
    elif i['dir']=='down':
        depth+=i['quant']
    elif i['dir']=='up':
        depth-=i['quant']

print(f'x:{x}; depth:{depth}; result:{x*depth}')

print('part2')

depth = 0
x = 0
aim = 0

for i in inputs:
    if i['dir']=='forward':
        x+=i['quant']
        depth = depth + aim*i['quant']
    elif i['dir']=='down':
        aim+=i['quant']
    elif i['dir']=='up':
        aim-=i['quant']

print(f'x:{x}; depth:{depth};aim:{aim}; result:{x*depth}')