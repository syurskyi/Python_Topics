# Default Printing and State
raise IndexError                    # Same as IndexError(): no arguments

raise IndexError('spam')            # Constructor argument attached, printed

I = IndexError('spam')              # Available in object attribute
I.args
# ('spam',)
print(I)

class E(Exception): pass

raise E

raise E('spam')

I = E('spam')
I.args
print(I)

try:
  raise E('spam')
except E as X:
  print(X, X.args)                 # Displays and saves construtor arguments

# spam ('spam',)

try:
  raise E('spam', 'eggs', 'ham')
except E as X:
  print(X, X.args)
