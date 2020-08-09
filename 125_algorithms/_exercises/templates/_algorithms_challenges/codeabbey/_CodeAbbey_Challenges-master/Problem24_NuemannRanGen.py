infile = open("prob24.txt")
infile.readline()
data = infile.read().strip().split(" ")

___ start_val in data:
    seq = [start_val] # Initialise sequence LIST

    new_val = str(int(start_val)**2).rjust(8,"0") # Padding

    new_val = new_val[2:6]      #truncate first two and last two
    w___ new_val not in seq:   # check for looping pattern
        seq.append(new_val)
        new_val = str(int(new_val)**2).rjust(8,"0")
        new_val = new_val[2:6]


    print(le.(seq),end=" ")



infile.close()
