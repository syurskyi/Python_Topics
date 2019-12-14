__author__ = 'sergejyurskyj'


D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(list(D.values()))
print(list(D.items()))

print('#' * 52 + ' key that is there')
print(D.get('spam'))              # A key that is there

print('#' * 52 + ' key that is missing')
print(D.get('toast'))      # A key that is missing

print(D.get('toast', 88))
print(D)

D2 = {'toast': 4, 'muffin': 5}
D.update(D2)
print(D)

# pop a dictionary by key
print('#' * 52 + ' pop a dictionary by key')
print(D)
D.pop('muffin')
print(D)

print('#' * 52 + ' Delete and return from a key')
D.pop('toast')                # Delete and return from a key
print(D)

# pop a list by position
print('#' * 52 + ' pop a list by position')
L = ['aa', 'bb', 'cc', 'dd']
print(L)

print('#' * 52 + ' Delete and return from the end')
L.pop()                       # Delete and return from the end
print(L)

print('#' * 52 + ' Delete from a specific position')
L.pop(1)                      # Delete from a specific position
print(L)
