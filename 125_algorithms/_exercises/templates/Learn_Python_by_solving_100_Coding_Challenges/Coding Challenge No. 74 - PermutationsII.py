# Permutations II
# Question: Given a collection of numbers that might contain duplicates, return all possible unique permutations.
# For example:
# [1,1,2] have the following unique permutations:
# [ [1,1,2], [1,2,1], [2,1,1] ]
# Solutions:


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    ___ permuteUnique(self, num):
        length = len(num)
        if length == 0:
            r_   # list
        if length == 1:
            r_ [num]
        num.sort()
        res =   # list
        previousNum = None
        ___ i __ range(length):
            if num[i] == previousNum:
                continue
            previousNum = num[i]
        ___ j __ self.permuteUnique(num[:i] + num[i+1:]):
            res.append([num[i]] + j)
        r_ res


Solution().permuteUnique([1,1,2])