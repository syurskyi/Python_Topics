______ ma__
infile = open("prob128.txt")
infile.readline()
data =infile.readlines()
infile.close()

___ line in data:
    N,K = line.strip().split(" ")
    numerator = ma__.factorial(int(N))
    denominator = (ma__.factorial(int(K))*ma__.factorial(int(N)-int(K)))
    total = numerator/denominator
    print(int(total),end = " ")
    
