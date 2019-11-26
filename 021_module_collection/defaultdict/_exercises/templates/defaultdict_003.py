# # The defaultdict
# # The defaultdict works exactly like a python dictionary, except for it does not throw KeyError when you try to access
# # a non-existent key.
# # Instead, it initializes the key with the element of the data type that you pass as an argument at the creation of
# # defaultdict. The data type is called default_factory.
# # Import defaultdict
# # First, you have to import defaultdict from collections module before using it:
#
# f__ c.. _______ d..d..
#
# # Create a defaultdict
# # You can create a defaultdict with the defaultdict() constructor. You have to specify a data type as an argument.
# # Check the following code:
#
# nums _ d..d.. in.
# n... 'one' _ 1
# n... 'two' _ 2
# print n..'three'
#
# # Output:
# # 0
#
# # In this example, int is passed as the default_factory. Notice that you only pass int, not int(). Next, the values are
# # defined for the two keys, namely, 'one' and 'two', but in the next line we try to access a key that has not been
# # defined yet.
# # In a normal dictionary, this will force a KeyError. But defaultdict initialize the new key with default_factory's
# # default value which is 0 for int. Hence, when the program is executed, and 0 will be printed. This particular feature
# # of initializing non-existent keys can be exploited in various situations.
# # For example, let's say you want the count of each name in a list of names given as "Mike, John, Mike, Anna, Mike,
# # John, John, Mike, Mike, Britney, Smith, Anna, Smith".
#
# f_ c... ______ d..d..
#
# count _ d..d.. in.
# names_list _ "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".sp..
# ___ names i_ n.._l..
#     c.. n.. +_1
# print c..
#
# # Output:
# # defaultdict(<class 'int'>, {'Mike': 5, 'Britney': 1, 'John': 3, 'Smith': 2, 'Anna': 2})
#
# # First, we create a defaultdict with int as default_factory. The names_list includes a set of names which repeat
# # several times. The split() function returns a list from the given string. It breaks the string whenever
# # a white-space is encountered and returns words as elements of the list. In the loop, each item in the list is
# # added to the defaultdict named as count and initialized to 0 based on default_factory. If the same element is
# # encountered again, as loop continues, count of that element will be incremented.

