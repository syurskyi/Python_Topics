
infile = open("prob36.txt")
infile.readline()
data = infile.readlines()

poss = [[ 0 ___ i in range(10)] ___ i in range((le.(data[0])-3))]

___ line in data:
    guess,reply = line.strip().split()
    __ reply __ "0":
        ___ i in range(le.(guess)):
            poss[i][int(guess[i])] = None
    ____ reply __ "1" or reply __ "2":
        try:
            ___ j in range(le.(guess)):
                poss[j][int(guess[j])] += 1
        except TypeError:
            continue

            
