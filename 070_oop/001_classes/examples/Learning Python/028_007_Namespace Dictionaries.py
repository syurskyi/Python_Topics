class super:
    def hello(self):
        self.data1 = 'spam'

class sub(super):
    def hola(self):
        self.data2 = 'eggs'


X = sub()
print('#' * 23 + ' Instance namespace dict')
print(X.__dict__)                            # Instance namespace dict

print('#' * 23 + ' Class of instance')
print(X.__class__)                           # Class of instance

print('#' * 23 + ' Superclasses of class')
print(sub.__bases__)                         # Superclasses of class

print('#' * 23 + ' empty tuple in Python 2.6')
print(super.__bases__)                      # () empty tuple in Python 2.6

Y = sub()

X.hello()
print('#' * 23 + ' X.hello(), print(X.__dict__)')
print(X.__dict__)

X.hola()
print('#' * 23 + ' X.hola()--> print(X.__dict__)')
print(X.__dict__)

sub.__dict__.keys()

super.__dict__.keys()

print('#' * 23 + ' print(Y.__dict__)')
print(Y.__dict__)

print('#' * 23 + ' print(X.data1, X.__dict__[data1])')
print(X.data1, X.__dict__['data1'])

X.data3 = 'toast'
print('#' * 23 + ' --> print(X.__dict__)')
print(X.__dict__)


X.__dict__['data3'] = 'ham'
print('#' * 23 + ' X.__dict__[data3] = ham--> print(X.data3)')
print(X.data3)

print('#' * 23 + ' print(X.__dict__, Y.__dict__)')
print(X.__dict__, Y.__dict__)

print('#' * 23 + ' print(list(X.__dict__.keys())) ')
print(list(X.__dict__.keys()))                                  # Need list() in 3.0

# In Python 2.6:

print('#' * 23 + ' print(dir(X))')
print(dir(X))

print('#' * 23 + ' print(dir(sub))')
print(dir(sub))

print('#' * 23 + ' print(dir(super))')
print(dir(super))

# In Python 3.0:

print('#' * 23 + ' print(dir(X))')
print(dir(X))

print('#' * 23 + ' print(dir(sub))')
print(dir(sub))

print('#' * 23 + ' print(dir(super))')
print(dir(super))

