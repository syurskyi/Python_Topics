infile = open("prob49.txt")
infile.readline()
data = infile.readlines()
infile.close()

# S>P
# P>R
# R>S


___ line in data:
    p1 = 0
    p2 = 0
    match = line.strip().split(" ")
    ___ game in match:
        c1 = game[0] # p1 choice
        c2 = game[1]
        __ c1 __ "S":
            __ c2 __ "P":
                p1+=1
            ____ c2 __ "R":
                p2+=1
                
        ____ c1 __ "R":
            __ c2 __ "S":
                p1+=1
            ____ c2 __ "P":
                p2+=1
                
        ____ c1 __ "P":
            __ c2 __ "R":
                p1+=1
            ____ c2 __ "S":
                p2+=1

    __ p1>p2:
        print("1",end=" ")
    ____
        print("2",end=" ")

















        
