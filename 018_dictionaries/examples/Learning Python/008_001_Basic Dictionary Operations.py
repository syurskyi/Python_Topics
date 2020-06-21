__author__ = 'sergejyurskyj'

D = {'spam': 2, 'ham': 1, 'eggs': 3}    # Make a dictionary
D['spam']                               # Fetch a value by key
print(D)                                       # Order is scrambled

print('#' * 52 + ' Number of entries in dictionary')
print(len(D))                         # Number of entries in dictionary

print('#' * 52 + ' Key membership test alternative')
print('ham' in D)                     # Key membership test alternative

print('#' * 52 + ' Create a new list of my keys')
print(list(D.keys()))                 # Create a new list of my keys

print('#' * 52 + ' Change entry')
print(D)
D['ham'] = ['grill', 'bake', 'fry']       # Change entry
print(D)

print('#' * 52 + ' Delete entry')
del D['eggs']                             # Delete entry
print(D)
print('#' * 52 + ' Add new entry')

D['brunch'] = 'Bacon'                     # Add new entry
print(D)
