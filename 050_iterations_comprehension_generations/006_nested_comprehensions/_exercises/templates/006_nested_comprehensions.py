# # Nested Comprehensions
# # Just as with list comprehensions, we can nest generator expressions too:
# # A multiplication table:
# # Using a list comprehension approach first:
# # The equivalent generator expression would be:
# # We can iterate through mult_list:
# # But you'll notice that our rows are themselves generators!
# # o fully materialize the table we need to iterate through the row generators too:
#
# start _ 1
# stop _ 10
#
# mult_list _ i * j
#                ___ j i_ r___ s.. s..+1
#              ___ i i_ r___ s.. s..+1     # lIST
#
# mult_list
#
# start _ 1
# stop _ 10
#
# mult_list _ i * j
#                ___ j i_ r___ s.. s...+1
#              ___ i i_ r___ s... s..+1     tUPLE OR SET
#
# mult_list
#
# table _ l__ m.._l..
# table
#
# table_rows _  l__ gen ___ gen i_ t..   # List
# table_rows
#
# # Nested Comprehensions
# # Of course, we can mix list comprehensions and generators.
# # In this modification, we'll make the rows list comprehensions, and retain the generator expression in the outer
# # comprehension:
# # Notice what is happening here, the table itself is lazy evaluated, i.e. the rows are not yielded until they
# # are requested - but once a row is requested, the list comprehension that defines the row will be entirely
# # evaluated at that point:
#
# start _ 1
# stop _ 10
#
# mult_list _ i * j
#                ___ j i_ r__ s.. s..+1
#              ___ i i_ r__ s.. s..+1
#
# ___ item i_ m.._l..
#     print i...
#
# # Let's try Pascal's triangle again:
# # Here's how we did it using a list comprehension:
#
# f... ma.. _______ fa...
#
# ___ combo n k
#     r_ fac... n // fac... k * fac... n-k
#
# size _ 10  # global variable
# pascal _ combo n k ___ k i_ r___ n+1 ___ n i_ r____ s...+1
#
# # Let's try Pascal's triangle again:
# #
# # If we want to materialize the triangle into a list we'll need to do so ourselves:
#
# size _ 10  # global variable
# pascal _ combo n k ___ k i_ r___ n+1 ___ n i_ r___ s...+1
#
# l__ row ___ r.. i_ p...
