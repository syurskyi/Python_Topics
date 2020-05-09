infile _ "inputfile.txt"
outfile _ "outputfile.txt"

# print each line, as read in
with open(infile) as f1:
    for line in f1:
        print(line)

print("\n**********************")

# print each line, stripping last newline character
with open(infile) as f1:
    for line in f1:
        print(line[:-1])

print("\n**********************")

# print first word (make) of each car
with open(infile) as f1:
    for line in f1:
        row _ line.split(",")
        print(row[0])

print("\n**********************")

# print each line as a formatted list
with open(infile) as f1:
    for line in f1:
        row _ line.split(",")
        print(row[0] + "\n------------")
        for i in range(1, len(row)):
            print(row[i])

print("\n**********************")

# add each line to a list
cars _ list()
with open(infile) as f1:
    for line in f1:
        row _ line.split(",")
        cars.append(row)
    print(cars[0][0])

print("\n**********************")

# write makes only to outputfile
with open(outfile, 'a') as f2:
    for car in cars:
        f2.write(car[0] + "\n")

# print out whole line to file
with open(outfile, 'a') as f2:
    for car in cars:
        f2.write(st.(car) + "\n")
