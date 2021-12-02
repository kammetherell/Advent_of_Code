from datetime import datetime
inputs = [9,6,0,10,18,2,1]

tests = {
    '1': {
        'vals': [0,3,6],
        'ans': 436
    },
    '2': {
        'vals': [1,3,2],
        'ans': 1
    },
    '3': {
        'vals': [2,1,3],
        'ans': 10
    },
    '4': {
        'vals': [1,2,3],
        'ans': 27
    }
}

def estimate_time_remaining(start, num_iters, curr_iter):
    now = datetime.now()
    time_elapsed = now - start

    time_per_iter = time_elapsed / curr_iter
    total_time = time_per_iter * num_iters
    time_remaining = total_time - time_elapsed

    print(f'\rEstimated Time Remaining: {time_remaining}\r', end='', flush=True)

def play_game(start_list, number):
    spoken = []
    start = datetime.now()

    #Create Dictionary to write previous two ocurences to of a number
    last_spoken = {}

    for i in range(number):
        if i % 1000==0:
            estimate_time_remaining(start, number, i+1)
        if i < len(start_list):
            spoken.append(start_list[i])
            last_spoken[start_list[i]] = [None,i + 1]
        else:
            last_num_spoken = spoken[i-1]
            diff = 0
            last_occur = last_spoken[last_num_spoken]
            #Check if this occurence is not only occurence
            if last_occur[0] is not None:
                diff = i - last_occur[0]

            spoken.append(diff)
            if diff in last_spoken.keys():
                last_spoken[diff] = [last_spoken[diff][1], i+1] 
            else:
                last_spoken[diff] = [None, i+1] 

    print('\r')
    return spoken[-1]

# print(play_game(tests['1']['vals'], 10))
print(f'\r{play_game(inputs, 2020)}')
print(f'\r{play_game(inputs, 30000000)}')