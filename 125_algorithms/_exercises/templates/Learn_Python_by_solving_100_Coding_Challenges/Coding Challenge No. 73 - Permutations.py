# Permutations
# Question: Given a collection of distinct numbers, return all possible permutations.
# For example:
# [1,2,3] have the following permutations:
# [ [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1] ]
# Solutions:


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num) == 0:
            return []
        if len(num) == 1:
            return [num]
        res = []
        for i in range(len(num)):
            for j in self.permute(num[:i] + num[i+1:]):
                res.append([num[i]] + j)
        return res


Solution().permute([1,2,3])