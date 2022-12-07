import re

class Elf_Handheld:
    def __init__(self, datastream):
        self.datastream = datastream

    def get_marker(self, marker_len):
        marker_found = False
        start_char = marker_len

        while not marker_found:
            sub_str = self.datastream[start_char-marker_len:start_char]

            valid = True

            for char in sub_str:
                if sub_str.count(char)>1:
                    valid=False

            if valid:
                marker_found = True
            else: start_char +=1

        return start_char

    def get_start_marker(self):
        return self.get_marker(4)

    def get_msg_marker(self):
        return self.get_marker(14)

    def load_file_system(self, output):
        dir = {
            'files': [],
            'path' : []
        }

        cwd = dir

        for line in output:
            #return to home
            if '$ cd /' in line:
                cwd = dir
            elif '$ cd ..' in line:
                None
            elif '$ cd' in line:
                cwd = cwd[line[5:]]
            elif '$ ls' in line:
                None
            elif 'dir ' in line:
                path = cwd['path'] + [line[4:]]
                cwd[line[4:]] = {
                    'files':[],
                    'path': path
                }
            else:
                cwd['files'].append(tuple(line.split(' ')))