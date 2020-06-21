# # Yielding and Generators
# # create def squares (sentinel) :
# # without error
#
# ___ squares sentinel
#     i _ 0
#     w___ T_
#         i_ i < sentinel
#             y___ i**2
#             i +_ 1 # note how we can incremenet **after** the yield
#         e___
#             r_ 'all done!'
#
# ___ num i_ squares 5 :
#     print n..
#
# # Yielding and Generators
# #
# # So now let's see how we could re-write our initial factorial example:
#
# ___ factorials n
#     ___ i i_ range n
#         y___ ma__.fac... i
#
# ___ num i_ factorials 5 :
#     print n..
#
# facts _ factorials 5
# li.. f...
# li.. f...
# ne.. f...  # error
#
# # Making an Iterable from a Generator
# #
# # As we now know, generators are iterators.
# # This means that they become exhausted - so sometimes we want to create an iterable instead.
# #
# # But, sq was an iterator - so now it's been exhausted:
# #
# # To restart the iteration we have to create a new instance of the generator  iterator :
#
# ___ squares_gen n
#     ___ i i_ ra... n
#         y___ i ** 2
#
# sq _ squares_gen 5
#
# ___ num i_ sq
#     print n..
#
# ne.. sq
#
# sq _ squares_gen 5
# num ___ num i_ sq
#
# # Generators used with other Generators
# # Now enumerate is lazy, so sq had not, at this point, been consumed:
# #
# # Since we have consumed two elements from sq, when we now use enumerate it will have two less elements from sq:
#
# ___ squares n
#     ___ i i_ ra... n
#         y___ i ** 2
#
# sq _ squares 5
# enum_sq _ en... sq
#
# ne.. sq
# ne.. sq
#
# ne.. enum_sq
#
# # Generator Expressions
# # Recall how li.. comprehensions worked:
# # We can easily create a generator by using    parentheses instead of the [] brackets:
# # Note that g is a generator, and is also lazily evaluated:
#
# l _  i ** 2 ___ i i_ ra... 5
# l
# # The expression inside the [] brackets is called a comprehension expression.
#
# g _  i ** 2 ___ i i_ ra... 5
#
# ty.. g
#
# ___ item i_ g
#     print i...
#
# # Generator Expressions
# #
# # We can iterate over the same li.. comprehension multiple times, since it is an iterable.
# # However, we can only iterate over a comprehension expression once, since it is an iterator.
#
# l _ i * 2 ___ i i_ ra... 5
# ty.. l
#
# g _  i ** 2 ___ i i_ ra... 5
# ty.. g