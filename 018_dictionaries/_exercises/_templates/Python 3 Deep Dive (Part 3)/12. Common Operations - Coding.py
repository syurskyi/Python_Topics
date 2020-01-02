# print('#' * 52 + ' ### Common Operations  ')
#
# d = di.. z.. 'abc ra.. 1 4
# print(d)
# print(len(d))
# print(d['a'])
# # print(d['python']) # KeyError: 'python'
#
# print('#' * 52 + ' Sometimes though, we do not want an exception to happen, and we want to provide some default'
#                  ' value instead. We could certainly catch the exception, but thats clunky. Instead we can use the'
#                  ' `get` instance method: ')
#
# d.ge. 'a
# result = ?.g.. python
# print ?
#
# print('#' * 52 + ' As you can see, we do not get an exception, we simply get `None` back. We can actually specify '
#                  ' the default to use when the key is not found: ')
#
# print ?.g.. 'python', 0
#
# print('#' * 52 + ' count letters ')
#
# text = 'Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam' \
#        ' rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, ' \
#        'explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur' \
#        ' magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum,' \
#        ' quia dolor sit amet consectetur adipisci[ng] velit, sed quia non-numquam [do] eius modi tempora inci[di]dunt,' \
#        ' ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem' \
#        ' ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure' \
#        ' reprehenderit, qui __ ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem' \
#        ' eum fugiat, quo voluptas nulla pariatur?'
# counts = di..
# ___ c __ t..
#     ? ? _ ?.ge. ? 0) + 1
# print ?
#
# print('#' * 52 + ' We can refine this a bit - first we ll ignore spaces, then we ll want to consider lowercase and '
#                  ' uppercase characters as the same:  ')
#
# counts _ di..
# ___ c __ text
#     key _ ?.lo__.st__
#     i_ ?
#         ? ? _ ?.ge. ? 0 + 1
# print ?
#
# print('#' * 52 + ' #### Membership Tests  ')
# print('#' * 52 + ' We can use the `__` and `not __` operators to test the presence of a **key** __ a dictionary:  ')
#
# d = di..(a=1, b=2, c=3)
# print('a' __ ?)
# print('z' __ ?)
# print('z' ___ __ ?)
#
# print('#' * 52 + ' #### Removing elements from a dictionary  ')
#
# d = di...f_k_ 'abcd', 0
# print?
#
# print('#' * 52 + ' We can remove a key this way:  ')
#
# del d['a']
# print(d)
#
# print('#' * 52 + ' If the key is not present, we will get a `KeyError` exception: ')
#
# # del d['z'] KeyError: 'z'
#
# result = ?.p.. 'b'
# print ?
#
# print('#' * 52 + ' So we still get a `KeyError` exception! To do this, we need to specify a **default** value'
#                  ' to use if the key is not found: ')
#
# result = ?.p.. 'z', 'Not found!'
# print ?
#
# print('#' * 52 + '  ')
#
# d = {'a': 10, 'b': 20, 'c': 30}
# print ?.p_i_
# print ?.p_i_
# print ?.p_i_
# # print(d.popitem()) #  KeyError: 'popitem(): dictionary is empty'
#
# print('#' * 52 + ' #### Inserting keys with a default  ')
# d =  'a' 1 'b' 2 'c' 3
# i_ 'z' n.. i.. d
#     ? 'z' _ 0
#
# print ?
#
# print('#' * 52 + ' We could write a simple utility function to do this for us, and r_ the value of the item as well'
#                  ' while were at it: ')
#
# ___ insert_if_not_present d, key, value
#     i_ k.. n.. i. d
#         ? k.. _ v..
#         r_ v..
#     e___
#         r_  ? k..
#
# print(d)
# result = i.. d 'a', 0
# print r.., d
#
# result = i.. d, 'y', 10)
# print(r... d
#
# print('#' * 52 + ' But instead, we can simply use the `s_d_` instance method, which will do the work we just did')
#
# d _ a 1 b 2 c 3
# result = ?.s_d_ a 0
# print ?
# print d
#
# result = ?.s_d_ z 100
# print ?
# print d
#
# print('#' * 52 + '  ')
#
# text = 'Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem' \
#        ' aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo.' \
#        ' Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni' \
#        ' dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor' \
#        ' sit amet consectetur adipisci[ng] velit, sed quia non-numquam [do] eius modi tempora inci[di]dunt, ut labore' \
#        ' et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam' \
#        ' corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure' \
#        ' reprehenderit, qui __ ea voluptate velit esse, quam nihil molestiae consequatur, vel illum,' \
#        'qui dolorem eum fugiat, quo voluptas nulla pariatur?'
# counts = di..
# ___ c __ t..
#     key = ?.lo__.st..
#     i_ ?
#         c..  k.. _ c__.g.. k.. 0| + 1
# print ?
# _______ str....
# print(str___.a.._l..
# print(str___.a.._u..
#
# print('#' * 52 + ' Heres one approach we might take:  ')
#
# categories _    # dict
# ___ c __ text
#     i_ c !_ ' '
#         i_ c i_ str___.a_l.
#             key = 'lower'
#         e__ ? __ str__.a_u..
#             k.. _ 'upper'
#         e__
#             key _ 'other'
#         i_ k.. n.. i. ca..
#             ca.. k.. _ s..  # set we'll insert the value into
#
#         c.. k__.a.. ?
# ___ cat __ ?
#     print _' | cat ', ''.j.. ca.. c..
#
# print('#' * 52 + '  We can simplify this a bit using `s_d_`: ')
#
# categories _
# ___ c __ text
#     i_ c !_ ' '
#         i_ ? __ str__.a_l_
#             key _ 'lower'
#         e____ ? __ str__.a_u_
#             key _ 'upper'
#         e___
#             key _ 'other'
#         c___.s_d_ k.. s.. .a.. ?
#
# ___ cat __ c...
#     print _* cat|:' ''.j.. ca.. c..
#
#
# print('#' * 52 + '  Just to clean things up a but more, lets create a small utility function that will r_'
#                  ' the category key: ')
#
# ___ cat_key c
#     i_ c __ ' '
#         r_ N..
#     e___ c __ str__.a_l_
#         r_ 'lower'
#     e___ c __ str__.a_u_:
#         r_ 'upper'
#     el__
#         r_ 'other'
#
# categories
# ___ c __ text
#     key _ cat_key ?
#     i_ ?
#         ca__.s_d_ k.. se. .ad. ?
#
# ___ cat __ categories
#     print _* ?:', ''.j.. ca.. c..
#
#
# print('#' * 52 + ' If you are not a fan of using `if...elif...` __ the `cat_key` function we could do it this way'
#                  ' as well: ')
#
# ___ cat_key c
#     categories _ {' ': N..
#                  str__.a_l_: 'lower',
#                  str__.a_u_: 'upper'}
#     ___ key __ c...
#         i_ c __ k..
#             r_ ca.. k..
#     e___
#         r_ 'other'
#
# ? 'a' ? 'A' ? '!' ? ' '
#
# print('#' * 52 + ' This approach is easier to extend without having a lot of `elif` statements,'
#                  ' but for a few categories, I find the first implementation much clearer to read and understand. ')
#
# categories _
# ___ c __ text
#     key = c.. ?
#     i_ k..
#         ?.s_d_ k.. se. .ad. ?
#
# ___ cat __ c..
#     print(_* cat| :', ''.j.. ca.. c..
#
#
# print('#' * 52 + ' We could also do it this way, creating a categories dictionary that has all the individual'
#                  ' characters we are interested __:  ')
#
# f___ it__ ____ cha..
#
# ___ cat_key c
#     cat_1 _ ' ': None
#     cat_2 = di...f_k_ str__.a_l_, 'lower'
#     cat_3 = di...f_k_ str__.a_u_, 'upper'
#     categories _ di.. ch..  _1.it.. _2.it.. _3.it..
#     # categories = {**cat_1, **cat_2, **cat_3} - I'll explain this later
#     r_ c__.ge ? 'other'
#
# ? 'a' ? 'A' ? '!' ? ' '
#
# categories _
# ___ c __ text
#     key _ c.. ?
#     i_ ?
#         ca__.s_d_ ? se. .a.. ?
#
# ___ cat __ categories
#     print(_* ? :', ''.j.. ca.. c..
#
# print('#' * 52 + '  #### Clearing All Items ')
# print('#' * 52 + ' If we want to remove all the keys __ a dictionary, we can use the `clear` method: ')
#
# d = {'a': 1, 'b': 2, 'c': 3}
# print(d)
# d.clear()
# print(d)
