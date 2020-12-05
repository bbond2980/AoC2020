import re

def producePassports():
    with open("/Users/benjaminbond/Desktop/AoC/day4/day4input.txt", 'r') as f:

        data = f.read()
        passports = []
        for block in data.split('\n\n'):
         ###   print(block)
            parsed = re.findall(r'(\w+):(\S+)', block)
            passports.append({m[0]: m[1] for m in parsed})
        return(passports)

    
passlist = producePassports()

def validatepassports(passlist):

    valid = 0
    for passport in passlist:
        
        try:
            byr = int(passport['byr'])
            if not (1920 <= byr <= 2002 or len(byr) == 4):
                continue
            
            iyr = int(passport['iyr'])
            if not (2010 <= iyr <= 2020 or len(iyr) == 4):
                continue
            eyr = int(passport['eyr'])
            if not (2020 <= eyr <= 2030 or len(eyr) == 4):
                continue
            hgt = passport['hgt']
            if not ( hgt[-2:] == 'cm' or hgt[-2:] == 'in'):
                continue
            if hgt[-2:] == 'cm':
                if int(passport['hgt'][0:-2]) > 193 or int(passport['hgt'][0:-2]) < 150:
                    continue                  
            else:
                if int(passport['hgt'][0:-2]) > 76 or int(passport['hgt'][0:-2]) < 59:
                    continue

            hcl = passport['hcl']
            if hcl[0] == '#':
                for i in passport['hcl'][1:]:
                    if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                        continue
            else:
                continue
            
            ecl = passport['ecl']
            if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                continue

            pid = passport['pid']
            if len(passport['pid']) != 9:
                continue
            valid += 1
            print("Valid!")
        except:
            print("Invalid!")
            continue
    return valid

print(validatepassports(passlist))

'''
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country 
'''
