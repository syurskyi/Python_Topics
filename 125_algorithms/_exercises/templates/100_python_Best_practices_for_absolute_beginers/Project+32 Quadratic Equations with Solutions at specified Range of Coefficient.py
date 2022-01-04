_______ math
x1  i..(input("Insert the value of x1: "))
x2  i..(input("Insert the value of x2: "))
y1  i..(input("Insert the value of y1: "))
y2  i..(input("Insert the value of y2: "))
z1  i..(input("Insert the value of z1: "))
z2  i..(input("Insert the value of z2: "))

x  r..(x1, x2+1)
y  r..(y1, y2+1)
z  r..(z1, z2+1)

___ i __ x:
    __ i __ 0:
        _____
    ___ j __ y:
        ___ k __ z:
            print(i, j, k, end' ')
            A  j*j-4*i*k
            __ A > 0:
                x1  (-j - math.sqrt(A))/(2*i)
                x2  (-j + math.sqrt(A))/(2*i)
                print("Valid", round(x1,2), round(x2,2))
            ____:
                print("Invalid")