def load_data(file):
    with open(file) as f:
        inputs = f.readlines()
    inputs = [x.strip('\n') for x in inputs] 

    return inputs

def export_list(list, file):
    with open(file, 'w') as f:
        for item in list:
            f.write("%s\n" % item)