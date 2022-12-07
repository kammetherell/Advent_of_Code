import aoc_helpers
import sys
sys.path.append('..')
from comms_device import Elf_Handheld

example = aoc_helpers.load_data('test.txt')
actual = aoc_helpers.load_data('actual.txt')

def load_file_system(stream):
    files = []
    dirs = []
    cwd = []

    for line in stream:
        #return to home
        if '$ cd /' in line:
            cwd = ['/']
        elif '$ cd ..' in line:
            cwd.pop()
        elif '$ cd ' in line:
            cwd.append(line.split()[-1])
        elif '$ ls' in line:
            None
        elif 'dir ' in line:
            dirs.append(
                {
                    'dir_name': line.split()[-1],
                    'path':cwd.copy() + [line.split()[-1]]
                }
            )
            None
        else:
            files.append(
                {
                    'file_name': line.split()[-1],
                    'size': int(line.split()[0]),
                    'path': cwd.copy()
                }
            )

    for dir in dirs:
        dir_files = [
            f for f in files if all(
                p in f['path'] for p in dir['path']
                )
            ]
        
        dir['total_size'] = sum(f['size'] for f in dir_files)

    return dirs, files

dirs, files = load_file_system(example)

print(sum([d['total_size'] for d in dirs if d['total_size']<=100000]))
