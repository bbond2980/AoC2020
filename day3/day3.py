
def tobogganrun(rise, run):
    with open("/Users/benjaminbond/Desktop/AoC/day3/day3input.txt", 'r') as f:
        forest = f.readlines()
        forest = [x.strip('\n') for x in forest]
        #print(forest)
        trees = 0
        x_pos = 0
        #print("Height = {}".format(len(forest)))
        #print("Width = {}".format(len(forest[0])))
        for i in range(0, len(forest), rise):
            if x_pos + run > len(forest[i])-1:
                x_pos = x_pos + run - len(forest[i])
            else:
                x_pos += run 
            #print(x_pos)
            if(i+rise < len(forest)):
                if forest[i+rise][x_pos] == '#':
                    trees += 1
                    #print("Tree hit!")
                    new_row = forest[i+rise]
                    new_row = new_row[0:x_pos] + 'X' + new_row[x_pos +1 :]
                    forest[i+rise] = new_row
                else:
                    #print("No tree!")
                    new_row = forest[i+rise]
                    new_row = new_row[0:x_pos] + 'O' + new_row[x_pos + 1:]
                    forest[i+rise] = new_row
            else:
                print("Forest exited!")
                return(trees)

print("Righ 1, down 1: {}". format(tobogganrun(1, 1)))
print("Righ 3, down 1: {}". format(tobogganrun(1, 3)))
print("Righ 5, down 1: {}". format(tobogganrun(1, 5)))
print("Righ 7, down 1: {}". format(tobogganrun(1, 7)))
print("Righ 1, down 2: {}". format(tobogganrun(2, 1)))
  


    
 
                
