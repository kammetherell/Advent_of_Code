def list_to_file(list, file):
    with open(file, 'w') as f:
        for item in list:
            f.write("%s\n" % item)