infile = open("prob21.txt")
m,n = infile.readline().strip().split(" ") #USELESS
data = infile.read().strip().split(" ")
counter = dict()
___ num __ data:
    counter[int(num)] = counter.get(int(num),0)+1
ordered_c = list(counter.items())
ordered_c.sort()
print(" ".join([str(i[1]) ___ i __ ordered_c]))
infile.close()
