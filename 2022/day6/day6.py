import aoc_helpers
import sys
sys.path.append('..')
from comms_device import Elf_Handheld

example = aoc_helpers.load_data('test.txt')
actual = aoc_helpers.load_data('actual.txt')

actual = actual[0]

device = Elf_Handheld(actual)

print(device.get_start_marker())
print(device.get_msg_marker())