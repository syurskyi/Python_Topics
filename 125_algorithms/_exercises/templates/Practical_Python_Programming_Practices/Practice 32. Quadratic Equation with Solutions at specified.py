______ math
x1 _ in.(input("Insert the value of x1: "))
x2 _ in.(input("Insert the value of x2: "))
y1 _ in.(input("Insert the value of y1: "))
y2 _ in.(input("Insert the value of y2: "))
z1 _ in.(input("Insert the value of z1: "))
z2 _ in.(input("Insert the value of z2: "))

x _ ra..(x1, x2+1)
y _ ra..(y1, y2+1)
z _ ra..(z1, z2+1)

___ i __ x:
    __ i __ 0:
        continue
    ___ j __ y:
        ___ k __ z:
            print(i, j, k, end_' ')
            A _ j*j-4*i*k
            __ A >_ 0:
                x1 _ (-j - math.sqrt(A))/(2*i)
                x2 _ (-j + math.sqrt(A))/(2*i)
                print("Valid", round(x1,2), round(x2,2))
            ____
                print("Invalid")