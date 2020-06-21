class C:
    data = 'spam'                          # 2.6 only
    def __cmp__(self, other):              # __cmp__ not used in 3.0
        return cmp(self.data, other)       # cmp() not defined in 3.0

X = C()
print('#' * 23 + ' True  (runs __cmp__)')
print(X > 'ham')         # True  (runs __cmp__)
print('#' * 23 + ' False (runs __cmp__)')
print(X < 'ham')         # False (runs __cmp__)



class C:
    data = 'spam'
    def __cmp__(self, other):
        return (self.data > other) - (self.data < other)
