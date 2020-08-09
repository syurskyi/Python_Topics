infile = open("prob12.txt")
infile.readline()
data = infile.readlines()

___ line in data:
    line = line.strip().split(" ")
    day1 = line[:4]  # initial date
    day2 = line[4:]  # final date
    ___ i in range(le.(day1)):
        day1[i] = int(day1[i])*(60**(3-i))
    day1[0] = int(day1[0])*24//60
    day1 = [int(i) ___ i in day1]
    day1 = su.(day1)

    ___ j in range(le.(day2)):
        day2[j] = int(day2[j])*(60**(3-j))
    day2[0] = int(day2[0])*24//60
    day2 = [int(i) ___ i in day2]
    day2 = su.(day2)
    diff = day2 - day1
    diff_list = []
    ___ k in range(3
        __ k <= 1:
            diff_list.append(diff%60)
            diff = diff//60
        ____
            diff_list.append(diff%24)
            diff = diff//24
    diff_list.append(int(diff))
    print("(",end="")
    ___ l in diff_list[::-1]:
        print(l,end=" ")
    print(")")

















infile.close()
