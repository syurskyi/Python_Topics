# Sort Dictionary Using a for Loop

dict1 = {1: 1, 2: 9, 3: 4}
sorted_values = sorted(dict1.values()) # Sort the values
sorted_dict = {}  # dict

for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]
            break

print(sorted_dict)

# Sort Dictionary Using the sorted() Function

dict1 = {1: 1, 2: 9, 3: 4}
sorted_dict = {} # dict
sorted_keys = sorted(dict1, key=dict1.get)  # [1, 3, 2]

for w in sorted_keys:
    sorted_dict[w] = dict1[w]

print(sorted_dict) # {1: 1, 3: 4, 2: 9}

# Sort Dictionary Using the operator Module and itemgetter()

import operator

dict1 = {1: 1, 2: 9}
get_item_with_key_2 = operator.itemgetter(2)

print(get_item_with_key_2(dict1))  # 9

import operator

dict1 = {1: 1, 2: 9, 3: 4}
sorted_tuples = sorted(dict1.items(), key=operator.itemgetter(1))
print(sorted_tuples) # [(1, 1), (3, 4), (2, 9)]
sorted_dict = {k: v for k, v in sorted_tuples}

print(sorted_dict) # {1: 1, 3: 4, 2: 9}

# Sort Dictionary Using a Lambda Function

dict1 = {1: 1, 2: 9, 3: 4}
sorted_tuples = sorted(dict1.items(), key=lambda item: item[1])
print(sorted_tuples)  # [(1, 1), (3, 4), (2, 9)]
sorted_dict = {k: v for k, v in sorted_tuples}

print(sorted_dict)  # {1: 1, 3: 4, 2: 9}

# Returning a New Dictionary with Sorted Values

import operator
from collections import OrderedDict

dict1 = {1: 1, 2: 9, 3: 4}
sorted_tuples = sorted(dict1.items(), key=operator.itemgetter(1))
print(sorted_tuples)  # [(1, 1), (3, 4), (2, 9)]

sorted_dict = OrderedDict()
for k, v in sorted_dict:
    sorted_dict[k] = v

print(sorted_dict)  # {1: 1, 3: 4, 2: 9}
