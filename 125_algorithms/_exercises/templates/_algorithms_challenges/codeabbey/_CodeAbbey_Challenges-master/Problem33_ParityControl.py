infile = open("prob33.txt")
data = infile.read()
infile.close()

data = data.split(" ")
output = ""
___ symbol in data:
    binary = list(bin(int(symbol))[2:].rjust(8,"0"))
##    total = sum([int(i) for i in binary])
    total = binary.count("1")
    print(total)
    __ total%2 __ 0:
        binary[0] = 0 
        char = chr(int("".join(str(i)___ i in binary),base=2))
        output+= char
    
print(output)
