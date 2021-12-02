    
with open("./Day6/input.txt") as f:
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

groups =  [x for x in split(inputs, '')]

def alphabet_generator():
    letters = []

    for i in range(0,26):
        letter = chr(i+97)
        letters.append(letter)
    
    return letters

def day6_1():
    sum_questions = 0
    alphabet = alphabet_generator()
    
    for group in groups:
        yes_answers = 0
        
        for letter in alphabet:
            if len([ans for ans in group if letter in ans])>0:
                yes_answers +=1
        
        sum_questions +=yes_answers
        
    return sum_questions
    
print(day6_1())

def day6_2():
    sum_questions = 0
    alphabet = alphabet_generator()
    
    for group in groups:
        yes_answers = 0
        
        for letter in alphabet:
            present = True
            
            for person in group:
                pers_yes = person.find(letter)
                
                if pers_yes is -1:
                    present = False
                    
                continue
            
            if present:
                yes_answers +=1
            
            continue
        
        sum_questions += yes_answers
        
    return sum_questions
    
print(day6_2())