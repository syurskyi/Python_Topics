# Enumerate a List

L = ['apples', 'bananas', 'oranges']
for idx, val in enumerate(L):
  print("index is %d and value is %s" % (idx, val))


# index is 0 and value is apples
# index is 1 and value is bananas
# index is 2 and value is oranges


# Enumerate a Tuple

t = ('apples', 'bananas', 'oranges')
for idx, val in enumerate(t):
  print("index is %d and value is %s" % (idx, val))

# index is 0 and value is apples
# index is 1 and value is bananas
# index is 2 and value is oranges

# Enumerate a List of Tuples (The Neat Way)

L = [('Matt', 20), ('Karim', 30), ('Maya', 40)]

for idx, val in enumerate(L):
  name = val[0]
  age = val[1]
  print("index is %d, name is %s, and age is %d" \
         % (idx, name, age))

# index is 0, name is Matt, and age is 20
# index is 1, name is Karim, and age is 30
# index is 2, name is Maya, and age is 40

for idx, (name, age) in enumerate(L):
  print("index is %d, name is %s, and age is %d" \
        % (idx, name, age))

# Enumerate a String

str = "Python"
for idx, ch in enumerate(str):
  print("index is %d and character is %s" \
         % (idx, ch))


# index is 0 and character is P
# index is 1 and character is y
# index is 2 and character is t
# index is 3 and character is h
# index is 4 and character is o
# index is 5 and character is n

# Enumerate with a Different Starting Index

L = ['apples', 'bananas', 'oranges']
for idx, s in enumerate(L, start = 1):
  print("index is %d and value is %s" \
         % (idx, s))

# index is 1 and value is apples
# index is 2 and value is bananas
# index is 3 and value is oranges

# Why It doesn’t Make Sense to Enumerate Dictionaries and Sets

d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
  # k is now the key
  # v is the value
  print(k, v)

s = {'a', 'b', 'c'}
for v in s:
  print(v)

# Advanced: Enumerate Deep Dive

list(enumerate(['a', 'b', 'c']))
# [(0, 'a'), (1, 'b'), (2, 'c')]

for idx, val in enumerate(['a', 'b']):
  print(idx, val)

# 0 a
# 1 b

for i in enumerate(['a', 'b']):
  print(i[0], i[1])

# 0 a
# 1 b