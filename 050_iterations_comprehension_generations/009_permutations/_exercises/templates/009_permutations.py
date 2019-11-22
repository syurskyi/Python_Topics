# # Permutations
# # In mathematics, the notion of permutation relates to the act of arranging all the members of a set into some sequence
# # or order, or if the set is already ordered, rearranging (reordering) its elements, a process called permuting.
# # These differ from combinations, which are selections of some members of a set where order is disregarded.
# # We can create permutations of length n from an iterable of length m (n <= m) using the permutation function:
# # As you can see all the permutations are, by default, the same length as the original iterable.
# # We can create permutations of smaller length by specifying the r value:
# # The important thing to note is that elements are not 'repeated' in the permutation.
# # But the uniqueness of an element is not based on its value, but rather on its position in the original iterable.
# # This means that the following will yield what looks like the same permutations when considering the values of
# # the iterable:
#
# l1 = 'abc'
# l___ it__.per__ l1
#
# l___ it__.per__ l1 2
#
# l___ it__.per__ aaa
#
# l___ it__.per__ aba 2
#
# # Combinations
# # Combinations refer to the combination of n things taken k at a time without repetition. To refer to combinations in
# # which repetition is allowed, the terms k-selection,[1] k-multiset,[2] or k-combination with repetition are often used.
# # itertools offers both flavors - with and without replacement.
# # Let's look at a simple example with replacement first:
# # As you can see (4, 3) is not included in the result since, as a combination, it is the same as (3, 4) -
# # order is not important.
#
# l___ it__.com__ 1 2 3 4|, 2
#
# l___ it__.com.._w.._r.. 1 2 3 4|, 2
