import aoc_helpers

example = aoc_helpers.load_data('test.txt')
actual = aoc_helpers.load_data('actual.txt')

def get_span(elf):
    [start, end] = elf.split('-')

    span = [i for i in range(int(start), int(end)+1)]

    return span


def check_overlap(pair):
    [elf_1, elf_2] = pair.split(',')
    elf_1_span = get_span(elf_1)
    elf_2_span = get_span(elf_2)

    overlap = False

    if all(i in elf_1_span for i in elf_2_span) or all(i in elf_2_span  for i in elf_1_span):
        overlap = 'Full'

    elif any(i in elf_1_span for i in elf_2_span) or any(i in elf_2_span  for i in elf_1_span):
        overlap = 'Partial'

    return overlap

def part_1(input):
    count=0

    for i in input:
        if check_overlap(i)=='Full':
            count +=1

    return count

print(part_1(actual))


def part_2(input):
    count=0

    for i in input:
        if check_overlap(i) in ['Partial', 'Full']:
            count +=1

    return count


print(part_2(actual))