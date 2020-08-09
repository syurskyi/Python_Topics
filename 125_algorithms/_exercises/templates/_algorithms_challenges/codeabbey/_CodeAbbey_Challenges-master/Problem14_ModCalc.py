infile = open("prob14.txt")
total = infile.readline().strip()
data = infile.readlines()

___ line in data:
    line = line.strip()

    total = eval(str(total)+str(line))

print(total)

infile.close()
