# # defaultdict
# # The defaultdict is a specialized dictionary found in the collections module. (It is a subclass of the dict type).
#
# f__ c... ______ d..d..
#
# # Standard dictionaries in Python will raise an exception if we try to access a non-existent key:
#
# d _ ||
# # d['a']  # ERROR KeyError: 'a'
#
# # Now, we can certainly use the .get method:
#
# result _ d.ge.'a'
# ty.. r..
# # NoneType
#
# # And we can even specify a default value for the key if it is not present:
#
# d.ge. 'a' 0
# # 0
#
# # Often we have dictionaries where we want to return a consistent default value if the requested key does not exist.
# # Although we can do so using the .get method as above, we have to remember to use the same default value every time
# # - plus it gets a little cumbersome.
# # Let's say we want to keep track of the number of occurrences of individual characters in a string.
# # We might approach it this way:
#
# counts _
# sentence _ "able was I ere I saw elba"
#
# ___ c i_ se..
#     i_ c i_ co..
#         co.. c +_ 1
#     e___
#         co.. c _ 1
#
# print co..
# # {'a': 4, 'b': 2, 'l': 2, 'e': 4, ' ': 6, 'w': 2, 's': 2, 'I': 2, 'r': 1}
#
# # So this works, but we have that if statement - it would be nice to simplify our code somewhat:
#
# counts _
# ___ c i_ se..
#     co.. c _ co__.ge. c 0 + 1
#
# print co..
# # {'a': 4, 'b': 2, 'l': 2, 'e': 4, ' ': 6, 'w': 2, 's': 2, 'I': 2, 'r': 1}
#
# # So, that works well and is much cleaner. But if we have to specify that default value (0 in this case) many times
# # in our code when working with the same dictionary, we have to remember what the default needs to be each time.
# # Instead, we could use a defaultdict. In a defaultdict we specify what the default value is for a missing key -
# # more precisely, we specify a default factory method that is called:
#
# counts _ d..d.. l______ 0
# ___ c i_ se..
#     co.. c +_ 1
#
# print co..
# # defaultdict(<function __main__.<lambda>()>,
# #             {'a': 4,
# #              'b': 2,
# #              'l': 2,
# #              'e': 4,
# #              ' ': 6,
# #              'w': 2,
# #              's': 2,
# #              'I': 2,
# #              'r': 1})
#
# # As you can see that simplified our code quite a bit, but the result is not quite a dictionary - it is a defaultdict.
# # However, it inherits from dict so all the dictionary methods we have grown to know and love are still available
# # because defaultdict is a dict:
#
# print isi__ co.. d..d..
# # True
#
# print isi__ co.. di..
# # True
#
# # And counts behaves like a regular dictionary too:
#
# print co__.it..
# # dict_items([('a', 4), ('b', 2), ('l', 2), ('e', 4), (' ', 6), ('w', 2), ('s', 2), ('I', 2), ('r', 1)])
#
# print(co.. 'a'
# # 4
#
# # The main difference is when we request a non-existent key:
#
# print co.. 'python'
# # 0
#
# # We get the default value back - not only that, but it actually created that key as well:
#
# print co..
# #
# # defaultdict(<function __main__.<lambda>()>,
# #             {'a': 4,
# #              'b': 2,
# #              'l': 2,
# #              'e': 4,
# #              ' ': 6,
# #              'w': 2,
# #              's': 2,
# #              'I': 2,
# #              'r': 1,
# #              'python': 0})
# #
# # So this is a bit different from using .get.
# # And of course we can manipulate our dictionary just like a standard dictionary:
#
# co.. 'hello' _ 'world'
# print co..
# # defaultdict(<function __main__.<lambda>()>,
# #             {'a': 4,
# #              'b': 2,
# #              'l': 2,
# #              'e': 4,
# #              ' ': 6,
# #              'w': 2,
# #              's': 2,
# #              'I': 2,
# #              'r': 1,
# #              'python': 0,
# #              'hello': 'world'})
#
#
# del co.. 'hello'
# co..
#
# # defaultdict(<function __main__.<lambda>()>,
# #             {'a': 4,
# #              'b': 2,
# #              'l': 2,
# #              'e': 4,
# #              ' ': 6,
# #              'w': 2,
# #              's': 2,
# #              'I': 2,
# #              'r': 1,
# #              'python': 0})
#
# # Very often you will see what looks like a type specified as the default factory - but keep in mind that it is in
# # fact the corresponding functions (constructors) that are actually being specified.
#
# print in.
# # 0
#
# print bo.
# # False
#
# print st.
# # ''
#
# print li..
# # []
#
# d _ d..d.. in.
# print d 'a'
# # 0
#
# d _ d..d.. bo..
# print d 'a'
# # False
#
# d _ d..d.. st.
# print d 'a'
# # ''
#
# d _ d..d.. li..
# print d 'a'
# # []
#
# # Note that this no different than writing:
#
# d _ d..d.. l____ li..
# print d 'a'
# # []