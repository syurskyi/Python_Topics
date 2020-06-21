class limiter(object):
    __slots__ = ['age', 'name', 'job']

x = limiter()
x.age                                           # Must assign before use
# AttributeError: age

x.age = 40
x.age

x.ape = 1000                                    # Illegal: not in __slots__
# AttributeError: 'limiter' object has no attribute 'ape'
