__author__ = 'sergejyurskyj'

"""
while True:
   print('Type Ctrl-C to stop me!')
"""
x = 'spam'
while x:                  # While x is not empty
    print(x, end=' ')
    x = x[1:]             # Strip first character off x

a=0; b=10
while a < b:              # One way to code counter loops
    print(a, end=' ')
a += 1                # Or, a = a + 1

"""
while True:
    ...loop body...
    if exitTest(): break
"""