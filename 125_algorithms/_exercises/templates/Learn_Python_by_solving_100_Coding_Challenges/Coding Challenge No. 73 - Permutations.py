# Permutations
# Question: Given a collection of distinct numbers, return all possible permutations.
# For example:
# [1,2,3] have the following permutations:
# [ [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1] ]
# Solutions:


c_ Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    ___ permute , num:
        __ le. num __ 0:
            r_   # list
        __ le. num __ 1:
            r_ [num]
        res _   # list
        ___ i __ ra.. le. num:
            ___ j __ permute num[:i] + num[i+1:]:
                res.ap.. [num[i]] + j
        r_ res


Solution .permute [1,2,3]