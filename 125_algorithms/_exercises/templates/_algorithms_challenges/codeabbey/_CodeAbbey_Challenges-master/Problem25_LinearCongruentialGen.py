infile = open("prob25.txt")
infile.readline()
data = infile.readlines()
infile.close()

___ line __ data:
    a,c,m,x,n = line.strip().split(" ")
    random =   # list
    ___ i __ range(int(n)):
        x = (int(a)*int(x)+int(c))%int(m)
        random.append(x)
    print(random[-1],end=" ")
