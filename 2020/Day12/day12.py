import math

with open("./Day12/input.txt") as f:
    inputs = f.readlines()
inputs = [x.strip('\n') for x in inputs]

def move(ew, ns, bearing, instruction):
    ins_type = instruction[0]
    ins_quant = int(instruction[1:])

    if ins_type == 'N':
        ns += ins_quant
    elif ins_type == 'S':
        ns = ns - ins_quant
    elif ins_type == 'E':
        ew += ins_quant
    elif ins_type == 'W':
        ew = ew - ins_quant
    elif ins_type == 'L':
        bearing = bearing - ins_quant
        if bearing >= 360:
            bearing = bearing - 360
        elif bearing < 0:
            bearing = bearing + 360
    elif ins_type == 'R':
        bearing = bearing + ins_quant
        # while bearing < 0 or bearing>=360:
        if bearing >= 360:
            bearing = bearing - 360
        elif bearing < 0:
            bearing = bearing + 360
    elif ins_type == 'F':
        delta_ns = 0
        delta_ew = 0
        if bearing >= 0 and bearing <90:
            # Increase in ns and ew
            angle = math.radians(90 - bearing)
            delta_ns = ins_quant * math.sin(angle)
            delta_ew = ins_quant * math.cos(angle)
        elif bearing >= 90 and bearing <180:
            # Decrease in ns and increase ew
            angle = math.radians(bearing - 90)
            delta_ns = -1 * ins_quant * math.sin(angle)
            delta_ew = ins_quant * math.cos(angle)
        elif bearing >= 180 and bearing <270:
            # Decrease in both
            angle = math.radians(270 - bearing)
            delta_ns = -1 * ins_quant * math.sin(angle)
            delta_ew = -1 * ins_quant * math.cos(angle)
        elif bearing >= 270 and bearing <360:
            # Increase ns; decrease ew
            angle = math.radians(bearing - 270)
            delta_ns = ins_quant * math.sin(angle)
            delta_ew = -1 * ins_quant * math.cos(angle)

        ns = ns + delta_ns
        ew = ew + delta_ew

        ns = round(ns)
        ew = round(ew)
        bearing = round(bearing)
    return ew, ns, bearing

def day12_1():
    ns = 0
    ew = 0
    bearing = 90

    for input in inputs:
        # print(input)
        ew, ns, bearing = move(ew, ns, bearing, input)
        # print (ns, ew, bearing)
    
    print (ns, ew)
    manhat_dist = abs(ns) + abs(ew)

    return manhat_dist

print(day12_1())

def wpt_move(wpt_ns, wpt_ew, instruction):
    ins_type = instruction[0]
    ins_quant = int(instruction[1:])

    if ins_type == 'N':
        wpt_ns += ins_quant
    elif ins_type == 'S':
        wpt_ns = wpt_ns - ins_quant
    elif ins_type == 'E':
        wpt_ew += ins_quant
    elif ins_type == 'W':
        wpt_ew = wpt_ew - ins_quant
    elif ins_type == 'L' or ins_type == 'R':
        wpt_dist = math.sqrt(wpt_ns**2 + wpt_ew**2)
        wpt_rad = math.atan(abs(wpt_ns)/abs(wpt_ew))
        wpt_deg = math.degrees(wpt_rad)
        wpt_bear = 0

        if wpt_ew >=0:
            if wpt_ns >= 0:
                wpt_bear = 90 - wpt_deg
            else:
                wpt_bear = 90 + wpt_deg
        else:
            if wpt_ns >= 0:
                wpt_bear = 270 + wpt_deg
            else: 
                wpt_bear = 270 - wpt_deg

        if ins_type == 'L':
            wpt_bear = wpt_bear - ins_quant
        else:
            wpt_bear = wpt_bear + ins_quant

        if wpt_bear >= 360:
            wpt_bear = wpt_bear - 360
        elif wpt_bear < 0:
            wpt_bear = wpt_bear + 360

        wpt_ns = wpt_dist * math.cos(math.radians(wpt_bear))
        wpt_ew = wpt_dist * math.sin(math.radians(wpt_bear))

    return wpt_ns, wpt_ew

def day12_2():
    curr_ns = 0
    curr_ew = 0
    curr_bearing = 0

    wpt_ns = 1
    wpt_ew = 10

    for input in inputs:
        # print(input)
        if input[0]=='F':
            steps = int(input[1:])
            curr_ns = curr_ns + steps * wpt_ns
            curr_ew = curr_ew + steps * wpt_ew
        else:
            wpt_ns, wpt_ew = wpt_move(wpt_ns, wpt_ew, input)
        # print('Current location')
        # print(curr_ns, curr_ew)
        # print('Waypoint Location')
        # print(wpt_ns, wpt_ew)
    manhat_dist = abs(curr_ns) + abs(curr_ew)

    return manhat_dist

print(day12_2())