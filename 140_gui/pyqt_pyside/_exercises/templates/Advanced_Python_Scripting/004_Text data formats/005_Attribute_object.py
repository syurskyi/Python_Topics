class simpleClass(object):
    def __intit__(selfs):
        self.a = 10
        self.b = 20

    def method1(self):
        print('I am method 1')

    def method2(self):
        print('I am method 2')

s = simpleClass()
atr = 'method1'
print(atr in dir(s))
b = 1
print(type(b) == type(0))
print(hasattr(s, atr))

m = getattr(s, atr)
print(m())
print(s.method1())

print(getattr(s, atr)())

setattr(s, 'x', 123)