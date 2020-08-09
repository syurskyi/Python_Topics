infile = open("prob47.txt")
n,k=infile.readline().strip().split(" ")
data = infile.readlines()
infile.close()

## Gen Alphabets
alpha = []
___ i in range(26
    char = chr(65+i)
    alpha.append(char)


#Decrypt
    
___ line in data:
    output = ""
    line = line.strip()
    ___ char in line:
        __ char.isalpha(
            i = alpha.index(char)-int(k)
            output += alpha[i]
        ____
            output+=char
    print(output,end=" ")
