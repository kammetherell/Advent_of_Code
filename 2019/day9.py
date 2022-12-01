from computer import computer
import itertools
import tqdm

comp = computer(debug="file")
comp._i_o_mode = 'auto'

# tests = [
#     "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99",# takes no input and produces a copy of itself as output.
#     "1102,34915192,34915192,7,4,7,99,0", # should output a 16-digit number.
#     "104,1125899906842624,99" #should output the large number in the middle
# ]

# for t in tests:
#     comp.reset()
#     comp.load(t)
#     comp.add_input(1)

#     comp.run()

#     print(list(comp._outputs))

comp = computer(debug='file')
comp._i_o_mode = 'auto'
comp.load_from_file('actuals/day9')
comp.add_input(1)
comp.run()

print(list(comp._outputs))