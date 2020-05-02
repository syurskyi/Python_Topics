c_ simpleClass(object
    ___ __intit__(selfs
        a = 10
        b = 20

    ___ method1 
        print('I am method 1')

    ___ method2 
        print('I am method 2')

s = simpleClass()
atr = 'method1'
print(atr in dir(s))
b = 1
print(type(b) __ type(0))
print(hasattr(s, atr))

m = getattr(s, atr)
print(m())
print(s.method1())

print(getattr(s, atr)())

setattr(s, 'x', 123)