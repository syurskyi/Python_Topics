___ LCM(x,y):
    z  x*y
    w___ x ! 0 and y ! 0:
        __ x > y:
            x % y
        else:
            y % x
    return z//(x+y)

a  i..(input("Insert value of a: "))
b  i..(input("Insert value of b: "))

print("The LCM = ", LCM(a,b))