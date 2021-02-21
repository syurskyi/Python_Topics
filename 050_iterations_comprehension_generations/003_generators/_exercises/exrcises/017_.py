# # Let's take a look at a more interesting example of yield from.
# # Our goal is to flatten a  l... containing nested lists to any level.
# # And of course we can, i_. we prefer, make a  l... out of it:
#
# l _ [1, 2, [3, 4, [5, 6]], [7, [8, 9, 10]]]
#
# ___ flatten_gen curr_item
#     i_. isi... curr_item  l...
#         ___ item i_ curr_item
#             y___ from f....
#     e___
#         y___ c.._i..
#
# ___ item i_ f.._g.. l :
#     print i...
#
#  l... f.._g.. l
#
# # Our goal is to flatten a  list containing nested lists to any level.
# # Why are we getting this recursion error?
# # That's because strings are iterables too - even a single character string!
# # So, two issues: we may not want to treat strings as iterables, and if. we do, then we need to be careful with single
# # character strings.
# # We're going to tweak our is_iterable function, and our flatten generator to handle these two issues:
# # Let's just make sure our function works as expected:
# # Good, now we can tweak our flatten generator so we can tell it whether to handle strings as iterables or not:
#
# l _ [1, 2, [3, 4, [5, 6]], [7, [8, 9, 10]]]
#
# ___ is_iterable item * s.._i._i.. _ T...
#     t__
#         it.. item
#     e...
#         r_ F...
#     e___:
#         i_. isi... item st.
#             i_. s.._i._i. an. le. it..  > 1
#                 r_ T...
#             e___:
#                 r_ F...
#         e___:
#             r_ T...
#
# print i.....  1 2 3
# print i..... 'abc'
# print i..... 'a'
#
# print i..... [1, 2, 3], s.._i._i. _ F...
# print i..... 'abc', s.._i._i. _ F...
# print i..... 'a', s.._i._i. _ F...
#
# ___ flatten_gen curr_item * str_is_iterable _ T...
#     i_. i..... c.._i.. s.._i._iterable_str_is_iterable :
#         ___ item i_ curr_item
#             y___ from flatten_gen item, str_is_iterable_str_is_iterable
#     e___:
#         y___ c.._i..
#
# llist flatten_gen l
#  l... flatten_gen l, s.._i._i... _ F..
#
# # we saw we could use yield from recursively. in fact a generator can be both a delegator and a subgenerator.
# # Here's a simple example of this:
#
# ___ coro
#     w____ T...:
#         received _ y___
#         print r...
#
#
# ___ gen1
#     y___ f.. g..2
#
#
# ___ gen2
#     y___ f.. g..3
#
#
# ___ gen3
#     y___ f.. c...
#
#
# g _ gen1
# ne.. g
#
# g.se.. 'hello'
