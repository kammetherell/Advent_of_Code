with open("./Day16/input.txt") as f:
    inputs = f.readlines()
inputs = [x.strip('\n') for x in inputs] 

def split(sequence, sep):
    chunk = []
    for val in sequence:
        if val == sep:
            yield chunk
            chunk = []
        else:
            chunk.append(val)
    yield chunk

inputs = [x for x in split(inputs, '')]
ticket_rules = inputs[0]
my_ticket = inputs[1][1].split(',')
other_tickets = inputs[2][1:]

def define_rules(rule_list):
    rule_dict = {}
    for rule in rule_list:
        field = rule.split(': ')[0]

        rule_dict[field] = rule.split(': ')[1].split(' or ')
    
    return rule_dict

def check_valid(ticket, rules):
    valid = True
    invalid_sum = 0

    ticket_fields = ticket.split(',')

    for field in ticket_fields:
        valid_list = []
        field = int(field)
        for key, value in rules.items():
            range1 = value[0].split('-')
            range2 = value[1].split('-')

            in_range1 = field>=int(range1[0]) and field <= int(range1[1])
            in_range2 = field>=int(range2[0]) and field <= int(range2[1])

            if in_range1 or in_range2:
                valid_list.append(key)

        if len(valid_list) == 0:
            valid = False
            invalid_sum += field

    return valid, invalid_sum

rule_dict = define_rules(ticket_rules)
# print('===RULES===')
# print(rule_dict)

print('===PART 1===')
error_rate = 0
invalid_tickets = []
for idx, ticket in enumerate(other_tickets):
    valid, e_rate = check_valid(ticket, rule_dict)
    error_rate+= e_rate
    if not valid:
        invalid_tickets.append(idx)
print(error_rate)

print('===PART 2===')
field_opts = {}
#Create dictionary of field index and all possible options
for i in range(len(rule_dict)):
    field_opts[i] = list(rule_dict.keys())

#Loop over all valid tickets
for idx, ticket in enumerate(other_tickets):
    if idx not in invalid_tickets:
        ticket_fields = ticket.split(',')
        for field_idx, field in enumerate(ticket_fields):
            field = int(field)
            #Test value against all field rules
            for key, value in rule_dict.items():
                range1 = value[0].split('-')
                range2 = value[1].split('-')

                in_range1 = field>=int(range1[0]) and field <= int(range1[1])
                in_range2 = field>=int(range2[0]) and field <= int(range2[1])

                #if value cannot be a field, remove it from our field_ops dictionary
                if not in_range1 and not in_range2:
                    field_opts[field_idx].remove(key)

assigned = []
# Loop over all field_opts until all fields are assinged
while len(assigned) != len(field_opts):
    # Check if we've already assigned an index to this field
    for idx, opts in field_opts.items():
        if opts not in assigned:
            # If only one field option, assign this index to that fiels
            if len(opts) == 1:
                field_opts[idx] = opts[0]
                assigned.append(opts[0])
            # Else, remove any already assigned to an index
            else:
                field_opts[idx] = [x for x in field_opts[idx] if x not in assigned]

print(field_opts)

# Run against my ticket
output = 1
for idx, field_name in field_opts.items():
    if field_name[:9]=='departure':
        output = output * int(my_ticket[idx])

print(output)