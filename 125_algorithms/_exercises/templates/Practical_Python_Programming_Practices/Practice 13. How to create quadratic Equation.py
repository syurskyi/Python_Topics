____ math ______ sqrt

x _ fl..(i..("Insert x = "))
y _ fl..(i..("Insert y = "))
z _ fl..(i..("Insert z = "))

a _ y*y-4*x*z

__ a>0:
    x1 _ (-y + sqrt(a))/(2*x)
    x2 _ (-y - sqrt(a))/(2*x)
    print("x1 = %.2f; x2 = %.2f" % (x1,x2))
____ a__0:
    x1 _ -y/(2*x)
    print("x1 = %.2f" % x1)
____
    print("No roots exist")