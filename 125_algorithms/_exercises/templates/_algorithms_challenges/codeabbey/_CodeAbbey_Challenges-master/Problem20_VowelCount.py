with open("prob20.txt") as infile:
    infile.readline()
    data = infile.readlines()

    ___ line in data:
        count = 0    # resets every line
        ___ each_char in line:
            __ each_char in ["a","e","i","o","u","y"]:
                count+=1

        print(count, end=" ")
        
