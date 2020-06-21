class C:
    pass

class D:
    pass

c = C()
d = D()
print('#' * 23 + ' 3.0: compares the instances classes')
print(type(c) == type(d))                 # 3.0: compares the instances' classes


print(type(c), type(d))

c.__class__, d.__class__


c1, c2 = C(), C()
print(type(c1) == type(c2))


class C:
    pass


class D:
    pass

c = C()
d = D()
print('#' * 23 + ' 2.6: all instances are same type')
print(type(c) == type(d))                 # 2.6: all instances are same type

print('#' * 23 + ' Must compare classes explicitly')
print(c.__class__ == d.__class__)         # Must compare classes explicitly

print(type(c), type(d))

print(c.__class__, d.__class__)


class C(object):
    pass


class D(object):
    pass

c = C()
d = D()
print('#' * 23 + ' But classes are not the same as types')
print(type(c) == type(d))                 # 2.6 new-style: same as all in 3.0

print(type(c), type(d))
print(c.__class__, d.__class__)
