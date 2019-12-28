print('#' * 52 + ' By position')
template = '{0}, {1} and {2}'  # By position
print(template.format('spam', 'ham', 'eggs'))

print('#' * 52 + ' By keyword')
template = '{motto} , {pork} and {food}'  # By keyword
print(template.format(motto='spam', pork='ham', food='eggs'))

print('#' * 52 + ' By both')
template = '{motto}, {} and {food}'  # By both
print(template.format('ham', motto='spam', food='eggs'))

print('#' * 52 + ' By relative position')
template = '{}, {} and {}'  # By relative position
#
print('#' * 52 + ' New in 3.1 and 2.7')
print(template.format('spam', 'ham', 'eggs')) #  New in 3.1 and 2.7

print('#' * 52 + ' Same via expression')
template = '%s, %s and %s'  # Same via expression
print(template % ('spam', 'ham', 'eggs'))
template = '%(motto)s, %(pork)s and %(food)s'
print(template % dict(motto='spam', pork='ham', food='eggs'))
print('{motto}, {0} and  {food}'.format(42, motto=3.14, food=[1, 2]))
X = '{motto} , {0} and {food}'.format(42, motto=3.14, food=[1, 2])
print(X)
print(X.split(' and '))
Y = X.replace('and', 'but under no circumstances')
print(Y)
