with open("prob43.txt") as infile:
    infile.readline()
    data = infile.readlines()
    ___ line in data:
        line = line.strip()
        dice = int(float(line)*6)+1
        print(dice, end=" ")
