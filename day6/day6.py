def customsdec():
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
        print(sum)


customsdec()
