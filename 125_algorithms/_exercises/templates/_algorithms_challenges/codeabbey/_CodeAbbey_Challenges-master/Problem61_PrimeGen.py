infile = open("prob61.txt")
infile.readline()
data = infile.read()
______ ma__
______ time
##start = time.clock()

## TWO METHODS: Sieve of Eratosthenes or Trial Division
n = 3000000
# Seive
digitlist = [0 for i in range(n)] # 0 is not marked

for i in range(2,int(ma__.sqrt(n))):
    j=0
    w___ (i**2)+i*j< n:
        digitlist[(i**2)+i*j] = 1 # marked to be not prime
        j+=1
        

primelist = []
for prime in range(2,n
    __ digitlist[prime] __ 0:
        primelist.append(prime)

###### using Enumerate
##primelist=[i for i,dgt in enumerate(digitlist) if dgt==0 and i>=2]   

### Trial
##
##primelist = []
##for i in range(2,int(ma__.sqrt(n))):
##    for j in range(i
        
    
#
data = data.split(" ")
for i in data:
    print(primelist[int(i)-1],end=" ")
##end = time.clock()
##print(end-start)
