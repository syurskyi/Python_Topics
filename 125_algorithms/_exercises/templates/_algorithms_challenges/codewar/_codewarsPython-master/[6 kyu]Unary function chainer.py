___ chained(f
    z = lambda x:x
    for func in f:
        func(z)
        r_ z
         




___ f1(x r_ x*2
___ f2(x r_ x+2
___ f3(x r_ x**2
___ f4(x r_ x.split()
___ f5(xs r_ [x[::-1].title() for x in xs]
___ f6(xs r_ "_".join(xs)

print(chained([f1,f2,f3])(0)) #4 

