# # The OrderedDict
# # OrderedDict is a dictionary where keys maintain the order in which they are inserted, which means if you change
# # the value of a key later, it will not change the position of the key.
# # ____ OrderedDict
# # To use OrderedDict you have to ____ it from the collections module.
#
# f.. c.. ____ O..
# f.. c.. ____ C..
#
# # Create a OrderedDict
# # You can create an OrderedDict object with OrderedDict() constructor. In the following code, You create an
# # OrderedDict without any arguments. After that some items are inserted into it.
#
# od = O..
# od 'a'  1
# od 'b'  2
# od 'c'  3
# print(od)
#
# # Output:
# # OrderedDict([('a', 1), ('b', 2), ('c', 3)])
#
# # You can access each element using a loop as well. Take a look at the following code:
#
# ___ key value i_ o_.it..
#     print k.. v..
#
# # Output:
# #
# # a 1
# # b 2
# # c 3
#
# # Following example is an interesting use case of OrderedDict with Counter. Here, we create a Counter from a list
# # and insert element to an OrderedDict based on their count.
# # Most frequently occurring letter will be inserted as the first key and the least frequently occurring letter will
# # be inserted as the last key.
#
# list _ ["a","c","c","a","b","a","a","b","c"]
# cnt _ C.. li..
# od _ O.. c__.m.._c..
# ___ key value i_ o_.it..
#     print k.. v..
#
# # Output:
# #
# # a 4
# # c 3
# # b 2
