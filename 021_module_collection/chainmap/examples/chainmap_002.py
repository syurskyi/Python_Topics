# The ChainMap
# ChainMap is used to combine several dictionaries or mappings. It returns a list of dictionaries.
# Import chainmap
# You have to import ChainMap from the collections module before using it.

from collections import ChainMap

# Create a ChainMap
# To create a chainmap we can use ChainMap() constructor. We have to pass the dictionaries we are going to combine as
# an argument set.

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'b': 4}
chain_map = ChainMap(dict1, dict2)
print(chain_map.maps)

# Output:
# [{'b': 2, 'a': 1}, {'c': 3, 'b': 4}]

# You can see a list of dictionary as the output. You can access chain map values by key name.

print(chain_map['a'])

# Output:
# 1

# '1' is printed as the value of key 'a' is 1. Another important point is ChainMap updates its values when its
# associated dictionaries are updated. For example, if you change the value of 'c' in dict2 to '5',
# you will notice the change in ChainMap as well.

dict2['c'] = 5
print(chain_map.maps)

# Output:
# [{'a': 1, 'b': 2}, {'c': 5, 'b': 4}]

# Getting Keys and Values from ChainMap
# You can access the keys of a ChainMap with keys() function. Similarly, you can access the values of elements with
# values() function, as shown below:

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'b': 4}
chain_map = ChainMap(dict1, dict2)
print (list(chain_map.keys()))
print (list(chain_map.values()))

# Output:
# ['b', 'a', 'c']
# [2, 1, 3]

# Notice that the value of the key 'b' in the output is the value of key 'b' in dict1. As a rule of thumb,
# when one key appears in more than one associated dictionaries, ChainMap takes the value for that key from
# the first dictionary.
# Adding a New Dictionary to ChainMap
# If you want to add a new dictionary to an existing ChainMap, use new_child() function. It creates a new ChainMap with
# the newly added dictionary.

dict3 = {'e': 5, 'f': 6}
new_chain_map = chain_map.new_child(dict3)
print(new_chain_map)

# Output:
# ChainMap({'f': 6, 'e': 5}, {'a': 1, 'b': 2}, {'b': 4, 'c': 3})

# Notice that new dictionary is added to the beginning of ChainMap list.
