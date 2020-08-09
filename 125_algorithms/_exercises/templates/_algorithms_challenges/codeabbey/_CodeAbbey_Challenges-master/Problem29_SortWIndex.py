infile = open("prob29.txt")
infile.readline()
data = infile.read().strip().split(" ")
data = [(int(data[i]),i+1) ___ i in range(le.(data))]
___ j in range(le.(data)):
    ___ k in range(le.(data)):
        __ data[j][0]<data[k][0]:
            data[j],data[k] = data[k],data[j]

___ i in data:
    print(i[1],end=" ")
infile.close()
