import math
from operator import itemgetter

def decodeboard():
    with open("/Users/benjaminbond/Desktop/AoC/day5/day5input.txt", 'r') as f:
        boardingpasses = [x.strip('\n') for x in f.readlines()]

        decodedpasses = list()
        for bpass in boardingpasses:
            upper = 127
            lower = 0
            mid = 0
            firstanswer = 0
            for letter in bpass[:7]:
                mid = (upper + lower) // 2
                if letter == 'F':
                    upper = mid
                elif letter == 'B':
                    lower =  mid + 1
                firstanswer = lower
                
            upper = 7
            lower = 0
            mid = 0
            secondanswer = 0
            for letter in bpass:
                mid = (upper + lower) // 2
                if letter == 'L':
                    upper = mid
                elif letter == 'R':
                    lower =  mid + 1
                secondanswer = lower
                
                
            decodedpasses.append([firstanswer, secondanswer])
        sortedpasses = sorted(decodedpasses, key=itemgetter(0))
        for first in range(12, 124):
            for second in range(0,8):
                if [first, second] not in sortedpasses:
                    print("{} might be your id".format(first*8 + second))
        ids = list()
        for pair in decodedpasses:
            id = pair[0]*8 + pair[1]
            ids.append(id)
        
        maxpair = max(ids)
        print(maxpair)
        for pair in decodedpasses:
            if pair[0]*8 + pair[1] == maxpair:
                print(pair)
                
        
decodeboard()
