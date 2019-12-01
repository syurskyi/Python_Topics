class X:
    a = 1       # Class attribute

I = X()
I.a             # Inherited by instance

X.a


X.a = 2         # May change more than X
I.a             # I changes too

J = X()         # J inherits from X's runtime values
J.a             # (but assigning to J.a changes a in J, not X or I)
2

class X: pass                       # Make a few attribute namespaces
class Y: pass

X.a = 1                             # Use class attributes as variables
X.b = 2                             # No instances anywhere to be found
X.c = 3
Y.a = X.a + X.b + X.c

for X.i in range(Y.a): print(X.i)   # Prints 0..5

class Record: pass
X = Record()
X.name = 'bob'
X.job  = 'Pizza maker'
