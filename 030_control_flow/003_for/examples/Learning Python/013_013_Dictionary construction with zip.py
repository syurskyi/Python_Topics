__author__ = 'sergejyurskyj'

D1 = {'spam': 1, 'eggs': 3, 'toast': 5}
D1

D1 = {}
D1['spam'] = 1
D1['eggs'] = 3
D1['toast'] = 5

keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]

print(list(zip(keys, vals)))

D2 = {}
for (k, v) in zip(keys, vals): D2[k] = v

print(D2)

keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]

D3 = dict(zip(keys, vals))
print(D3)

print({k: v for (k, v) in zip(keys, vals)})
