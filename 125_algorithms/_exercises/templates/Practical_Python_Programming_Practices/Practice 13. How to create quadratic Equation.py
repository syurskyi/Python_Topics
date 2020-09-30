from math ______ sqrt

x _ fl..(input("Insert x = "))
y _ fl..(input("Insert y = "))
z _ fl..(input("Insert z = "))

a _ y*y-4*x*z

__ a>0:
    x1 _ (-y + sqrt(a))/(2*x)
    x2 _ (-y - sqrt(a))/(2*x)
    print("x1 = %.2f; x2 = %.2f" % (x1,x2))
elif a__0:
    x1 _ -y/(2*x)
    print("x1 = %.2f" % x1)
____
    print("No roots exist")