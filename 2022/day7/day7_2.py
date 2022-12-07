import aoc_helpers
import sys
sys.path.append('..')
from comms_device import Elf_Handheld

example = aoc_helpers.load_data('test.txt')
actual = aoc_helpers.load_data('actual.txt')

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.files = set()
        self.directories = set()

    def get_sub_dir(self, dir_name):
        dir = [dir for dir in self.directories if dir.name==dir_name][0]

        return dir

    @property
    def dir_size(self):
        size_files = sum([f.size for f in self.files])
        size_sub_dirs = sum([
            dir.dir_size for dir in self.directories if dir.dir_size
        ])

        total_size = size_files + size_sub_dirs

        return total_size




class File:
    def __init__(self, fname, size):
        self.fname = fname
        self.size = int(size)




class FileSystem:
    def __init__(self, stream):
        self.stream = stream
        self.root = Directory('/')
        self.cwd = self.root

    def cd(self, dirName):
        if dirName == '/':
            self.cwd = self.root

        elif dirName == '..':
            if self.cwd != self.root:
                self.cwd = self.cwd.parent

        else:
            self.cwd = self.cwd.get_sub_dir(dirName)

    def add_to_fs(self, line):
        attr, name = line.split()
        if line.startswith('dir '):
            self.cwd.directories.add(Directory(name, parent=self.cwd))
        else:
            self.cwd.files.add(File(name, attr))

    def process_stream(self):
        for line in self.stream:
            if line == '$ ls':
                continue
            elif line.startswith('$ cd '):
                dirName = line.split()[-1]
                self.cd(dirName)
            else:
                self.add_to_fs(line)

    


system = FileSystem(actual)
system.process_stream()


def part1():
    dirs_to_process = [system.root]
    sizes = []

    while len(dirs_to_process) > 0:
        dir = dirs_to_process.pop(0)

        sizes.append(dir.dir_size)

        for d in dir.directories:
            dirs_to_process.append(d)

    result = sum([s for s in sizes if s <= 100000])

    print(result)

    return sizes

sizes = part1()


def part2():
    unused_space = 70000000 - system.root.dir_size
    space_to_clear = 30000000 - unused_space

    big_enough = [s for s in sizes if s >= space_to_clear]

    print(min(big_enough))


part2()