import aocd
import datetime
import dotenv
from . import helper
from . import error_checking
dotenv.load_dotenv()

today = datetime.datetime.now()

class AOC:
    def __init__(self, year, day) -> None:
        self.year = year
        self.day = day

    def get_inputs(self):
        actual = aocd.get_data(day=self.day, year=self.year)
        return actual

    def submit_a(self, ans):
        aocd.submit(ans, part='a', year=self.year, day=self.day)
    def submit_b(self, ans):
        aocd.submit(ans, part='b', year=self.year, day=self.day)