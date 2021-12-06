import requests
from bs4 import BeautifulSoup

def load_data(file):
    with open(file) as f:
        inputs = f.readlines()
    inputs = [x.strip('\n') for x in inputs] 

    return inputs

def export_list(list, file):
    with open(file, 'w') as f:
        for item in list:
            f.write("%s\n" % item)

def get_challenge_input(year, day, cookie):
    headers = {
        'cookie': cookie
    }

    resp= requests.get(
        f'https://adventofcode.com/{year}/day/{day}/input',
        headers=headers,
        verify=False
    )

    inputs = resp.text.split('\n')

    return inputs

def get_challenge_example(year, day, cookie):
    headers = {
        'cookie': cookie
    }

    resp= requests.get(
        f'https://adventofcode.com/{year}/day/{day}',
        headers=headers,
        verify=False
    )
    soup = BeautifulSoup(resp.text, 'html.parser')

    input = soup.pre.code.text.split('\n')

    if input[-1:][0] == '':
        input = input[:-1]

    return input