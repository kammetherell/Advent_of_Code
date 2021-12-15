from datetime import datetime

class computer :
    _programme = ""
    _complete = False
    _err = None
    _cursor = 0
    _loop_count = 0
    _start_time = None
    _end_time = None
    _elapsed = None

    def __init__(self, debug = False):
        self.debug = debug

    def print_debug(self,status):
        if self.debug == 'log':
            print(status, end='\r')
        elif self.debug == 'prompt':
            proceed = input(f'{status}\nPress any key to continue')
    
    def reset(self):
        self._programme = ""
        self._complete = False
        self._err = None
        self._cursor = 0
        self._loop_count = 0
        self._start_time = None
        self._end_time = None
        self._elapsed = None

    def load(self, programme):
        self._programme = [int(i) for i in programme.strip().split(',')]

    def load_from_file(self, file):
        with open(file) as f:
            input = f.readlines()[0]

        self._programme = [int(i) for i in input.strip().split(',')]
    
    def save_noun(self,noun):
        self._programme[1] = noun
        self.print_debug(f'Noun set to {noun}\n')

    def save_verb(self, verb):
        self._programme[2] = verb
        self.print_debug(f'Verb set to {verb}\n')

    def _get_instruction(self):
        opcode = self._programme[self._cursor]
        parameters = self._programme[self._cursor + 1: self._cursor + 4]
        return (opcode, parameters)

    def _save_value(self, value, idx):
        if idx < len(self._programme):
            self._programme[idx] = value
        else:        
            raise Exception(f'Attempt to write {value} to index {idx} failed: Index our of range')

    def _finished(self):
        self._end_time = datetime.now()
        self._elapsed = self._end_time - self._start_time
        self.print_debug(f'\n**FINISHED** Output: {self._programme[0]}\n')

    def _print_err(self):
        self._complete = True
        self._end_time = datetime.now()
        self._elapsed = self._end_time - self._start_time
        print(f'ERROR OCCURRED on loop {self._loop_count}')
        print(f'err message: {self._err}')
        
    def run(self):
        self._start_time = datetime.now()
        self._complete = False

        try:
            while not self._complete and self._cursor < len(self._programme):
                opcode, parameters = self._get_instruction()
                self.print_debug(f'Loop:{self._loop_count}; Opcode:{opcode}; Parameters:{parameters}')

                increment = None

                if opcode==99:
                    self._complete = True
                    self._finished()
                    return 

                elif opcode in [1,2]:
                    input_1 = self._programme[parameters[0]]
                    input_2 = self._programme[parameters[1]]
                    output_idx = parameters[2]

                    value = None

                    if opcode == 1:
                        value = input_1 + input_2
                    elif opcode == 2:
                        value = input_1 * input_2

                    increment = 4

                    self._save_value(value, output_idx)
    
                else:
                    raise Exception(f'Invalid Opcode received at position {self._cursor}: {opcode} ')
                
                self._cursor += increment              
                self._loop_count += 1
        except Exception as e:
            self._err = e
            self._print_err()
