import aoc_helpers
import sys
# sys.path.append('..')
# from comms_device import Elf_Handheld

example = aoc_helpers.load_data('test.txt')
actual = aoc_helpers.load_data('actual.txt')

example_small = [
    'noop',
    'addx 3',
    'addx -5',
]

class Screen:
    def __init__(self, signal):
        self.signal = signal
        self.outputs = []

    def run_program(self):
        loop=1
        x=1

        for sig in self.signal:
            
            if sig=='noop':
                sig_strength = loop * x
                self.outputs.append((loop,x,sig_strength))
                loop +=1

            else:
                sig_strength = loop * x
                self.outputs.append((loop,x,sig_strength))
                loop +=1
                

                sig_strength = loop * x
                self.outputs.append((loop,x,sig_strength))
                loop+=1
                x+=int(sig.split()[-1])
    
    def print_output(self, debug=False):
        full_out = []
        line = ''
        adjustment = 0
        for i in range(240):
            x_val = self.outputs[i][1]
            if debug:
                print(f'CRT @ posn {i}; X={x_val}')
            diff = abs((i-adjustment) - x_val)
            pixel = '.'
            if diff <=1:
                pixel = '#'
                if debug:
                    print('Adding Pixel')

            line+=pixel

            if len(line) == 40:
                full_out.append(line)
                adjustment +=40
                line = ''
                if debug:
                    print('starting new line')

        for line in full_out:
            print(line)



screen = Screen(actual)
screen.run_program()

care_about = [20, 60, 100, 140, 180, 220]

strengths = [i for i in screen.outputs if i[0] in care_about]

print(sum([i[2] for i in strengths]))

screen.print_output(True)

