infile = open("prob44.txt")
infile.readline()
data = infile.readlines()

___ line in data:
    line = line.strip().split(" ")
    summ = 0
    ___ random in line:
        summ += (int(random)%6)+1
    print(summ,end=" ")

infile.close()
