# # Here let us use a list of numbers and create a dictionary with string value of the number as key and
# # the number as values.
# # dict comprehension to create dict with numbers as values
# # i
# print st_ ? ? ___ ? __ 1,2,3,4,5
# # {'1': 1, '3': 3, '2': 2, '5': 5, '4': 4}
#
# # Let us say, we have a list of fruits and we can use dict comprehension to create a dictionary with fruits,
# # the list elements as the keys and the length of each string as the values.
# # create list of fruits
# fruits = ['apple', 'mango', 'banana','cherry']
# # dict comprehension to create dict with fruit name as keys
# # f
# print ? le_ ? ___ ? __ ?
# # {'cherry': 6, 'mango': 5, 'apple': 5, 'banana': 6}
#
# # Let us create a dictionary with dict comprehension such that elements of the list as the keys and the elements
# # with first letter capitalized as the values.
# # f
# print ? ?.ca.. ___ f __ ?
# # {'cherry': 'Cherry', 'mango': 'Mango', 'apple': 'Apple', 'banana': 'Banana'}
#
# # Let us use enumerate function in dictionary comprehension.
# # If you have not used enumerate: enumerate can take any thing iterable as input and returns element and its index.
# # dict comprehension example using enumerate function
# # f i
# print ? ? ___ ? ? __ e.. ?
# # {'cherry': 3, 'mango': 1, 'apple': 0, 'banana': 2}
#
# # Another use of dict comprehension is to reverse key:value in an existing dictionary. Sometimes you may want
# # to create new dictionary from an existing directory, such that the role of key:value pair in the first dictionary
# # is reversed in the new dictionary. We can use Dict Comprehension and flip the element to index dictionary
# # to index to element dictionary.
# # dict comprehension example to reverse key:value pair in a dictionary
# # f, i
# f_dict _ ? ? ___ ? ? __ e.. ?
# print ?
# # {'apple': 0, 'banana': 2, 'cherry': 3, 'mango': 1}
# # dict comprehension to reverse key:value pair in a dictionary
# # v, k
# print ? ? ___ ? ? __ ?.i..
# # {0: 'apple', 1: 'mango', 2: 'banana', 3: 'cherry'}
#
# # How To Delete Selected Keys from Dictionary using Dict Comprehension?
# #
# # Let us say you have dictionary and want to create a new dictionary by removing certain key-value pair.
# # We can use Dict Comprehension to remove selected key-value pairs from a dictionary and create a new dictionary.
# fruits = ['apple', 'mango', 'banana','cherry']
# # f
# f_d1 = ? ?.ca.. ___ ? __ ?
# print ?
#
# # keys to be removed
# remove_this = {'apple','cherry'}
# # dict comprehension example to delete key:value pairs in a dictionary
# #key
# print ? ? ? ___ ? __ ?.k.. -
# # {'banana': 'Banana', 'mango': 'Mango'}