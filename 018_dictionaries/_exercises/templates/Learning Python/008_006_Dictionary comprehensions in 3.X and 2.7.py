__author__ = 'sergejyurskyj'

print('#' * 52 + ' Zip together keys and values')
print(list(zip(['a', 'b', 'c'], [1, 2, 3])))        # Zip together keys and values

print('#' * 52 + ' Make a dict from zip result')
D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))    # Make a dict from zip result
print(D)

# dict comprehension
print('#' * 52 + ' dict comprehension')

D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)

print('#' * 52 + ' Or: range(1, 5)')
D = {x: x ** 2 for x in [1, 2, 3, 4]}     # Or: range(1, 5)
print(D)

print('#' * 52 + ' Loop over any iterable')
D = {c: c * 4 for c in 'SPAM'}            # Loop over any iterable
print(D)

D = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
print(D)

print('#' * 52 + ' Initialize dict from keys')
D = dict.fromkeys(['a', 'b', 'c'], 0)       # Initialize dict from keys
print(D)

print('#' * 52 + ' Same, but with a comprehension')
D = {k:0 for k in ['a', 'b', 'c']}          # Same, but with a comprehension
print(D)

print('#' * 52 + ' Other iterators, default value')
D = dict.fromkeys('spam')                   # Other iterators, default value
print(D)

D = {k: None for k in 'spam'}
print(D)
