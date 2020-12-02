with open("/Users/benjaminbond/Desktop/AoC/day2/day2input.txt", 'r') as f:
    inputtext = f.readlines()

    totalcorrect = 0
    for item in inputtext:
        items = item.split()
        bounds = (items[0].split("-"))
        bounds = [int(x) for x in bounds]
        letter = items[1].strip(":")
        password = items[2]
        count = 0
        indices = list()
        for bound in bounds:
            indices.append(bound-1)
        if password[indices[0]] == letter and password[indices[1]] != letter:
            totalcorrect += 1
        elif password[indices[0]] != letter and password[indices[1]] == letter:
            totalcorrect += 1
        '''
        for current in password:
            if(current == letter):
                count += 1
        if(count >= bounds[0] and count <= bounds[1]):
            totalcorrect += 1
            print("{} has between {} and {} instances of {}".format(password, bounds[0], bounds[1], letter))
        '''
        
    print(totalcorrect)
            
        
        
