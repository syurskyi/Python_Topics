
class A:
    attr = 1         # Classic (Python 2.6)


class B(A):          # B and C both lead to A
    pass


class C(A):
    attr = 2


class D(B, C):
    pass             # Tries A before C

x = D()
print(x.attr)               # Searches x, D, B, A


class A(object):
    attr = 1         # New-style ("object" not required in 3.0)


class B(A):
    pass


class C(A):
    attr = 2


class D(B, C):
    pass             # Tries C before A

x = D()
print(x.attr)               # Searches x, D, B, C


