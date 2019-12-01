class Commuter:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val

x = Commuter(88)
y = Commuter(99)

print('#' * 23 + ' __add__: instance + noninstance')
x + 1                         # __add__: instance + noninstance
# add 88 1

print('#' * 23 + ' __radd__: noninstance + instance')
1 + y                         # __radd__: noninstance + instance
# radd 99 1

print('#' * 23 + ' __add__: instance + instance, triggers __radd__')
x + y                         # __add__: instance + instance, triggers __radd__


class Commuter:                        # Propagate class type in results
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        if isinstance(other, Commuter): other = other.val
        return Commuter(self.val + other)

    def __radd__(self, other):
        return Commuter(other + self.val)

    def __str__(self):
        return '<Commuter: %s>' % self.val

x = Commuter(88)
y = Commuter(99)
print('#' * 23 + ' Result is another Commuter instance')
print(x + 10)                          # Result is another Commuter instance

print(10 + y)


z = x + y                              # Not nested: doesn't recur to __radd__
print('#' * 23 + ' Not nested: doesnt recur to __radd__')
print(z)

print(z + 10)
print(z + z)


class Number:
    def __init__(self, val):
        self.val = val

    def __iadd__(self, other):             # __iadd__ explicit: x += y
        self.val += other                  # Usually returns self
        return self

print('#' * 23 + '  __iadd__ explicit: x += y')
print('#' * 23 + ' Usually returns self')
x = Number(5)
x += 1
x += 1
print(x.val)


class Number:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):              # __add__ fallback: x = (x + y)
        return Number(self.val + other)    # Propagates class type

print('#' * 23 + ' __add__ fallback: x = (x + y)')
print('#' * 23 + ' Propagates class type')
x = Number(5)
x += 1
x += 1
print(x.val)


