# ____ c.. _____ O__
#
# numbers = O__()
#
# ? ["one"] = 1
# ? ["two"] = 2
# ? ["three"] = 3
#
# ?
# # OrderedDict([('one', 1), ('two', 2), ('three', 3)])
#
# ____ c.. _____ O__
#
# numbers = O__ "one", 1), ("two", 2), ("three", 3    # l__t
# ?
# # OrderedDict([('one', 1), ('two', 2), ('three', 3)])
#
# letters = O__ "a", 1), ("b", 2), ("c", 3   # dict
# letters
# # OrderedDict([('c', 3), ('a', 1), ('b', 2)])
#
# ____ c.. _____ O__
#
# numbers = O__ "one": 1, "two": 2, "three": 3
# ?
# # OrderedDict([('one', 1), ('two', 2), ('three', 3)])
#
# ____ c.. _____ O__
#
# numbers = O__ "one": 1, "two": 2, "three": 3
# numbers
# # OrderedDict([('one', 1), ('three', 3), ('two', 2)])
#
# ____ c.. _____ O__
#
# numbers = O__(one=1, two=2, three=3)
# numbers
# # OrderedDict([('one', 1), ('two', 2), ('three', 3)])
#
#
# ____ c.. _____ O__
#
# keys = ["one", "two", "three"]
# O__.f.. ? 0
# # OrderedDict([('one', 0), ('two', 0), ('three', 0)])
#
#
# # Managing Items in an OrderedDict
#
# ____ c.. _____ O__
#
# numbers = O__(one=1, two=2, three=3)
# ?
# # OrderedDict([('one', 1), ('two', 2), ('three', 3)])
#
# ? "four" = 4
# ?
# # OrderedDict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
#
# ____ c.. _____ O__
# numbers = O__ one=1, two=2, three=3
#
# d.. ? "one"
# ?
# # OrderedDict([('two', 2), ('three', 3)])
#
# ? "one" = 1
# ?
# # OrderedDict([('two', 2), ('three', 3), ('one', 1)])
#
# ____ c.. _____ O__
# numbers = O__ one=1, two=2, three=3
#
# ? "one" = 1.0
# ?
# # OrderedDict([('one', 1.0), ('two', 2), ('three', 3)])
#
# ?.u.. two=2.0
# ?
# # OrderedDict([('one', 1.0), ('two', 2.0), ('three', 3)])
#
# # Iterating Over an OrderedDict
#
# ____ c.. _____ O__
# numbers = O__(one=1, two=2, three=3)
#
# # Iterate over the keys directly
# ___ key __ ?
#     print ? "->" ? ?
#
# # one -> 1
# # two -> 2
# # three -> 3
#
# # Iterate over the items using .items()
# ___ key value __ ?.i..
#      print ? "->" ?
#
# # one -> 1
# # two -> 2
# # three -> 3
#
# # Iterate over the keys using .keys()
# ___ key __ ?.k..
#      print ? "->" ? ?
#
# # one -> 1
# # two -> 2
# # three -> 3
#
# # Iterate over the values using .values()
# ___ value __ ?.v..
#      print ?
#
# # 1
# # 2
# # 3
#
# # Iterating in Reversed Order With reversed()
#
# ____ c.. _____ O__
# numbers  O__(one=1, two=2, three=3)
#
# # Iterate over the keys directly in reverse order
# ___ key __ r.. ?
#      print ? "->" ? ?
#
# # three -> 3
# # two -> 2
# # one -> 1
#
# # Iterate over the items in reverse order
# ___ key, value __ r.. ?.i..
#      print ? "->" ?
#
# # three -> 3
# # two -> 2
# # one -> 1
#
# # Iterate over the keys in reverse order
# ___ key __ r.. ?.k..
#      print ? "->" ? ?
#
# # three -> 3
# # two -> 2
# # one -> 1
#
# # Iterate over the values in reverse order
# ___ value __ r.. ?.v..
#      print ?
#
# # 3
# # 2
# # 1
#
# # Exploring Unique Features of Python’s
#
# ____ c.. _____ O__
# numbers = O__(one=1, two=2, three=3)
# ?
# # OrderedDict([('one', 1), ('two', 2), ('three', 3)])
#
# ?.m.. "one"
# ?
# # OrderedDict([('two', 2), ('three', 3), ('one', 1)])
#
# ?.m.. "one" l.._F..
# ?
# # OrderedDict([('one', 1), ('two', 2), ('three', 3)])
#
# ____ c.. _____ O__
# letters = O__(b=2, d=4, a=1, c=3)
#
# ___ key __ s.. ?
#      ?.m.. ?
#
# ?
# # OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
#
# ____ c.. _____ O__
# letters = O__(a=4, b=3, d=1, c=2)
#
# ___ key, _ __ s.. ?.i.. k.._l.. item ? 1
#      ?.m.. ?
#
# ?
# # OrderedDict([('d', 1), ('c', 2), ('b', 3), ('a', 4)])
#
#
# # Removing Items With .popitem()
#
# ____ c.. _____ O__
# numbers = O__(one=1, two=2, three=3)
#
# ?.p..
# # ('three', 3)
# ?.p..
# # ('two', 2)
# ?.p..
# # ('one', 1)
# ?.p..
# # Traceback (most recent call last):
# #   File "<input>", line 1, in <module>
# #     numbers.popitem()
# # KeyError: 'dictionary __ empty'
#
# ____ c.. _____ O__
# numbers = O__(one=1, two=2, three=3)
#
# ?.p.. l.._F..
# # ('one', 1)
# ?.p.. l.._F..
# # ('two', 2)
# ?.p.. l.._F..
# # ('three', 3)
# ?.p.. l.._F..
# # Traceback (most recent call last):
# #   File "<input>", line 1, in <module>
# #     numbers.popitem(last=False)
# # KeyError: 'dictionary __ empty'
#
# # Testing for Equality Between Dictionaries
#
# ____ c.. _____ O__
# letters_0 = O__(a=1, b=2, c=3, d=4)
# letters_1 = O__(b=2, a=1, c=3, d=4)
# letters_2 = O__(a=1, b=2, c=3, d=4)
#
# letters_0 == letters_1
# # False
#
# letters_0 == letters_2
# # True
#
# letters_0 = dict(a=1, b=2, c=3, d=4)
# letters_1 = dict(b=2, a=1, c=3, d=4)
# letters_2 = dict(a=1, b=2, c=3, d=4)
#
# letters_0 == letters_1
# # True
#
# letters_0 == letters_2
# # True
#
# letters_0 == letters_1 == letters_2
# # True
#
# ____ c.. _____ O__
# letters_0 = O__(a=1, b=2, c=3, d=4)
# letters_1 = dict(b=2, a=1, c=3, d=4)
#
# letters_0 == letters_1
# # True
#
#
# # Appending New Attributes to a Dictionary Instance
#
# ____ c.. _____ O__
# letters = O__(b=2, d=4, a=1, c=3)
# ?. -d
# # {}
#
# letters1 = dict(b=2, d=4, a=1, c=3)
# ?. -d
# # Traceback (most recent call last):
# #   File "<input>", line 1, in <module>
# #     letters1.__dict__
# # AttributeError: 'dict' object has no attribute '__dict__'
#
# ____ c.. _____ O__
# letters = O__(b=2, d=4, a=1, c=3)
#
# ?.s.. = l__ s.. ?.k..
# v.. ?
# # {'sorted_keys': <function <lambda> at 0x7fa1e2fe9160>}
#
# ?.s..
# # ['a', 'b', 'c', 'd']
#
# ? "e" = 5
# ?.s..
# # ['a', 'b', 'c', 'd', 'e']
#
# ___ key __ ?.s..
#      print ? "->" ? ?
#
# # a -> 1
# # b -> 2
# # c -> 3
# # d -> 4
# # e -> 5
#
# letters
# # OrderedDict([('b', 2), ('d', 4), ('a', 1), ('c', 3), ('e', 5)])
#
# # Merging and Updating Dictionaries With Operators
#
# ____ c.. _____ O__
#
# physic__ts = O__(newton="1642-1726", einstein="1879-1955")
# biolog__ts = O__(darwin="1809-1882", mendel="1822-1884")
#
# scient__ts = physic__ts | biolog__ts
# ?
# O__([
#    ('newton', '1642-1726'),
#    ('einstein', '1879-1955'),
#    ('darwin', '1809-1882'),
#    ('mendel', '1822-1884')
# ])
#
# physic__ts = O__(newton="1642-1726", einstein="1879-1955")
#
# physic__ts_1 = O__(newton="1642-1726/1727", hawking="1942-2018")
# physic__ts |= physic__ts_1
# ?
# O__([
#     ('newton', '1642-1726/1727'),
#     ('einstein', '1879-1955'),
#     ('hawking', '1942-2018')
# ])
#
#
# # Considering Performance
#
# # time_testing.py
#
# ____ c.. _____ O__
# ____ t. _____ p..
#
# ___ average_time dictionary
#     time_measurements  # l__t
#     ___ _ __ r.. 1_000_000
#         start  p..
#         ? key = value
#         key __ ?
#         m__sing_key __ ?
#         ? ?
#         d.. ? ?
#         end  p..
#         ?.a.. ? - ?
#     r_ s.. ? / l.. ? * int(1e9)
#
# ordereddict_time = a.. (O__.f.. r.. 1000
# dict_time = a.. d__.f.. r.. 1000
# gain = ? / ?
#
# print _*OrderedDict: ?:.2f ns
# print _*dict:        ?:.2f ns ?:.2f x faster)
#
# _____ ___
# ____ c.. _____ O__
#
# ordereddict_memory = ___.g.. O__.f.. r.. 1000
# dict_memory = ___.g.. d__.f.. r.. 1000
# gain = 100 - ? / ? * 100
#
# print _*OrderedDict: ? bytes
# # OrderedDict: 85408 bytes
#
# print _*dict:        ? bytes ( ?:.2f}% lower)
# # dict:        36960 bytes (56.73% lower)
#
# # Building a Dictionary-Based Queue
#
# # queue.py
#
# ____ c.. _____ O__
#
# c_ Queue
#     ___ -  initial_data_N.. / $$
#         data = O__
#         __ ? __ n.. N..
#             ?.u.. ?
#         __ k..
#             ?.u.. ?
#
#     ___ enqueue item
#         key, value _ ?
#         __ ? __ d..
#             d__.m.. ?
#         d.. ? _ ?
#
#     ___ dequeue
#         ___
#             r_ d__.p.. l.._F..
#         e.. K..
#             print("Empty queue")
#
#     ___ -l
#         r_ l.. d..
#
#     ___ -r
#         r_ _*Queue( d__.i..
#
# ____ q.. _____ Q..
#
# # Create an empty queue
# empty_queue = ?
# ?
# Queue(odict_items([]))
#
# # Create a queue with initial data
# numbers_queue = Queue([("one", 1), ("two", 2)])
# numbers_queue
# # Queue(odict_items([('one', 1), ('two', 2)]))
#
# # Create a queue with keyword arguments
# letters_queue = Queue(a=1, b=2, c=3)
# letters_queue
# # Queue(odict_items([('a', 1), ('b', 2), ('c', 3)]))
#
# # Add items
# numbers_queue.enqueue(("three", 3))
# numbers_queue
# # Queue(odict_items([('one', 1), ('two', 2), ('three', 3)]))
#
# # Remove items
# numbers_queue.dequeue()
# # ('one', 1)
# numbers_queue.dequeue()
# # ('two', 2)
# numbers_queue.dequeue()
# # ('three', 3)
# numbers_queue.dequeue()
# # Empty queue
#
#
