def customsdecP1():
    with open("/Users/benjaminbond/Desktop/AoC/day6/day6input.txt", 'r') as f:

        data = f.read()
        print(data)
        decl = []
        for block in data.split('\n\n'):
         ###   print(block)
            decl.append(block.strip('\n'))
            
        newdecl = list()
        for item in decl:
            newitem = item.replace('\n', '')
            newdecl.append(newitem)
            
        newnewdecl = list()
        for data in newdecl:
            newdata = ""
            for letter in data:
                if letter not in newdata:
                    newdata += letter
            newnewdecl.append(newdata)

        sum = 0
        for item in newnewdecl:
            sum += len(item)
        return sum

def customsdecP2():
    with open("/Users/benjaminbond/Desktop/AoC/day6/day6input.txt", 'r') as f:

        data = f.read()
        #print(data)
        decl = []
        for block in data.split('\n\n'):
         ###   print(block)
            decl.append(block.strip('\n'))
        splitgroups = list()
        for group in decl:
            splitgroups.append(group.split('\n'))
        #print(splitgroups)
        totallist = list()
        
        for item in splitgroups:
            totalsum = 0
            first = item[0]
            for letter in first:
                present = True
                for other in item[1:]:
                    if letter not in other:
                        present = False
                if present == True:
                    totalsum += 1
            totallist.append(totalsum)
        print(sum(totallist))
                        
            
                
customsdecP2()
