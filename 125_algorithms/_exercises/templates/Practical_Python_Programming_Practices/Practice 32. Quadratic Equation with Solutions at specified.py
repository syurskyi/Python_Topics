import math
x1 = int(input("Insert the value of x1: "))
x2 = int(input("Insert the value of x2: "))
y1 = int(input("Insert the value of y1: "))
y2 = int(input("Insert the value of y2: "))
z1 = int(input("Insert the value of z1: "))
z2 = int(input("Insert the value of z2: "))

x = ra..(x1, x2+1)
y = ra..(y1, y2+1)
z = ra..(z1, z2+1)

___ i __ x:
    if i == 0:
        continue
    ___ j __ y:
        ___ k __ z:
            print(i, j, k, end=' ')
            A = j*j-4*i*k
            if A >= 0:
                x1 = (-j - math.sqrt(A))/(2*i)
                x2 = (-j + math.sqrt(A))/(2*i)
                print("Valid", round(x1,2), round(x2,2))
            else:
                print("Invalid")