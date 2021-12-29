___ chained(f):
    z = l.... x:x
    ___ func __ f:
        func(z)
        r.. z
         




___ f1(x): r.. x*2
___ f2(x): r.. x+2
___ f3(x): r.. x**2
___ f4(x): r.. x.s..
___ f5(xs): r.. [x[::-1].t.. ___ x __ xs]
___ f6(xs): r.. "_".join(xs)

print(chained([f1,f2,f3])(0)) #4 

