infile = open("prob8.txt")
infile.readline()
data = infile.readlines()
___ line __ data:
    line = line.strip()
    a,b,n = line.split(" ")
    total = 0
    ___ i __ range(int(n)):
        total += int(a)+i*int(b)
    print(total,end=" ")
   


infile.close()
