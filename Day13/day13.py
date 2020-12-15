import math

with open("./Day13/input.txt") as f:
    inputs = f.readlines()
inputs = [x.strip('\n') for x in inputs]

earliest_departure = int(inputs[0])    
buses = inputs[1].split(',')
buses_pure = [int(x) for x in buses if not x == 'x']

def day13_1():
    bus_id = 0
    wait_time = earliest_departure

    for bus in buses_pure:
        wait = bus - (earliest_departure % bus)
        if wait < wait_time:
            bus_id = bus
            wait_time = wait
    
    return bus_id, wait_time

bus_id, wait_time = day13_1()

print(bus_id * wait_time)

def find_u(n_div, n):
    u = 0
    found = False

    while not found:
        if (n_div * u) % n ==1:
            found = True
        else:
            u += 1
    
    return u

def day13_2():
    buses_offset = list(enumerate(buses))
    buses_offset = [
        (x[0], int(x[1])) for x in buses_offset if not x[1] == 'x'
        ]

    print(buses_offset)

    equations = []
    
    for bus in buses_offset:
        equations.append(
            {
                'n': bus[1],
                'a': -1 * bus[0]
            }
        )

    N = math.prod([x['n'] for x in equations])

    for bus in equations:
        bus['n_div'] = int(N/bus['n'])
        bus['u'] = find_u(bus['n_div'], bus['n'])

        bus['x'] = bus['a'] * bus['n_div'] * bus['u']

    X = sum([bus['x'] for bus in equations]) % N

    return X

print(day13_2())