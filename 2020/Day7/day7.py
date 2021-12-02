with open("./Day7/input.txt") as f:
    inputs = f.readlines()
inputs = [x.strip('\n') for x in inputs] 
inputs = [rule.split(' bags contain ')for rule in inputs]

def get_parent_bags(bag_name):
    parents = []
    
    for rule in inputs:
        if bag_name in rule[1]:
            parents.append(rule[0])
            
    return parents
    
def construct_unique_list(lst, items_to_add):
    for item in items_to_add:
        if item not in lst:
            lst.append(item)
            
    return lst
    
def find_valid_combos(bag_name):
    combos = []
    
    opts = get_parent_bags(bag_name)
    
    combos = construct_unique_list(combos, opts)
    
    while len(opts) > 0:
        temp_opts = []
        for opt in opts:
            temp_opts = construct_unique_list(temp_opts, get_parent_bags(opt))
        
        combos = construct_unique_list(combos, temp_opts)
        
        opts = temp_opts
    
    return combos

print('===PART 1===')
print(len(find_valid_combos('shiny gold')))


print('===PART 2===')

def find_children(bag_name, num_bags):
    children = []
    
    for rule in inputs:
        if bag_name in rule[0]:
            children.append(rule[1])
            
    children = [r.split(', ') for r in children]
    children = [item for sublist in children for item in sublist]
    children = [r.split(' ',1) for r in children]
    
    for idx, child in enumerate(children):
        try:
            children[idx][0] = str(int(children[idx][0])*num_bags)
        except Exception:
            continue
        
        
    return children
    
def find_all_children(bag_name):
    bag_count = 0
    
    opts = find_children(bag_name, 1)
    
    
    while len(opts) > 0:
        temp_opts = []
        for opt in opts:
            if opt[0].find('no')!=0:
                bag_count = bag_count + int(opt[0])
                opt_name = opt[1].rsplit(' ',1)[0]
                temp_opts.append(find_children(opt_name, int(opt[0])))
            
        opts = temp_opts
        opts = [item for sublist in opts for item in sublist]

    return bag_count
    
# print(find_children('shiny gold'))
print(find_all_children('shiny gold'))