class rec: pass              # Empty namespace object

rec.name = 'Bob'             # Just objects with attributes
rec.age = 40

print('#' * 22 + ' Like a C struct or a record')
print(rec.name)              # Like a C struct or a record

x = rec()                    # Instances inherit class names
y = rec()

print('#' * 22 + ' name is stored on the class only')
print(x.name, y.name)               # name is stored on the class only

x.name = 'Sue'               # But assignment changes x only
print('#' * 22 + ' But assignment changes x only')
print(rec.name, x.name, y.name)

print('#' * 22 + ' rec.__dict__.keys())')
print(rec.__dict__.keys())

print('#' * 22 + ' list(x.__dict__.keys()')
print(list(x.__dict__.keys()))

print('#' * 22 + ' list(y.__dict__.keys()')
print(list(y.__dict__.keys()))              # list() not required in Python 2.6
# []

print('#' * 22 + ' x.__class__')
print(x.__class__)

print('#' * 22 + ' rec.__bases__')
print(rec.__bases__)                        # () empty tuple in Python 2.6


def upperName(self):
    return self.name.upper()    # Still needs a self

print('#' * 22 + ' Call as a simple function')
print(upperName(x))                   # Call as a simple function

rec.method = upperName

print('#' * 22 + ' Run  method to process x')
print(x.method())                             # Run  method to process x

print('#' * 22 + ' Same, but pass y to self')
print(y.method())                              # Same, but pass y to self

print('#' * 22 + ' Can call through instance or class')
print(rec.method(x))                           # Can call through instance or class

