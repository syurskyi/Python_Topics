# Генераторы словарей
keys = ["a", "b"]  # Список с ключами
values = [1, 2] # Список со значениями
print({k: v for (k, v) in zip(keys, values)})
#  {'a': 1, 'b': 2}
print({k: 0 for k in keys})
#  {'a': 0, 'b': 0}
d = {"a": 1, "b": 2, "c": 3, "d": 4 }
print({k: v for (k, v) in d.items() if v % 2 == 0})
# # {'b': 2, 'd': 4}

# Zip together keys and values
print(list(zip(['a', 'b', 'c'], [1, 2, 3])))

# Make a dict from zip result
D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))


# dict comprehension
D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)

# dict comprehension
# Or: range(1, 5)
D = {x: x ** 2 for x in [1, 2, 3, 4]}
print(D)

# dict comprehension
# Loop over any iterable
D = {c: c * 4 for c in 'SPAM'}
print(D)

D = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
print(D)

# Initialize dict from keys
# with a comprehension
D = dict.fromkeys(['a', 'b', 'c'], 0)
# Initialize dict from keys
print(D)
D = {k:0 for k in ['a', 'b', 'c']}
# Same, but with a comprehension
print(D)