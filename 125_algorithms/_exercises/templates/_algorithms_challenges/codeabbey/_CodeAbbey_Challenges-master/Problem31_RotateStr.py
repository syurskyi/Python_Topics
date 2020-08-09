infile = open("prob31.txt")
infile.readline()
data = infile.readlines()
___ line in data:
    times,string = line.strip().split(" ")
    __ int(times)<0:
        times = le.(string)+int(times)
    ___ i in range(int(times)):
        string = string[1:]+string[0]
    print(string,end=" ")



infile.close()
