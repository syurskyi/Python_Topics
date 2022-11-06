# # Example 1

words = ['data', 'science', 'machine', 'learning'] #list comprehension
# # i
print([len(i) for i in words])
# # [4, 7, 7, 8]
# # #dictionary comprehension
# # i
print({i: len(i) for i in words})
# # {'data': 4, 'science': 7, 'machine': 7, 'learning': 8}
#
#
# # list = [expression for item in iterable(if conditional)]
# # Dictionary = {expression for key, value in iterable(if conditional}
#
# # Example 2
# # For this example, we will repeat the task in the first example with an additional condition.
# # Both list and dictionary comprehensions accept if/else conditional statements.
#
words = ['data', 'science', 'machine', 'learning']#list comprehension
# # i
print([len(i) for i in words if len(i) > 5])
# # [7, 7, 8]
# #dictionary comprehension
# # i
print({i: len(i) for i in words if len(i) > 5})
# # {'science': 7, 'machine': 7, 'learning': 8}
#
# # Example 3
# # In this example, we will slightly increase the complexity of the conditional statement.
#
# # i
words_dict = {i: len(i) if len(i) > 5 else 'short' for i in words}
print(words_dict)
# # {'data': 'short', 'science': 7, 'machine': 7, 'learning': 8}

words_dict = {} # dict
for i in words:
    if len(i) > 5:
        words_dict[i] = len(i)
    else:
        words_dict[i] = 'short'
print(words_dict)

# # Example 4
# # We can iterate over two iterables in a dictionary comprehension.

words = ['data', 'science', 'machine', 'learning']
values = [5, 3, 1, 8]
# # i, j
dict_a = {i: j for i, j in zip(words, values)}
print(dict_a)
# # {'data': 5, 'science': 3, 'machine': 1, 'learning': 8}
#
# # Example 5
# # We can also put a condition on the values when iterating over a list of tuples.

words = ['data', 'science', 'machine', 'learning']
values = [5, 3, 1, 8]
# # i, j
dict_a = {i: j for i, j in zip(words, values) if j > 4}
print(dict_a)
# # {'data': 5, 'learning': 8}
#
# # Example 6
# # We can also apply transformations on key-value pairs.
#
# # i, j
dict_b = {i.upper(): j**2 for i, j in zip(words, values)}
print(dict_b)
# # {'DATA': 25, 'SCIENCE': 9, 'MACHINE': 1, 'LEARNING': 64}
#
# # Example 7
# # We can access the key-value pairs in a dictionary by using the items method.

print(dict_b.items())
# # dict_items([('DATA', 25), ('SCIENCE', 9), ('MACHINE', 1), ('LEARNING', 64)])
#
# # We can use the items of an existing dictionary as iterable in a dictionary comprehension.
# # It allows us to create dictionaries based on existing dictionaries and modify both keys and values.
#
# # i, j
dict_c = {i.lower(): j % 2 for i, j in dict_b.items()}
print(dict_c)
# # {'data': 1, 'science': 1, 'machine': 1, 'learning': 0}
#
# # Example 8
# # The enumerate function of Python can be used to create an iterable of tuples based on a list.
# # Each tuple contains the items in the list with incrementing integer values.

names = ['John', 'Jane', 'Adam', 'Eva', 'Ashley']
print(list(enumerate(names)))
# # [(0, 'John'), (1, 'Jane'), (2, 'Adam'), (3, 'Eva'), (4, 'Ashley')]
#
# # We can use the enumerate function in a dictionary comprehension.
#
# # i, j
dict_names = {i: len(j) for i,j in enumerate(names)}
print(dict_names)
# # {0: 4, 1: 4, 2: 4, 3: 3, 4: 6}
#
# # If you just want to create a dictionary based on a list of tuples without any modification on the values,
# # you do not need to use a comprehension. The dict function will do the job.

print(dict(enumerate(names)))
# # {0: 'John', 1: 'Jane', 2: 'Adam', 3: 'Eva', 4: 'Ashley'}
#
# # Example 9
# # This example contains a slightly more complicated conditionals than the previous ones.
# # Consider we have the following dictionary and list.

lst = ['data','science','artificial', 'intelligence']
dct = {'data': 5, 'science': 3, 'machine': 1, 'learning': 8}
#
# # We want to create a new dictionary using the list and dictionary defined above.
# # The keys of the new dictionary will be the elements in the list so we will iterate over the elements in list.
# # If the element is also in the dictionary, the value will be the values of that key in the dictionary.
# # Otherwise, the value will be the length of the key.
#
# #
print({i: dct[i] if i in dct else len(i) for i in lst})
# # {'artificial': 10, 'data': 5, 'intelligence': 12, 'science': 3}
#
# # Example 10
# # The keys of a dictionary must be immutable so tuples can be used as keys.
# # Dictionary comprehensions allow for generating keys of tuples by implemented nested loops.
#
a = [1,2,3,4]
b = [5,6,7]
# # i j
dct = {(i, j): i*j for i in a for j in b}
print(dct)
#
# # {(1, 5): 5,
# #  (1, 6): 6,
# #  (1, 7): 7,
# #  (2, 5): 10,
# #  (2, 6): 12,
# #  (2, 7): 14,
# #  (3, 5): 15,
# #  (3, 6): 18,
# #  (3, 7): 21,
# #  (4, 5): 20,
# #  (4, 6): 24,
# #  (4, 7): 28}
#
# # Each pair of items in the lists is a key in the dictionary. The value is the product of the items in keys.
# #
# # The equivalent for loop syntax:
#
# dct  # dict
# # i, j
for i in a:
    for j in b:
        dct[(i, j)] = i * j