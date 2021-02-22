# # Generator Functions Versus Generator Expressions
# # Generator expression
# # Force generator to produce all results
# # Generator function
# # Iterate automatically
# # Iterate manually
#
# c
G = (c * 4 for c in 'SPAM')   # Generator expression

print(list(G))   # Force generator to produce all results

def timesfour(S):   # Generator function
    for c in S:
        yield c * 4


G = timesfour('spam')
print(list(G))   # Iterate automatically

G = (c * 4 for c in 'SPAM')
I = iter(G)   # Iterate manually
print(next(I))
print(next(I))
print()
G = timesfour('spam')
I = iter(G)
print(next(I))
print(next(I))

# # Generator Functions Versus Generator Expressions
# # Function ___ gensub line : or
# #  ''.join x.upper    Expression
print()

line = 'aa bbb c'
# x
print(''.join(x.upper() for x in line.split() if len(x)> 1))   # Expression


def gensub(line):   # Function
    for x in line.split():
        if len(x) > 1:
            yield x.upper()


print(''.join(gensub(line)))  # But why generate?
