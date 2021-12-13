import aoc_helpers

inputs = aoc_helpers.load_data('actual.txt')
split_idx = inputs.index('')

coords = [(int(i.split(',')[0]), int(i.split(',')[1])) for i in inputs[:split_idx]]
folds = inputs[split_idx+1:]

max_x = max(coords, key=lambda i: i[0])[0]
max_y = max(coords, key=lambda i: i[1])[1]

def generate_paper(x,y):
    paper = []
    for i in range(y+1):
        paper.append(['.']*(x+1))

    return paper

paper = generate_paper(max_x, max_y)

for c in coords:
    paper[c[1]][c[0]] = '#'

print('part1')

def fold(paper, fold):
    axis = fold[11:].split('=')[0]
    split_line = int(fold[11:].split('=')[1])

    p_max_y = len(paper)
    p_max_x = len(paper[0])

    output = None

    if axis == 'x':
        output = generate_paper(p_max_x - split_line - 2, p_max_y - 1)
        for i in range(1,split_line+1):
            c_neg = split_line - i
            c_plus = split_line + i

            for j in range(p_max_y):
                if paper[j][c_neg]=='#' or paper[j][c_plus]=='#':
                    output[j][split_line - i] = '#'
    else:
        output = generate_paper(p_max_x-1, p_max_y - split_line - 2)
        for i in range(1,split_line+1):
            r_neg = split_line - i
            r_plus = split_line + i

            for j in range(p_max_x):
                if paper[r_neg][j]=='#' or paper[r_plus][j]=='#':
                    output[split_line - i][j] = '#'

    return output

paper_1 = fold(paper, folds[0])
count = 0
for r in paper_1:
    for c in r:
        if c =='#':
            count +=1
print(count)

print('part2')

p_out = paper
for f in folds:
    p_out = fold(p_out, f)

for i in p_out:
    print(''.join(i))