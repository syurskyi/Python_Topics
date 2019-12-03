class adder:
    def __init__(self, value=0):
        self.data = value                    # Initialize data
    def __add__(self, other):
        self.data += other                   # Add other in-place (bad!)

x = adder()                                  # Default displays
print('#' * 23 + '  Default displays')
print(x)


class addrepr(adder):                        # Inherit __init__, __add__
    def __repr__(self):                      # Add string representation
        return 'addrepr(%s)' % self.data     # Convert to as-code string

x = addrepr(2)                               # Runs __init__
print(x + 1)                                        # Runs __add__
print('#' * 23 + '  Runs __repr__')
print(x)                                            # Runs __repr__
addrepr(3)
print(x)                                     # Runs __repr__
addrepr(3)
print('#' * 23 + '  Runs __repr__ for both')
print(str(x), repr(x))                              # Runs __repr__ for both

class addstr(adder):
    def __str__(self):                       # __str__ but no __repr__
        return '[Value: %s]' % self.data     # Convert to nice string

x = addstr(3)
x + 1
print('#' * 23 + '  Default __repr__')
x                                            # Default __repr__
print('#' * 23 + '  Runs __str__')
print(x)                                     # Runs __str__

print(str(x), repr(x))



class addboth(adder):
    def __str__(self):
        return '[Value: %s]' % self.data     # User-friendly string
    def __repr__(self):
        return 'addboth(%s)' % self.data     # As-code string

x = addboth(4)
x + 1
x                                            # Runs __repr__
addboth(5)
print('#' * 23 + ' Runs __str__')
print(x)                                     # Runs __str__

print(str(x), repr(x))

class Printer:
    def __init__(self, val):
        self.val = val
    def __str__(self):                  # Used for instance itself
        return str(self.val)            # Convert to a string result

objs = [Printer(2), Printer(3)]
print('#' * 23 + ' __str__ run when instance printed')
print('#' * 23 + ' But not when instance in a list!')
for x in objs: print(x)                 # __str__ run when instance printed
                                        # But not when instance in a list!


print(objs)
# # [<__main__.Printer object at 0x025D06F0>, <__main__.Printer object at ...more...
# objs
# # [<__main__.Printer object at 0x025D06F0>, <__main__.Printer object at ...more...



class Printer:
    def __init__(self, val):
        self.val = val
    def __repr__(self):                 # __repr__ used by print if no __str__
        return str(self.val)            # __repr__ used if echoed or nested

objs = [Printer(2), Printer(3)]
print('#' * 23 + ' No __str__: runs __repr__')
for x in objs: print(x)                 # No __str__: runs __repr__
#
#
#
print('#' * 23 + ' Runs __repr__, not ___str__')
print(objs)                             # Runs __repr__, not ___str__
#
# objs
