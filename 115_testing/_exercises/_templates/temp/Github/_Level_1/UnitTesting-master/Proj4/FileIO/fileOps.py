infile _ "inputfile.txt"
outfile _ "outputfile.txt"

# print each line, as read in
w__ o..(infile) __ f1:
    ___ line __ f1:
        print(line)

print("\n**********************")

# print each line, stripping last newline character
w__ o..(infile) __ f1:
    ___ line __ f1:
        print(line[:-1])

print("\n**********************")

# print first word (make) of each car
w__ o..(infile) __ f1:
    ___ line __ f1:
        row _ line.split(",")
        print(row[0])

print("\n**********************")

# print each line as a formatted list
w__ o..(infile) __ f1:
    ___ line __ f1:
        row _ line.split(",")
        print(row[0] + "\n------------")
        ___ i __ ra..(1, le.(row)):
            print(row[i])

print("\n**********************")

# add each line to a list
cars _ li..()
w__ o..(infile) __ f1:
    ___ line __ f1:
        row _ line.split(",")
        cars.a..(row)
    print(cars[0][0])

print("\n**********************")

# write makes only to outputfile
w__ o..(outfile, 'a') __ f2:
    ___ car __ cars:
        f2.write(car[0] + "\n")

# print out whole line to file
w__ o..(outfile, 'a') __ f2:
    ___ car __ cars:
        f2.write(st.(car) + "\n")
