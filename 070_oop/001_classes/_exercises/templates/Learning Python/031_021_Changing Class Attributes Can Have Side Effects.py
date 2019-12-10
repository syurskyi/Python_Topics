# c_ X
#     a = 1       # Class attribute
#
# I = ?
# I.a             # Inherited by instance
#
# X.a
#
#
# X.a = 2         # May change more than X
# I.a             # I changes too
#
# J = X()         # J inherits from X's runtime values
# J.a             # (but assigning to J.a changes a in J, not X or I)
# 2
#
# c_ X p..                       # Make a few attribute namespaces
# c_ Y p..
#
# X.a = 1                             # Use class attributes as variables
# X.b = 2                             # No instances anywhere to be found
# X.c = 3
# Y.a = X.a + X.b + X.c
#
# ___ X.i i_ ra.. Y.a print(X.i)   # Prints 0..5
#
# c_ Record p..
# X = ?
# ?.name = 'bob'
# ?.job  = 'Pizza maker'
