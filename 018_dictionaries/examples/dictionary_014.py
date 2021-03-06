# defaultdict
# The defaultdict is a specialized dictionary found in the collections module. (It is a subclass of the dict type).

# Write a Python function that will create and return a dictionary from another dictionary, but sorted by value.
# You can assume the values are all comparable and have a natural sort order.
#
# composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}
#
#  instead of using a dictionary comprehension, we can simply use the dict()
#  function to create a dictionary from the sorted tuples!

composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}

def sort_dict_by_value(d):
    d = {k: v
        for k, v in sorted(d.items(), key=lambda el: el[1])}
    return d

print(sort_dict_by_value(composers))

def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda el: el[1]))

sort_dict_by_value(composers)


# Given two dictionaries, d1 and d2, write a function that creates a dictionary that contains only the keys
# common to both dictionaries, with values being a tuple containg the values from d1 and d2.
# (Order of keys is not important).
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 20, 'c': 30, 'y': 40, 'z': 50}

def intersect(d1, d2):
    d1_keys = d1.keys()
    d2_keys = d2.keys()
    keys = d1_keys & d2_keys
    d = {k: (d1[k], d2[k]) for k in keys}
    return d

intersect(d1, d2)

# You have text data spread across multiple servers.
# Each server is able to analyze this data and return a dictionary that contains words and their frequency.
# Your job is to combine this data to create a single dictionary that contains all the words and their combined
# frequencies from all these data sources. Bonus points if you can make your dictionary sorted by frequency
# (highest to lowest).
# For example, you may have three servers that each return these dictionaries:
#
# d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
# d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
# d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}
