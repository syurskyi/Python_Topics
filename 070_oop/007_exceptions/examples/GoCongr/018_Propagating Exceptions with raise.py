# Propagating Exceptions with raise
try:
    raise IndexError('spam') # Exceptions remember arguments
except IndexError:
    print('propagating')
    raise # Reraise most recent exception

# propagating
# Traceback (most recent call last):
# File "<stdin>", line 2, in <module>
# IndexError: spam