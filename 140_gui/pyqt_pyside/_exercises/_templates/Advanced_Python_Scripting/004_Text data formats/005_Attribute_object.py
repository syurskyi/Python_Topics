c_ simpleClass(object
    ___ __intit__(selfs
        a _ 10
        b _ 20

    ___ method1 
        print('I am method 1')

    ___ method2 
        print('I am method 2')

s _ simpleClass
atr _ 'method1'
print(atr __ dir(s))
b _ 1
print(ty..(b) __ ty..(0))
print(hasattr(s, atr))

m _ getattr(s, atr)
print(m())
print(s.method1())

print(getattr(s, atr)())

setattr(s, 'x', 123)