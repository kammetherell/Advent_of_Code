from computer import computer
import itertools
import tqdm

perms = itertools.permutations([0,1,2,3,4])

max_signal = 0

comp = computer(debug='file')
comp._i_o_mode = 'auto'

for p in tqdm.tqdm(perms, ascii=True):
    out = 0
    for phase in p:
        comp.reset(reset_programme=True)
        comp.load_from_file('actuals/day7')
        comp.add_input(phase)
        comp.add_input(out)
        comp.run()

        out = comp.get_output()
    if out > max_signal:
        max_signal = out

print(max_signal)

print('part2')

perms_2 = itertools.permutations([5,6,7,8,9])

max_signal_2 = 0
max_signal_phase_setting = []

def all_complete(comps):
    completed = True
    for k, amp in comps.items():
        if amp['comp']._complete:
            print(f'Amp {k} Complete')
        completed = completed * amp['comp']._complete

    return completed

for idx, phase_setting in enumerate(tqdm.tqdm(perms_2)):
    #reset amps for each permutation
    amplifiers = {
        'a': {'comp': computer(debug='file'), 'started':False, 'phs_idx':0, 'completed':False},
        'b': {'comp': computer(debug='file'), 'started':False, 'phs_idx':1, 'completed':False},
        'c': {'comp': computer(debug='file'), 'started':False, 'phs_idx':2, 'completed':False},
        'd': {'comp': computer(debug='file'), 'started':False, 'phs_idx':3, 'completed':False},
        'e': {'comp': computer(debug='file'), 'started':False, 'phs_idx':4, 'completed':False},
    }

    last_out = 0

    while True:
        for k, amp in amplifiers.items():
            if not amp['started']:
                amp['comp'].load_from_file('actuals/day7')
                amp['comp']._debug_file = f'AMP-{k}-d7p2.txt'
                amp['comp'].add_input(phase_setting[amp['phs_idx']])
                amp['comp']._debug_output_mode = 'file'
                amp['comp']._i_o_mode = 'auto'
                amp['comp'].run()
                amp['started'] = True
            
            amp['comp'].add_input(last_out)

            last_out = amp['comp'].get_output()

            if amp['comp']._complete:
                amp['completed'] = True

            if all([amp['completed'] for k, amp in amplifiers.items()]):
                # print('all amps completed')
                break

        if all([amp['completed'] for k, amp in amplifiers.items()]):
            if last_out > max_signal_2:
                max_signal_2 = last_out
                max_signal_phase_setting = phase_setting
            break
    
print(max_signal_2)
print(max_signal_phase_setting)




    