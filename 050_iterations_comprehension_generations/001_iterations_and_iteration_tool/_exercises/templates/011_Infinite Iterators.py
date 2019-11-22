# # Infinite Iterators
# # The count function is similar to range, except it does not have a stop value. It has both a start and a step:
# #
# # Unlike the range function, whose arguments must always be integers, count works with floats as well:
# #
# # In fact, we can even use other data types as well:
# #
# # We can even use Decimal numbers:
#
# f___ it___ _______ co__
# g _ co__ 10
# li__ isl__ g 5
# g _ co__ 10, step_2
# li__ isl__ g 5
#
# g _ co__ 10.5 0.5
# li__ isl__ g 5
#
# g _ co__ 1+1j 1+2j
# li__ isl__ g 5
#
# f___ dec... _______ D....
# g _ co__ D.... 0.0 Decimal 0.1
# li__ isl__ g 5
#
# # Infinite Iterators
# # cycle is used to repeatedly loop over an iterable:
# #
# # One thing to note is that this works even if the argument is an iterator
# # (i.e. gets exhausted after the first complete iteration over it)!
# #
# # As expected, cols was exhausted after the first iteration.
# # Now let's see how cycle behaves:
# #
# # As you can see, cycle iterated over the elements of iterator, and continued the iteration even though the first run
# # through the iterator technically exhausted it.
#
# g _ cycle 'red' 'green' 'blue'
# li__ isl__ g 8
#
# ___ colors
#     y___ 'red'
#     y___ 'green'
#     y___ 'blue'
#
# cols _ c...
# li__ c..
# li__ c..
#
# cols _ c..
# g _ c... c..
# li__ isl__ g 10
#
# # Infinite Iterators
# # The repeat function is used to create an iterator that just returns the same value again and again.
# # By default it is infinite, but a count can be specified optionally:
# #
# # And we also optionally specify a count to make the iterator finite:
# #
# # The important thing to note as well, is that the "value" that is returned is the same object every time!
#
# g _ repeat Python
# ___ _ i_ ra__ 5
#     print ne__ g
#
# g _ repeat 'Python' 4
# li__ g
#
# l _  1 2 3  # list
# result _ li__(repeat l 3
# r...
#
# l i_ r...|0 l i_ r...|1 l i_ r...|2
#
# # Infinite Iterators
# # repeat
# #
# # If you want to end up with three separate copies of your argument, then you'll need to use a copy mechanism
# # (either shallow or deep depending on your needs).
# #
# # This is easily done using a comprehension expression:
#
# l _ 1 2 3   # list
# result _ |item|:| ___ i.. i_ repeat l, 3
# l i_ r...|0 l i_ r...|1 l i_ r...|2
# r...|0|| 0| _ 100
# r...
