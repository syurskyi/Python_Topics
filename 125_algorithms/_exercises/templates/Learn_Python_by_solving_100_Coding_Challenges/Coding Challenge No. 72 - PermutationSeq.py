# Permutation Sequence
# Question: The set [1, 2, 3, …, n] contains a total of n! unique permutations.
# By listing and labelling all of the permutations in order. We get the following sequence (i.e., for n = 3): "123“; "132“; "213“; "231“; "312“; "321"
# Given n and k, return the kth permutation sequence.
# Note: Given n will be between 1 and 9 inclusive
# Solutions:


c_ Solution:
    # @param n,k: integers with 1 <= n <= 9
    # @return a string
    ___ getPermutation(self, n, k):
        res _ ''
        k -_ 1
        fac _ 1
        ___ i __ ra..(1, n): fac *_ i
        num _ [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ___ i __ reversed(ra..(n)):
            curr _ num[in.(k/fac)]
            res +_ st.(curr)
            num.r..(curr)
            __ i !_0:
                k %_ fac
                fac /_ i
        r_ res


Solution().getPermutation(3,6)