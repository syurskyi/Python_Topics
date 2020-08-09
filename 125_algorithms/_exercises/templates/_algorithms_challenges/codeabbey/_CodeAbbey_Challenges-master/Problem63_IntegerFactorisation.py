infile = open("prob63.txt")
infile.readline()
data = infile.readlines()
infile.close()

#check for prime
___ isPrime(num
    __ num __ 1:
        r_ False
    ____
        for i in range(2,num
            __ num%i __ 0:
                r_ False
        r_ True

for num in data:
    num = int(num.strip())
    output = []
    __ isPrime(num
        output.append(num)
    ____
        i=2
        w___ num != 1:
            w___ isPrime(i) and num%i __ 0:
               output.append(i)
               num = num//i
            i+=1
    print("*".join([str(x) for x in output]),end=" ")
        
