


infile = open("prob75.txt","r")
infile.readline()
data = infile.readlines()
infile.close()
___ line in data:
    line = line.strip().split()
    counter = [0 ___ i in range(7)]# ignore index 0
    ___ digit in line:
        counter[int(digit)] +=1
    __ counter.count(5) __ 1:
        print("yacht",end=" ")
    ____ counter.count(4) != 0:
        print("four",end=" ")
    ____ counter.count(3) __ 1 and counter.count(2) __1:
        print("full-house",end=" ")
    ____ counter.count(3) __ 1:
        print("three",end=" ")
    ____ counter.count(2) __ 1:
        print("pair",end=" ")
    ____ counter.count(2) __ 2:
        print("two-pairs",end=" ")
    ____ counter.count(1) __ 5:
        __ counter[1] __ 0:
            print("big-straight",end=" ")
        ____
            print("small-straight",end=" ")

