_______ random

x  {1:"a", 2: "b", 3: "c", 4: "d", 5: "e"}
print(x)

keys  l..(x.keys())
del_keys  random.choice(keys)
del x[del_keys]

print(x)