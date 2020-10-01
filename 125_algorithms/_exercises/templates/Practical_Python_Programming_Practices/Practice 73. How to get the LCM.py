___ LCM(x,y):
    z _ x*y
    w___ x !_ 0 an. y !_ 0:
        __ x > y:
            x %_ y
        ____
            y %_ x
    r_ z//(x+y)

a _ in.(i..("Insert value of a: "))
b _ in.(i..("Insert value of b: "))

print("The LCM = ", LCM(a,b))