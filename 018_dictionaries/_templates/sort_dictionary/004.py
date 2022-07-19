# Sort Dictionary Using a for Loop

dict1 = {1: 1, 2: 9, 3: 4}
sorted_values = s.. ?.v.. # Sort the values
sorted_dict  # dict

___ i __ ?
    ___ k __ ?.k..
        __ ? ? __ ?
            ? ? = ? ?
            b..

print ?

# Sort Dictionary Using the sorted() Function

dict1 = {1: 1, 2: 9, 3: 4}
sorted_dict # dict
sorted_keys = s.. ? k.._?.g..  # [1, 3, 2]

___ w __ ?
    ? ? = ? ?

print ? # {1: 1, 3: 4, 2: 9}

# Sort Dictionary Using the operator Module and itemgetter()

_____ o__

dict1 = {1: 1, 2: 9}
get_item_with_key_2 = o__.i.. 2

print ? ?  # 9

_____ o__

dict1 = {1: 1, 2: 9, 3: 4}
sorted_tuples = s.. ?.i.., k.._o__.i.. 1
print(sorted_tuples)  # [(1, 1), (3, 4), (2, 9)]
sorted_dict = {k: v ___ k, v __ sorted_tuples}

print(sorted_dict) # {1: 1, 3: 4, 2: 9}

# Sort Dictionary Using a Lambda Function

dict1 = {1: 1, 2: 9, 3: 4}
sorted_tuples = s..(dict1.i.., k.._l... item: item[1])
print(sorted_tuples)  # [(1, 1), (3, 4), (2, 9)]
sorted_dict = {k: v ___ k, v __ sorted_tuples}

print(sorted_dict)  # {1: 1, 3: 4, 2: 9}

# Returning a New Dictionary with Sorted Values

_____ o__
_____ c.. _____ O..

dict1 = {1: 1, 2: 9, 3: 4}
sorted_tuples = s..(dict1.i.., key=o__.i..(1))
print(sorted_tuples)  # [(1, 1), (3, 4), (2, 9)]

sorted_dict = O..()
___ k, v __ sorted_tuples:
    sorted_dict[k] = v

print(sorted_dict)  # {1: 1, 3: 4, 2: 9}
