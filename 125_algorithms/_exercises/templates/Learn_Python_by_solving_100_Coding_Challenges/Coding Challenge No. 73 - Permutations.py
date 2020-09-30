# Permutations
# Question: Given a collection of distinct numbers, return all possible permutations.
# For example:
# [1,2,3] have the following permutations:
# [ [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1] ]
# Solutions:


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    ___ permute(self, num):
        if len(num) == 0:
            r_   # list
        if len(num) == 1:
            r_ [num]
        res =   # list
        ___ i __ range(len(num)):
            ___ j __ self.permute(num[:i] + num[i+1:]):
                res.append([num[i]] + j)
        r_ res


Solution().permute([1,2,3])