infile = open("prob72.txt")
n,x = infile.readline().strip().split(" ")
data = infile.readline()
infile.close()
a = 445
c = 700001
m = 2097152
consonants = "bcdfghjklmnprstvwxz"
vowels = "aeiou"

___ length in data.strip().split(" "
    output = ""
    ___ i in range(int(length)):
        x = (int(a)*int(x)+int(c))%int(m)
        __ i%2__0: # ODDS
            output+=consonants[x%19]
        ____ # EVENS
            output+=vowels[x%5]
            
    print(output,end=" ")
    
