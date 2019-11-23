# defaultdict
# The defaultdict is a specialized dictionary found in the collections module. (It is a subclass of the dict type).

from collections import defaultdict

# Standard dictionaries in Python will raise an exception if we try to access a non-existent key:

d = {}
# d['a']  # ERROR KeyError: 'a'

# Now, we can certainly use the .get method:

result = d.get('a')
type(result)
# NoneType

# And we can even specify a default value for the key if it is not present:

d.get('a', 0)
# 0

# Often we have dictionaries where we want to return a consistent default value if the requested key does not exist.
# Although we can do so using the .get method as above, we have to remember to use the same default value every time
# - plus it gets a little cumbersome.
# Let's say we want to keep track of the number of occurrences of individual characters in a string.
# We might approach it this way:

counts = {}
sentence = "able was I ere I saw elba"

for c in sentence:
    if c in counts:
        counts[c] += 1
    else:
        counts[c] = 1

print(counts)
# {'a': 4, 'b': 2, 'l': 2, 'e': 4, ' ': 6, 'w': 2, 's': 2, 'I': 2, 'r': 1}

# So this works, but we have that if statement - it would be nice to simplify our code somewhat:

counts = {}
for c in sentence:
    counts[c] = counts.get(c, 0) + 1

print(counts)
# {'a': 4, 'b': 2, 'l': 2, 'e': 4, ' ': 6, 'w': 2, 's': 2, 'I': 2, 'r': 1}

# So, that works well and is much cleaner. But if we have to specify that default value (0 in this case) many times
# in our code when working with the same dictionary, we have to remember what the default needs to be each time.
# Instead, we could use a defaultdict. In a defaultdict we specify what the default value is for a missing key -
# more precisely, we specify a default factory method that is called:

counts = defaultdict(lambda : 0)
for c in sentence:
    counts[c] += 1

print(counts)
# defaultdict(<function __main__.<lambda>()>,
#             {'a': 4,
#              'b': 2,
#              'l': 2,
#              'e': 4,
#              ' ': 6,
#              'w': 2,
#              's': 2,
#              'I': 2,
#              'r': 1})

# As you can see that simplified our code quite a bit, but the result is not quite a dictionary - it is a defaultdict.
# However, it inherits from dict so all the dictionary methods we have grown to know and love are still available
# because defaultdict is a dict:

print(isinstance(counts, defaultdict))
# True

print(isinstance(counts, dict))
# True

# And counts behaves like a regular dictionary too:

print(counts.items())
# dict_items([('a', 4), ('b', 2), ('l', 2), ('e', 4), (' ', 6), ('w', 2), ('s', 2), ('I', 2), ('r', 1)])

print(counts['a'])
# 4

# The main difference is when we request a non-existent key:

print(counts['python'])
# 0

# We get the default value back - not only that, but it actually created that key as well:

print(counts)
#
# defaultdict(<function __main__.<lambda>()>,
#             {'a': 4,
#              'b': 2,
#              'l': 2,
#              'e': 4,
#              ' ': 6,
#              'w': 2,
#              's': 2,
#              'I': 2,
#              'r': 1,
#              'python': 0})
#
# So this is a bit different from using .get.
# And of course we can manipulate our dictionary just like a standard dictionary:

counts['hello'] = 'world'
print(counts)
# defaultdict(<function __main__.<lambda>()>,
#             {'a': 4,
#              'b': 2,
#              'l': 2,
#              'e': 4,
#              ' ': 6,
#              'w': 2,
#              's': 2,
#              'I': 2,
#              'r': 1,
#              'python': 0,
#              'hello': 'world'})


del counts['hello']
counts

# defaultdict(<function __main__.<lambda>()>,
#             {'a': 4,
#              'b': 2,
#              'l': 2,
#              'e': 4,
#              ' ': 6,
#              'w': 2,
#              's': 2,
#              'I': 2,
#              'r': 1,
#              'python': 0})

# Very often you will see what looks like a type specified as the default factory - but keep in mind that it is in
# fact the corresponding functions (constructors) that are actually being specified.

print(int())
# 0

print(bool())
# False

print(str())
# ''

print(list())
# []

d = defaultdict(int)
print(d['a'])
# 0

d = defaultdict(bool)
print(d['a'])
# False

d = defaultdict(str)
print(d['a'])
# ''

d = defaultdict(list)
print(d['a'])
# []

# Note that this no different than writing:

d = defaultdict(lambda: list())
print(d['a'])
# []