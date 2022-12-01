from computer import computer

comp = computer(debug='log')

comp.load_from_file('actuals/day5')
comp._debug_output_mode = 'file'
comp.run()