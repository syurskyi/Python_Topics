# -*- coding: utf-8 -*-

# # The range Iterable
# R _ r___ 10
# # range returns an iterator, not a list
# print(R)
# I = i___ R
# # Make an iterator from the range
# print n___ I  # Advance to next result
# print n___ I
# print n___ I
# print l__ r___ 10  # To force a list if required
#
# print le. R  # range also does len and indexing, but no others
# print R |0
# print R |-1
#
# print n___ I  # Continue taking from iterator, where left off
# print I. -n  # .next() becomes .__next__(), but use new next()
#
# # The map  Iterable
# M _ ? ab. |-1 0 1  # map returns an iterator, not a list
# print(M)
#
# print n___ M  # Use iterator manually: exhausts results. hese do not support len() or indexing
#
# print n___ M
#
# print n___ M
#
# # print(next(M))
#
# ___ x __ M print x  # map iterator is now empty: one pass only
#
# M = ma. ab. |-1 0 1  # Make a new iterator to scan again
#
# ___ x __ M print x  # Iteration contexts auto call next()
#
# print l___ ma. ab. |-1 0 1  # Can force a real list if needed
#
# # The zip Iterables
# Z _ z__ 1 2 3| 10 20 30  # zip is the same: a one-pass iterator
#
# print(Z)
#
# print l___ Z
#
# ___ pair __ Z print p...  # Exhausted after one pass
#
# Z _ z.. 1 2 3| 10 20 30
#
# ___ pair __ Z print p..  # Iterator used automatically or manually
#
# Z = z__ 2 3| 10 20 30
# print n___ Z
# print n___ Z
#
# # The filter Iterables
# print(? bo.. |'spam' '' 'ni
# print(l___ ? bo.. |'spam' '' 'ni'
#
# # Multiple Versus Single Pass Iterators
# # Range
#
# R _ ? 3  # range allows multiple iterators
#
# # print(next(R))                       # TypeError: range object is not an iterator
#
# I1 _ i___ R
# print n___ I1
# print n___ I1
#
# I2 _ i___ R # Two iterators on one range
# print n___ I2
#
# print n___ I1  # I1 is at a different spot than I2
#
# R _ r___ 3  # But range allows many iterators
# I1; I2 _ i___ R; i___ R
# print n___ I1 ; n___ I1 ; n___ I1
#
# print n___ I2  # Multiple active scans, like 2.X lists
#
# # Multiple Versus Single Pass Iterators
# # Zip
#
# Z = ? 1 2 3|; 10 11 12
#
# I1 _ i___ Z
# I2 _ i___ Z # Two iterators on one zip
#
# print n___ I1
# print n___ I1
#
# print n___ I2  # I2 is at same spot as I1!
#
# # Multiple Versus Single Pass Iterators
# # Map
#
# M _ ? ab. |-1 0 1  # Ditto for map (and filter)
# I1 _ i___ M
# I2 _ i___ M
# print n___ I1 ; n___ I1 ; n___ I1
#
# # next(I2)                              # (3.X) Single scan is exhausted! StopIteration
