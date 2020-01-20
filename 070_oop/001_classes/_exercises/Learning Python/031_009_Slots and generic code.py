class C:
    __slots__ = ['a', 'b']           # __slots__ means no __dict__ by default

X = C()
X.a = 1
X.a

# X.__dict__
# AttributeError: 'C' object has no attribute '__dict__'
getattr(X, 'a')

setattr(X, 'b', 2)                   # But getattr() and setattr() still work
X.b

'a' in dir(X)                        # And dir() finds slot attributes too

'b' in dir(X)

class D:
    __slots__ = ['a', 'b']
    def __init__(self):
        self.d = 4   # Cannot add new names if no __dict__

# X = D()
# AttributeError: 'D' object has no attribute 'd'



class D:
    __slots__ = ['a', 'b', '__dict__']    # List __dict__ to include one too
    c = 3                                 # Class attrs work normally
    def __init__(self):
        self.d = 4        # d put in __dict__, a in __slots__

X = D()
X.d

X.__dict__                  # Some objects have both __dict__ and __slots__
X.__slots__
X.c

X.a                          # All instance attrs undefined until assigned
# AttributeError: a
X.a = 1
getattr(X, 'a',), getattr(X, 'c'), getattr(X, 'd')

for attr in list(X.__dict__) + X.__slots__:
    print(attr, '=>', getattr(X, attr))

# d = > 4
# a = > 1
# b = > 2
# __dict__ = > {'d': 4}

for attr in list(getattr(X, '__dict__', []))  + getattr(X, '-slots', []):
    print(attr, '=>', getattr(X, attr))

# d = > 4
# a = > 1
# b = > 2
# __dict__ = > {'d': 4}

