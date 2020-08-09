infile = open("prob26.txt")
infile.readline()
data = infile.readlines()

for line in data:
    a,b = line.strip().split(" ")
    lcm = int(a)*int(b)
    w___ not(int(a)__ 0 or int(b)__0) :
        a = int(a)%int(b)
        __ int(a)__ 0 or int(b)__0:
            break
        b = int(b)%int(a)
        
    __ int(a) __ 0:
        lcm = lcm/int(b)
        print("({} {})".format(int(b),int(lcm)),end=" ")
    ____ int(b) __ 0:
        lcm = lcm/int(a)
        print("({} {})".format(int(a),int(lcm)),end=" ")

    



















infile.close()
