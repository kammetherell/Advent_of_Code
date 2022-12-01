from datetime import datetime
from collections import deque

class computer :
    _i_o_mode = 'manual' #auto

    def reset(self, reset_programme = True):
        if reset_programme:
            self._programme = ""

        self._complete = False
        self._running = False

        self._err = None
        self._cursor = 0
        self._loop_count = 0
        self._start_time = None
        self._end_time = None
        self._elapsed = None
        self._debug_new_line = True

        self._inputs = deque([])
        self._awaiting_input = False
        self._outputs = deque([])
        self._relative_base = 0

    def __init__(self, debug = False):
        self.reset()
        self.debug = debug
        today = datetime.now().strftime('%Y%b%d_T%H%M')
        self._debug_file = f'debug_{today}.txt'

    def print_debug(self,status):
        end = '\n'
        if not self._debug_new_line and self.debug:
            end = '\r'

        if self.debug == 'console':
                print(status, end=end)
        elif self.debug == 'file':
            with open(self._debug_file, 'a') as f:
                f.write(status + '\n')
        elif self.debug == 'prompt':
            proceed = input(f'{status}\nPress enter to continue')

    def load(self, programme):
        self._programme = [int(i) for i in programme.strip().split(',')]

    def load_from_file(self, file):
        with open(file) as f:
            input = f.readlines()[0]

        self._programme = [int(i) for i in input.strip().split(',')]

    def save_noun(self,noun):
        self._programme[1] = noun
        self.print_debug(f'Noun set to {noun}')

    def save_verb(self, verb):
        self._programme[2] = verb
        self.print_debug(f'Verb set to {verb}')

    def add_input(self, input):
        self._inputs.append(input)
        self.print_debug(f'New Input added: {input}')
        if self._awaiting_input and not self._complete:
            self._awaiting_input = False
            self._resume()

    def get_output(self):
        if len(self._outputs)>0:
            return self._outputs.popleft()
        else:
            return None

    def _get_operation(self):
        input = self._programme[self._cursor]

        input_decoded = []
        while input != 0:
            input_decoded.append(input % 10)
            input = input // 10

        #max complete length would be 5
        input_decoded = input_decoded + [0]*(5-len(input_decoded))        
        input_decoded = [int(str(input_decoded[1])+str(input_decoded[0]))] + input_decoded[2:]

        opcode = input_decoded[0]
        pos_modes = input_decoded[1:]

        return opcode, pos_modes

    def _prog_idx_exists(self, idx):
        if idx >= len(self._programme):
            self._programme = self._programme + [0] * (idx + 1 - len(self._programme))
            return True
        elif idx < 0:
            raise Exception(f'Attempting to read negative programme index: {idx}')
        else:
            return True

    def _get_params(self, pos_modes):
        parameters = []

        for idx, i in enumerate(pos_modes):
            val = self._programme[self._cursor + 1 + idx]
            if i == 0 and self._prog_idx_exists(val):
                #Position mode
                parameters.append(self._programme[val])

            elif i==2:
                self.print_debug(f'Relative mode test (Base: {self._relative_base} input: {val}')
                #Relative Mode
                if self._prog_idx_exists(self._relative_base + val):
                    parameters.append(self._programme[self._relative_base + val])
            
            else: #i==1
                #Immediate Mode
                parameters.append(val)

        return parameters

    def _save_value(self, value, idx):
        if self._prog_idx_exists(idx):
            self._programme[idx] = value
            self.print_debug(f'{value} saved to position {idx}')
        else:        
            raise Exception(f'Attempt to write {value} to index {idx} failed: Index out of range')

    def _move_cursor(self,num):
        self._cursor += num

    def _pause(self):
        self.print_debug('Pausing')
        self._running = False
    
    def _resume(self):
        self.print_debug('Resuming')
        self._running = True
        self.run()

    def _finished(self):
        self._complete = True
        self._running = False
        self._end_time = datetime.now()
        self._elapsed = self._end_time - self._start_time
        self.print_debug(f'**FINISHED** Output: {self._programme[0]}\n')

    def _print_err(self):
        self._complete = True
        self._running = False
        self._end_time = datetime.now()
        self._elapsed = self._end_time - self._start_time
        self.print_debug(f'ERROR OCCURRED on loop {self._loop_count}')
        self.print_debug(f'err message: {self._err}')
        
        
    def run(self):
        self._start_time = datetime.now()
        self._complete = False
        self._running = True

        try:
            while not self._complete and self._running and self._cursor < len(self._programme):
                self.print_debug(f'Loop:{self._loop_count}')
                opcode, pos_modes = self._get_operation()
                self.print_debug(f'Opcode: {opcode}; Pos Modes: {pos_modes}')

                if opcode==99:
                    self._finished()
                    return 

                elif opcode in [1,2,7,8]:
                    parameters = self._get_params(pos_modes[:2] + [1])
                    self.print_debug(f'Parameters: {parameters}')

                    input_1 = parameters[0]
                    input_2 = parameters[1]
                    output_idx = parameters[2]

                    value = None

                    #add
                    if opcode == 1:
                        value = input_1 + input_2
                    #multiply
                    elif opcode == 2:
                        value = input_1 * input_2
                    #less than
                    elif opcode == 7:
                        value = int(input_1 < input_2)
                    #equals
                    elif opcode == 8:
                        value = int(input_1==input_2)

                    self._move_cursor(4)
                    self._save_value(value, output_idx)
                
                elif opcode==3:
                    dest = self._get_params(pos_modes[:1])[0]
                    self.print_debug(f'Parameters: {dest}')
                    value = None
                    if self._i_o_mode=='manual':
                        value = int(input('Please enter your input:'))
                        self._move_cursor(2)
                        self._save_value(value,dest)
                    else:
                        if len(self._inputs) > 0:
                            self.print_debug(f'Reading input from stored inputs: {self._inputs}')
                            value = self._inputs.popleft()
                            self._move_cursor(2)
                            self._save_value(value,dest)
                        else:
                            self.print_debug(f'Waiting for input')
                            self._awaiting_input = True
                            self._pause()
                    
                elif opcode==4:
                    value = self._get_params(pos_modes[:1])[0]
                    if self._i_o_mode=='manual':
                        print(f'output: {value}')
                    else:
                        self.print_debug(f'output: {value}')
                        self._outputs.append(value)
                    
                    self._move_cursor(2)

                elif opcode in [5,6]:
                    #Jump
                    parameters = self._get_params(pos_modes[:2])
                    self.print_debug(f'Parameters: {parameters}')

                    if (opcode==5 and parameters[0] != 0) or (opcode==6 and parameters[0]==0):
                        self._cursor = parameters[1]
                    else:
                        self._move_cursor(3)

                elif opcode == 9:
                    parameters = self._get_params(pos_modes[:1])
                    self.print_debug(f'Parameters: {parameters}')
                    self._relative_base += parameters[0]
                    self.print_debug(f'New Relative Base: {self._relative_base}')
                    self._move_cursor(2)
    
                else:
                    raise Exception(f'Invalid Opcode received at position {self._cursor}: {opcode} ')
                             
                self._loop_count += 1
        except Exception as e:
            self._err = e
            self._print_err()
