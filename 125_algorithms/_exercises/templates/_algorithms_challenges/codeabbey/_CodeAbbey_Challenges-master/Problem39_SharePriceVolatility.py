infile = open("prob39.txt")
infile.readline()
data = infile.readlines()
infile.close()


___ line __ data:
    line = line.strip().split(" ")
    name = line[0]
    share_p = [int(i) ___ i __ line[1:]]
    mean = su.(share_p)/le.(share_p)
    var = [(price-mean)**2 ___ price __ share_p]
    dev = (su.(var)/le.(var))**0.5
    __ dev >= 4*0.01*mean:
        print(name,end=" ")
        
    
