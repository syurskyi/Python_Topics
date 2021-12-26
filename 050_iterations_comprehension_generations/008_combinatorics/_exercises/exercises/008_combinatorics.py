# # Combinatorics
# # Cartesian Product
# # The cartesian product is actually a lot more useful than it might appear at first.
# # Consider this example, where we want to create a multiplication table as we have seen before:
# # We can look at a few elements using islice:
# # So, the Cartesian product of two iterables in general can be generated using a nested loop:
# # We can achieve the same result with the product function in itertools. As usual, it is lazy as well.
#
# ___ matrix n
#     ___ i i_ r___ 1 n+1
#         ___ j i_ r___ 1 n+1
#             y___ _*|i| x |j| _ |i*j|*
#
# l___ it___.is... matrix 10; 10 20
#
# l1 _ 'x1' 'x2' 'x3' 'x4'
# l2 _ 'y1' 'y2' 'y3'
# ___ x i_ l1
#     ___ y i_ l2:
#         printx y| e.._' '
#     print('')
#
# l1 _ 'x1' 'x2' 'x3' 'x4'
# l2 _ 'y1' 'y2' 'y3'
# l___ it___.pr... l1 l2
#
# # Combinatorics
# # Cartesian Product
# # As a simple example, let's go back to the multiplication table we created using a generator function.
# # And of course this is now simple enough to even use just a generator expression:
#
# ___ matrix n
#     ___ i i_ r___  1 n+1
#         ___ j i_ r___ 1 n+1
#             y___ i j i*j
#
# l___ matrix 4
#
# ___ matrix n
#     ___ i, j i_ it___.pr.. r___ 1 n+1  r___ 1 n+1
#         y___ i j i*j
#
# l___ matrix 4
#
# ___ matrix n
#     r_ i j i*j
#             ___ i, j i_ it___.pr.. r.. 1 n+1 r.. 1 n+1
#
# l___ matrix 4
#
#
# # Combinatorics
# # Cartesian Product
# #
# # You'll notice how we repeated the range(1, n+1) twice?
# #
# # This is a great example of where tee can be useful:
#
# from itertools import tee
#
# ___ matrix n
#     r_ i j i*j
#             ___ i j i_ it___.pr..*it___.te. r.. 1 n+1 2
#
# l___ matrix 4
#
# # A common usage of Cartesian products might be to generate a grid of coordinates.
# # For a 2D space for example, we might want to generate a grid of points ranging from -5 to 5 in both the x and y axes,
# # with a step of 0.5.
# # We can't use a range since ranges need integral numbers,
# # but we have the count function in itertools we have seen before:
# # And of course we can now do it in 3D as well:
#
# ___ grid min_val max_val step * num_dimensions_2
#     axis _ it___.tak... l______ x x <_ m.._v..
#                                it___.count(m.._v.., s..
#
#     # to handle multiple dimensions, we just need to repeat the axis that
#     # many times - tee is perfect for that
#     axes = it___.te. ax.. n.._d..
#
#     # and now we just need the product of all these iterables
#     r_ it___.pr.. *a..
#
#
# l___ g... -1 1 0.5
#
# l___ g... -1 1 0.5 num_dimensions_3
#
# # Another simple application of this might be to determine the odds of rolling an 8 with a pair of dice
# # (with values 1 - 6).
# # We can brute force this by generating all the possible results (the sample space),
# # and counting how may items add up to 8.
# # Now we want to filter out the tuples whose elements add up to 8:
# # And we can calculate the odds by dividing the number acceptable outcomes by the size of the sample space.
# # I'll actually use a Fraction so we retain our result as a rational number:
#
# sample_space _ l___ it___.pr.. r___ 1, 7 r___ 1, 7
# print s...
#
# outcomes _ l___ f... l____ x x|0| + x|1 __ 8 s...
# print(outcomes)
#
# f... f... _______ Fr..
# odds _ Fr.. le. o.. le. s.._s..
# print o..
