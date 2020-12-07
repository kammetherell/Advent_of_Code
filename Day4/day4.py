import re

with open("./inputs/day4.txt") as f:
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

def day4_1():
    passports = [x for x in split(inputs, '')]
    
    num_valid = 0
    
    for passport in passports:
        #byr (Birth Year)
        byr_bool = len([s for s in passport if 'byr' in s])>0
        #iyr (Issue Year)
        iyr_bool = len([s for s in passport if 'iyr' in s])>0
        #eyr (Expiration Year)
        eyr_bool = len([s for s in passport if 'eyr' in s])>0
        #hgt (Height)
        hgt_bool = len([s for s in passport if 'hgt' in s])>0
        #hcl (Hair Color)
        hcl_bool = len([s for s in passport if 'hcl' in s])>0
        #ecl (Eye Color)
        ecl_bool = len([s for s in passport if 'ecl' in s])>0
        #pid (Passport ID)
        pid_bool = len([s for s in passport if 'pid' in s])>0
        #cid (Country ID) - OPTIONAL
        
        valid = byr_bool * iyr_bool * eyr_bool * hgt_bool * hcl_bool * ecl_bool \
            * pid_bool
            
        #print(valid)
            
        if valid:
            num_valid +=1
    
    return num_valid
  
  
#######PART2###########

def day4_2():
    passports = [x for x in split(inputs, '')]
    
    num_valid = 0
    
    for passport in passports:
        passport = [r.split(' ') for r in passport]
        passport = [item for sublist in passport for item in sublist]
        
        byr_bool = iyr_bool = eyr_bool = hgt_bool = hcl_bool = ecl_bool = pid_bool = False
        
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        byr = [s for s in passport if 'byr' in s]
        if len(byr) > 0:
            byr = byr[0]
            if len(byr) == 8:
                if int(byr[4:])>=1920 and int(byr[4:])<=2002:
                    byr_bool = True#
            
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        iyr = [s for s in passport if 'iyr' in s]
        if len(iyr) > 0:
            iyr = iyr[0]
            if len(iyr) == 8:
                if int(iyr[4:])>=2010 and int(iyr[4:])<=2020:
                    iyr_bool = True
                    
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        eyr = [s for s in passport if 'eyr' in s]
        if len(eyr) > 0:
            eyr = eyr[0]
            if len(eyr) == 8:
                if int(eyr[4:])>=2020 and int(eyr[4:])<=2030:
                    eyr_bool = True
        
        # hgt (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
        hgt = [s for s in passport if 'hgt' in s]
        if len(hgt) > 0:
            hgt = hgt[0]
            if hgt[-2:]=='cm':
                if int(hgt[4:-2])>=150 and int(hgt[4:-2])<=193:
                    hgt_bool = True
            if hgt[-2:]=='in':
                if int(hgt[4:-2])>=59 and int(hgt[4:-2])<=76:
                    hgt_bool = True
                    
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        hcl = [s for s in passport if 'hcl' in s]
        if len(hcl) > 0:
            hcl = hcl[0]
            if len(hcl)==11:
                hcl = hcl[4:]
                if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hcl):
                    hcl_bool = True
                    
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        valid_ecl = [
            'amb',
            'blu',
            'brn',
            'gry',
            'grn',
            'hzl',
            'oth'
            ]
        ecl = [s for s in passport if 'ecl' in s]
        if len(ecl) > 0:
            ecl = ecl[0]
            ecl = ecl[4:]
            if ecl in valid_ecl:
                ecl_bool = True
                
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        pid = [s for s in passport if 'pid' in s]
        if len(pid) > 0:
            pid = pid[0]
            if len(pid) == 13:
                try:
                    int(pid[4:])
                    pid_bool = True
                except ValueError:
                    pid_bool = False
                    
        # cid (Country ID) - ignored, missing or not.
        
        valid = byr_bool * iyr_bool * eyr_bool * hgt_bool * hcl_bool * ecl_bool \
            * pid_bool

        if valid:
            num_valid +=1
    
    return num_valid

if __name__ == '__main__':
    print(day4_1())
    print(day4_2())