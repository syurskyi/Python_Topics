# # Yielding and Generators
# # create def squares (sentinel) :
# # without error
#
# ___ squares sentinel
#     i _ 0
#     w___ T_
#         __ ? < ?
#             y___ ?**2
#             ? +_ 1 # note how we can incremenet **after** the yield
#         ____
#             r_ 'all done!'
#
# num
# ___ ? __ ? 5
#     print ?
#
# # Yielding and Generators
# #
# # So now let's see how we could re-write our initial factorial example:
#
# import math
# # i
# ___ factorials n
#     ___ ? __ ra__ ?
#         y___ ma__.fac... ?
#
# # num
# ___ ? __ f.. 5
#     print ?
#
# facts _ ? 5
# li.. ?
# li.. ?
# ne.. ?  # error
#
# # Making an Iterable from a Generator
# # As we now know, generators are iterators.
# # This means that they become exhausted - so sometimes we want to create an iterable instead.
# # But, sq was an iterator - so now it's been exhausted:
# # To restart the iteration we have to create a new instance of the generator  iterator :
#
# # i
# ___ squares_gen n
#     ___ ? __ ra... ?
#         y___ ? ** 2
#
# sq _ ? 5
#
# # num
# ___ ? __ ?
#     print ?
#
# ne.. ?
#
# sq _ ? 5
# ? ___ ? __ ?   # list comprehension
#
# # Generators used with other Generators
# # Now enumerate is lazy, so sq had not, at this point, been consumed:
# # Since we have consumed two elements from sq, when we now use enumerate it will have two less elements from sq:
#
# # i
# ___ squares n
#     ___ ? __ ra... ?
#         y___ ? ** 2
#
# sq _ ? 5
# enum_sq _ en... ?
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
# # i
# l _  ? ** 2 ___ ? __ ra... 5  # list comprehension
# l
# # The expression inside the [] brackets is called a comprehension expression.
#
# g _  ? ** 2 ___ ? __ ra... 5  # comprehension expression
#
# ty.. ?
#
# item
# ___ ? __ ?
#     print ?
#
# # Generator Expressions
# #
# # We can iterate over the same li.. comprehension multiple times, since it is an iterable.
# # However, we can only iterate over a comprehension expression once, since it is an iterator.
#
# # i
# l _ ? * 2 ___ ? __ ra... 5  # list comprehension
# ty.. ?
#
# g _  ? ** 2 ___ ? __ ra... 5  # comprehension expression
# ty.. ?