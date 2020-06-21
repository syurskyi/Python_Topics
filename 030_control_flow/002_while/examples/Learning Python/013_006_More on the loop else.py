__author__ = 'sergejyurskyj'


found = False
while x and not found:
    if match(x[0]):                  # Value at front?
        print('Ni')
        found = True
    else:
        x = x[1:]                    # Slice off front and repeat
if not found:
    print('not found')



while x:                             # Exit when x empty
    if match(x[0]):
        print('Ni')
        break                        # Exit, go around else
    x = x[1:]
else:
    print('Not found')               # Only here if exhausted x

