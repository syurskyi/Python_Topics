___ chained(f):
    z = lambda x:x
    for func in f:
        func(z)
        return z
         




___ f1(x): return x*2
___ f2(x): return x+2
___ f3(x): return x**2
___ f4(x): return x.split()
___ f5(xs): return [x[::-1].title() for x in xs]
___ f6(xs): return "_".join(xs)

print(chained([f1,f2,f3])(0)) #4 

