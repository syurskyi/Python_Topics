class Callee:
    def __call__(self, *pargs, **kargs):   # Intercept instance calls
        print('Called:', pargs, kargs)     # Accept arbitrary arguments

C = Callee()
print('#' * 23 + ' C is a callable object')
C(1, 2, 3)                                 # C is a callable object
C(1, 2, 3, x=4, y=5)

# class C:
#     def __call__(self, a, b, c=5, d=6):       # Normals and defaults
#
# # class C:
#     # def __call__(self, *pargs, **kargs):      # Collect arbitrary arguments
#
# class C:
#     def __call__(self, d=6, *pargs, **kargs):   # 3.0 keyword-only argument
#
X = Callee()
print('#' * 23 + ' Omit defaults')
X(1, 2)                             # Omit defaults
print('#' * 23 + '  Positionals')
X(1, 2, 3, 4)                       # Positionals
print('#' * 23 + ' Keywords')
X(a=1, b=2, d=4)                    # Keywords
print('#' * 23 + ' Unpack arbitrary arguments')
X(*[1, 2], **dict(c=3, d=4))        # Unpack arbitrary arguments
print('#' * 23 + ' Mixed modes')
X(1, *(2,), c=3, **dict(d=4))       # Mixed modes

#
class Prod:
    def __init__(self, value):             # Accept just one argument
        self.value = value

    def __call__(self, other):
        return self.value * other

x = Prod(2)                                # "Remembers" 2 in state
print('#' * 23 + ' "Remembers" 2 in state')
print(x(3))                                       # 3 (passed) * 2 (state)
print('#' * 23 + ' "3 (passed) * 2 (state)')
print(x(4))


class Prod:
    def __init__(self, value):
        self.value = value
    def comp(self, other):
        return self.value * other

x = Prod(3)
print('#' * 23)
print(x.comp(3))
#
print(x.comp(4))
#
#
#
#
class Callback:
    def __init__(self, color):               # Function + state information
        self.color = color

    def __call__(self):                      # Support calls with no arguments
        print('turn', self.color)


# cb1 = Callback('blue')                       # Remember blue
# cb2 = Callback('green')
#
# B1 = Button(command=cb1)                     # Register handlers
# B2 = Button(command=cb2)                     # Register handlers
#
#
# cb1()                                        # On events: prints 'blue'
# cb2()                                        # Prints 'green'
#
#
#
# cb3 = (lambda color='red': 'turn ' + color)  # Or: defaults
# print(cb3())
#
#
#
# class Callback:
#     def __init__(self, color):               # Class with state information
#         self.color = color
#     def changeColor(self):                   # A normal named method
#         print('turn', self.color)
#
# cb1 = Callback('blue')
# cb2 = Callback('yellow')
#
# B1 = Button(command=cb1.changeColor)         # Reference, but don't call
# B2 = Button(command=cb2.changeColor)         # Remembers function+self
#
#
#
# object = Callback('blue')
# cb = object.changeColor                      # Registered event handler
# cb()                                         # On event prints 'blue'
