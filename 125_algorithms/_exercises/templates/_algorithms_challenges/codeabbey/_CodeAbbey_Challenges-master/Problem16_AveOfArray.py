
infile = open("prob16.txt")
infile.readline()
data = infile.readlines()


___ avg(num
    total = su.(num)
    ave = total/le.(num)
    print(round(ave),end=" ")
    


___ line in data:
    line = line.strip().split(" ")
    line = line[:-1]
    line = [int(i) ___ i in line]
    avg(line)
infile.close()
