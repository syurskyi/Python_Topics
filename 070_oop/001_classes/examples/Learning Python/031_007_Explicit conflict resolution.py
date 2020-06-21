class A:
    attr = 1         # Classic


class B(A):
    pass


class C(A):
    attr = 2


class D(B, C):
    attr = C.attr    # Choose C, to the right

x = D()
print('#' * 23 + ' Works like new-style (all 3.0)')
print(x.attr)               # Works like new-style (all 3.0)


class A(object):
    attr = 1         # New-style


class B(A):
    pass


class C(A):
    attr = 2


class D(B, C):
    attr = B.attr    # Choose A.attr, above

x = D()
print('#' * 23 + ' Works like classic (default 2.6)')
print(x.attr)               # Works like classic (default 2.6)


class A:
    def meth(s):
        print('A.meth')


class C(A):
    def meth(s):
        print('C.meth')


class B(A):
    pass


class D(B, C):
    pass                       # Use default search order
x = D()                        # Will vary per class type
print('#' * 23 + 'Use default search order. Will vary per class type. Defaults to classic order in 2.6')
print(x.meth())                       # Defaults to classic order in 2.6
print(A.meth)


class D(B, C):
    meth = C.meth   # Pick C's method: new-style (and 3.0)
x = D()
print('#' * 23 + 'Pick Cs method: new-style (and 3.0)')
print(x.meth())
print(C.meth)


class D(B, C):
    meth = B.meth   # Pick B's method: classic
x = D()
print('#' * 23 + 'Pick Bs method: classic')
print(x.meth())
print(A.meth)


class D(B, C):
    def meth(self):                # Redefine lower
        C.meth(self)               # Pick C's method by calling
