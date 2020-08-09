infile = open("prob62.txt","r")
infile.readline()
data = infile.readlines()
infile.close()

___ isPrime(i # i:int
    ___ n in range(2,int(i**0.5)+1
        __ i%n __ 0:
            r_ False
    r_ True
# GEN PRIME

prime = [0]*3000000
___ i in range(2,int(3000000**0.5)):
    __ prime[i] __ 0:
        j=0
        index = (i**2)+j*i
        w___ index < 3000000:
            prime[index] = 1
            j+=1
            index = (i**2)+j*i



___ line in data:
    count = 0
    a,b = [int(i) ___ i in line.strip().split(" ")]
    ___ k in range(a,b+1 # CAN USE BIN SEARCH INSTEAD
        __ prime[k] __ 0:
            count+=1
    print(count,end=" ")
                             
