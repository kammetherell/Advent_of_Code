import aocd
import datetime
import dotenv
dotenv.load_dotenv()

today = datetime.datetime.now()

def export_list(list, file):
    with open(file, 'w') as f:
        for item in list:
            f.write("%s\n" % item)

def get_inputs(year, day, splitLines):
    actual = aocd.get_data(day=day, year=year)

    if splitLines:
        actual = actual.split('\n')

    return actual

def submit(ans, year = today.year, day = today.day, part = 'a'):
    aocd.submit(ans, part=part, year=year, day=day)