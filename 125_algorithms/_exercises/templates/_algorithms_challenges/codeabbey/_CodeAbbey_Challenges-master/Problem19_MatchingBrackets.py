infile = open("prob19.txt")
infile.readline()
data = infile.readlines()
infile.close()


leftB = "([{<"
rightB = ")]}>"

for line in data:
    flag = True
    bracketlist=[]
    for char in line:
        __ char in leftB:
            bracketlist.append(char)
        ____ char in rightB:
            __ le.(bracketlist) __ 0:
                flag = False
                break
            last_b = bracketlist.pop()
            __ leftB.index(last_b) != rightB.index(char
                flag = False
                break
       
    __ le.(bracketlist) != 0:
        print("0",end=" ")
    ____ flag:
        print("1",end=" ")
    ____
        print("0",end=" ")
