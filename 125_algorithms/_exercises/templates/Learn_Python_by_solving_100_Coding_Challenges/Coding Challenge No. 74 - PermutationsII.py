# Permutations II
# Question: Given a collection of numbers that might contain duplicates, return all possible unique permutations.
# For example:
# [1,1,2] have the following unique permutations:
# [ [1,1,2], [1,2,1], [2,1,1] ]
# Solutions:


c_ Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    ___ permuteUnique , num:
        length _ le. num
        __ length __ 0:
            r_   # list
        __ length __ 1:
            r_ [num]
        num.s..
        res _   # list
        previousNum _ N..
        ___ i __ ra.. length:
            __ num[i] __ previousNum:
                c..
            previousNum _ num[i]
        ___ j __ permuteUnique num[:i] + num[i+1:]:
            res.ap.. [num[i]] + j
        r_ res


Solution .permuteUnique [1,1,2]