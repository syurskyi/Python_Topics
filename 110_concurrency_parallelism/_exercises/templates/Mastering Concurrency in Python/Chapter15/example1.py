# ch15/example1.py

______ ___

print(f'Reference count when direct-referencing: {___.getrefcount([7])}.')

a _ [7]
print(f'Reference count when referenced once: {___.getrefcount(a)}.')

b _ a
print(f'Reference count when referenced twice: {___.getrefcount(a)}.')

###########################################################################

a[0] _ 8
print(f'Variable a after a is changed: {a}.')
print(f'Variable b after a is changed: {b}.')

print('Finished.')
