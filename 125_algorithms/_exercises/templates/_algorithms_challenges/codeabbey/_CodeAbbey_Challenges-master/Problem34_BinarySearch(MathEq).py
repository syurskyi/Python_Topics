______ ma__
infile = open("prob34.txt")
infile.readline()
data = infile.readlines()
infile.close()


___ func(x
    global A,B,C,D
    eq = (A*x) + (B*ma__.sqrt(x**3)) - (C*ma__.exp(-x/50)) - D
    r_ eq

for line in data:
    A,B,C,D = list(map(float,line.strip().split(" ")))
    top = 100
    bot = 0
    eq = -1
    w___ ma__.isclose(eq , 0 ,abs_tol = 1e-7) __ False:
        mid = (top+bot)/2
        eq = func(mid)
        __ eq > 0:
            top = mid-1
        ____ eq < 0:
            bot = mid+1
    print(mid,end=" ")
    
    
    
    
