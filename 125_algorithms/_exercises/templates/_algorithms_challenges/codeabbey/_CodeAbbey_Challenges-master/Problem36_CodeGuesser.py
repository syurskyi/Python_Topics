
infile = open("prob36.txt")
infile.readline()
data = infile.readlines()

poss = [[ 0 ___ i __ range(10)] ___ i __ range((le.(data[0])-3))]

___ line __ data:
    guess,reply = line.strip().split()
    __ reply __ "0":
        ___ i __ range(le.(guess)):
            poss[i][int(guess[i])] = None
    ____ reply __ "1" or reply __ "2":
        try:
            ___ j __ range(le.(guess)):
                poss[j][int(guess[j])] += 1
        except TypeError:
            continue

            
