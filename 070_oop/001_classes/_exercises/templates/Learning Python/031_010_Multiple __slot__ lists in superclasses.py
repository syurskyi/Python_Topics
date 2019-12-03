
class E:
    __slots__ = ['c', 'd']            # Superclass has slots

class D(E):
    __slots__ = ['a', '__dict__']     # So does its subclass

X = D()
X.a = 1; X.b = 2; X.c = 3             # The instance is the union
X.a, X.c

E.__slots__                           # But slots are not concatenated
D.__slots__
X.__slots__                           # Instance inherits *lowest* __slots__
X.__dict__                            # And has its own an attr dict

for attr in list(getattr(X, '__dict__', [])) + getattr(X, '__slots__', []):
    print(attr, '=>', getattr(X, attr))

# b => 2                                    # Superclass slots missed!
# a => 1
# __dict__ => {'b': 2}

dir(X)                                # dir() includes all slot names
