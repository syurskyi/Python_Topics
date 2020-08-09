infile = open("prob11.txt")
infile.readline()
data = infile.readlines()
___ line in data:
    first,second,third = line.strip().split(" ")
    digits = (int(first)*int(second))+int(third)
    total = 0
    temp = digits
    ___ i in range(le.(str(digits))):
        total += temp%10
        temp = temp//10 
    print(total,end=" ")









infile.close()
