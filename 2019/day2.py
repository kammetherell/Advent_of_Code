from computer import computer

comp = computer(debug='log')

comp.load_from_file('actuals/day2')
comp._debug_output_mode = 'file'
comp.save_noun(12)
comp.save_verb(2)
comp.run()

print(f'part1: {comp._programme[0]}')

# found = False

# for n in range(100):
#     for v in range (100):
#         comp.reset()
#         comp.load_from_file('actuals/day2')
#         comp.save_noun(n)
#         comp.save_verb(v)
#         comp.run()

#         if comp._programme[0] == 19690720:
#             print(f'Noun:{n}; Verb:{v}')
#             break