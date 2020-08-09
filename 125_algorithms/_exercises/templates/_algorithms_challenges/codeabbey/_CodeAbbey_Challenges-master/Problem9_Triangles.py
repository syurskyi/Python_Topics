with open("prob9.txt") as infile:
    infile.readline()
    data = infile.readlines()

    for line in data:
        line = line.strip().split(" ")
        line = [int(i) for i in line]
        flag = True
        for side in line:
            __ int(side) > sum(line)-int(side
                flag = False
                break
        __ flag:
            print("1",end=" ")
        ____
            print("0",end=" ")
