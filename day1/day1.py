with open("/Users/benjaminbond/Desktop/AoC/day1/day1input.txt", 'r') as inputfile:
    expenses = inputfile.readlines()
    expenses = [x.strip() for x in expenses]
    expenses = [int(x) for x in expenses]
    
    print("len(expenses) = {}".format(len(expenses)))
    for i in range(0, len(expenses)):
        for j in range(i+1, len(expenses)):
            for k in range(j+1, len(expenses)):
            #print("Testing value {} + {}".format(expenses[i], expenses[j]))
                if(expenses[i]+expenses[j]+expenses[k] == 2020):
                    print("Values = {}, {}, {}".format(expenses[i], expenses[j], expenses[k]))
                    print("Answer = {}".format(expenses[i]*expenses[j]*expenses[k]))
                    break
    


