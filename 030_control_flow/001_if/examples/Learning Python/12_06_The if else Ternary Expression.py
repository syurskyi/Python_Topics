__author__ = 'sergejyurskyj'

"""
if X:
    A = Y
else:
    A = Z
"""

# A = Y if X else Z        # doesn't work


A = 't' if 'spam' else 'f'      # Nonempty is true
print(A)

A = 't' if '' else 'f'
print(A)


# A = ((X and Y) or Z)     # doesn't work

# A = [Z, Y][bool(X)]      # doesn't work

print(['f', 't'][bool('')])

print(['f', 't'][bool('spam')])

