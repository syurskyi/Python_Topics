# Raising Exceptions
raise IndexError             # Class (instance created)
raise IndexError()           # Instance (created in statement)

exc = IndexError()           # Create instance ahead of time
raise exc

excs = [IndexError, TypeError]
raise excs[0]

try:
    ...
except IndexError as X:      # X assigned the raised instance object
   ...