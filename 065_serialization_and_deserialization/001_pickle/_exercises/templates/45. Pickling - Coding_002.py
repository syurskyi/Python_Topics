# # n this part of the course I am only going to discuss pickling basic data types such as numbers, strings, tuples,
# # lists, sets and dictionaries.
# # In general tuples, lists, sets and dictionaries are all picklable as long as their elements are themselves picklable.
# # Let's start by serializing some simple data types, such as strings and numbers.
# # Instead of serializing to a file, I will store the resulting pickle data in a variable, so we can easily
# # inspect it and unpickle it:
#
# ______ p___
#
# ser _ p___.d... Python Pickled Peppers
#
# print ?
# # b'\x80\x03X\x16\x00\x00\x00Python Pickled Peppersq\x00.'
# # ######################################################################################################################
#
# print('#' * 52 + ' We can deserialize the data this way:  ')
#
# deser _ p___.l... s..
# print ?
# # 'Python Pickled Peppers'
# # ######################################################################################################################
#
# print('#' * 52 + ' We can do the same thing with numerics ')
# ser _ p___.d... 3.14
# print(ser)
# deser _ p___.l... s..
# print ?
# # 3.14
# # ######################################################################################################################
#
# print('#' * 52 + ' We can do the same with lists and tuples:  ')
# d _ [10, 20, ('a', 'b', 30)]
# ser _ p___.d...(d)
# print ?
# # b'\x80\x03]q\x00(K\nK\x14X\x01\x00\x00\x00aq\x01X\x01\x00\x00\x00bq\x02K\x1e\x87q\x03e.'
# # ######################################################################################################################
#
# deser _ p___.l... s..
# print ?
# # [10, 20, ('a', 'b', 30)]
# # ######################################################################################################################
#
# print('#' * 52 + '  Note that the original and the deserialized objects are equal, but not identical:')
# print d i_ d... d __ d..
# # (False, True)
# # ######################################################################################################################
#
# print('#' * 52 + '  This works the same way with sets too:')
# s _  'a', 'b', 'x', 10
# print s
# # {10, 'a', 'b', 'x'}
# # ######################################################################################################################
#
# ser _ p___.d... s
# print ?
# # b'\x80\x03cbuiltins\nset\nq\x00]q\x01(X\x01\x00\x00\x00aq\x02K\nX\x01\x00\x00\x00xq\x03X\x01\x00\x00\x00bq\x04e\x85q\x05Rq\x06.'
# # ######################################################################################################################
#
# deser _ p___.l... s..
# print ?
# # {'a', 10, 'b', 'x'}
# # ######################################################################################################################
#
# print('#' * 52 + '  And finally, we can pickle dictionaries as well:')
# d _ 'b' 1, 'a' 2, 'c' |'x' 10, 'y' 20
# print ?
# # {'b': 1, 'a': 2, 'c': {'x': 10, 'y': 20}}
# # ######################################################################################################################
#
# ser _ p___.d... d
# print ?
# # b'\x80\x03}q\x00(X\x01\x00\x00\x00bq\x01K\x01X\x01\x00\x00\x00aq\x02K\x02X\x01\x00\x00\x00cq\x03}q\x04(X\x01\x00\x00\x00xq\x05K\nX\x01\x00\x00\x00yq\x06K\x14uu.'
# # ######################################################################################################################
#
# deser _ p___.l... s..
# print ?
# # {'b': 1, 'a': 2, 'c': {'x': 10, 'y': 20}}
# # ######################################################################################################################
#
# print d __ d..
# # True
#
# print('#' * 52 + '  What happens if we pickle a dictionary that has two of its values set to another dictionary?')
# d1 _  'a' 10, 'b' 20
# d2 _ 'x' 100, 'y' d1, 'z' d1
# print _2
# # {'x': 100, 'y': {'a': 10, 'b': 20}, 'z': {'a': 10, 'b': 20}}
# # ######################################################################################################################
#
# ser _ p___.d... _2
# d3 _ p___.l... s..
# print _3
# # {'x': 100, 'y': {'a': 10, 'b': 20}, 'z': {'a': 10, 'b': 20}}
# # ######################################################################################################################
#
# print('#' * 52 + '  That seems to work... Is that sub-dictionary still the same as the original one?')
# print d3|'y' __ d2|'y'
# # True
# # ######################################################################################################################
#
# print d3|'y' i_ d2|'y'
# # False
# # ######################################################################################################################
#
# print('#' * 52 + '  But consider the original dictionary d2: both the x and y keys referenced the same dictionary d1:')
# print d2|'y' i_ d2|'z'
# # True
# # ######################################################################################################################
#
# print('#' * 52 + '  How did this work with our deserialized dictionary?')
# print d3|'y']__ d3|'z'
# # True
# # ######################################################################################################################
#
# # As you can see the relative shared object is maintained.
# # As you can see our dictionary d looks like the earlier one. So, when Python serializes the dictionary,
# # it behaves very similarly to serializing a deep copy of the dictionary. The same thing happens with other collections
# # types such as lists, sets, and tuples.
# # What this means though is that you have to be very careful how you use serialization and deserialization.
# # Consider this piece of code:
#
# print('#' * 52 + '  As you can see the relative shared object is maintained.')
# print('#' * 52 + '  ')
#
# print('#' * 52 + '  What this means though is that you have to be very careful how you use serialization and '
#                  'deserialization.')
# d1 _  'a' 1, 'b' 2
# d2 _  'x' 10, 'y' d1
# print(d1)
# print(d2)
# d1['c'] _ 3
# print(d1)
# print(d2)
# # {'a': 1, 'b': 2}
# # {'x': 10, 'y': {'a': 1, 'b': 2}}
# # {'a': 1, 'b': 2, 'c': 3}
# # {'x': 10, 'y': {'a': 1, 'b': 2, 'c': 3}}
# # ######################################################################################################################
#
# print('#' * 52 + '  Now suppose we pickle our dictionaries to restore those values the next time around, '
#                  '  but use the same code, expecting the same result:')
#
# d1 _  'a' 1, 'b' 2
# d2 _  'x' 10, 'y' _1
# d1_ser _ p___.d... _1
# d2_ser _ p___.d... _2
#
# # simulate exiting the program, or maybe just restarting the notebook
# de. _1
# de. _2
#
# # load the data back up
# d1 _ p___.l... _1_s.
# d2 _ p___.l... _2_s.
#
# # and continue processing as before
# print(d1)
# print(d2)
# d1['c'] _ 3
# print(d1)
# print(d2)
# # {'a': 1, 'b': 2}
# # {'x': 10, 'y': {'a': 1, 'b': 2}}
# # {'a': 1, 'b': 2, 'c': 3}
# # {'x': 10, 'y': {'a': 1, 'b': 2}}
# # ######################################################################################################################
#
# # So just remember that as soon as you pickle a dictionary, whatever object references it had to another object is
# # essentially lost - just as if you had done a deep copy first. It's a subtle point, but one that can easily lead
# # to bugs if we're not careful.
# # However, the pickle module is relatively intelligent and will not re-pickle an object it has already pickled -
# # which means that relative references are preserved.
# # Let's see an example of what I mean by this:
#
# print('#' * 52 + '  So just remember that as soon as you pickle a dictionary, '
#                  '  whatever object references it had to another object is essentially lost - '
#                  '  just as if you had done a deep copy first. '
#                  '  It is a subtle point, but one that can easily lead to bugs if we are not careful.')
# print('#' * 52 + '  ')
# print('#' * 52 + '  However, the pickle module is relatively intelligent and will not re-pickle an object it has'
#                  '  already pickled - which means that relative references are preserved.')
#
#
# c_ Person
#     ___ __i__ ____ name age
#         ____.n.. _ n..
#         ____.a.. _ a..
#
#     ___ __eq__ ____ other
#         r_ ____.n.. __ o__.n.. an. ____.a.. __ o___.a..
#
#     ___ __re__ self
#         r_ _*P... n.._ |____.name| a.._ |____.a..|*
#
#
# john _ P.. 'John Cleese' 79
# eric _ P.. 'Eric Idle' 75
# michael _ P.. 'Michael Palin' 75
#
# parrot_sketch _
#     "title": "Parrot Sketch",
#     "actors": [john, michael]
#
#
# ministry_sketch _
#     "title": "Ministry of Silly Walks",
#     "actors": [john, michael]
#
#
# joke_sketch _
#     "title": "Funniest Joke in the World",
#     "actors": [eric, michael]
#
#
# fan_favorites _
#     "user_1": [parrot_sketch, joke_sketch],
#     "user_2": [parrot_sketch, ministry_sketch]
#
#
#
# f... pp.. ______ pp...
# pprint f.._f..
# # {'user_1': [{'actors': [Person(name_John Cleese, age_79),
# #                         Person(name_Michael Palin, age_75)],
# #              'title': 'Parrot Sketch'},
# #             {'actors': [Person(name_Eric Idle, age_75),
# #                         Person(name_Michael Palin, age_75)],
# #              'title': 'Funniest Joke in the World'}],
# #  'user_2': [{'actors': [Person(name_John Cleese, age_79),
# #                         Person(name_Michael Palin, age_75)],
# #              'title': 'Parrot Sketch'},
# #             {'actors': [Person(name_John Cleese, age_79),
# #                         Person(name_Michael Palin, age_75)],
# #              'title': 'Ministry of Silly Walks'}]}
# # ######################################################################################################################
#
# print('#' * 52 + '  As you can see we have some shared references, for example:')
# print f.._f.. 'user_1'| 0 i_ f.._f.. 'user_2'| 0
# # True
# # ######################################################################################################################
#
# print('#' * 52 + '  Lets store the id of the parrot_sketch for later reference:')
# parrot_id_original _ i. p.._s..
#
# print('#' * 52 + '  Now lets pickle and unpickle this object:')
# ser _ p___.d... f.._f..
# new_fan_favorites _ p___.l... ?
# print(f.._f. __ n.._f.._f..
# # True
# # ######################################################################################################################
#
# print('#' * 52 + '  And lets look at the id of the parrot_sketch object in our new dictionary'
#                  '  compared to the original one:')
# print i_ f.._f.. 'user_1'| 0 i_ n._f._f. 'user_1'| 0
# # (4554999848, 4555001288)
# # ######################################################################################################################
#
# print('#' * 52 + '  As expected the ids differ - but the objects are equal:')
# print f.._f. 'user_1'| 0 __ n.._f.._f..'user_1'| 0
# # True
# # ######################################################################################################################
#
# print('#' * 52 + '  But now lets look at the parrot sketch that is in both user_1 and user_2 - '
#                  '  remember that originally the objects were identical (is):')
# print f.._f.. 'user_1' 0 i_ f._f..'user_2' |0
# # True
# # ######################################################################################################################
#
# print('#' * 52 + '  and with our new object:')
# print n.._f.._f..'user_1' 0 i_ n.._f.._f..'user_2' 0
# # True
# # ######################################################################################################################
#
# print('#' * 52 + '  As you can see the relative relationship between objects that were pickled is preserved.')
#
# # And that's all I'm really going to say about pickling objects in Python. Instead I'm going to focus more on what
# # is probably a more relevant topic to many of you - JSON serialization/deserialization.
