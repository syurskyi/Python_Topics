"""
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
"""
__author__ = 'Danyang'
class Solution:
    ___ permute(self, num):
        """
        Catalan
        :param num: a list of integer
        :return: a list of lists of integers
        """
        result = []
        self.get_permute(num, [], result)
        return result

    ___ get_permute(self, seq, current, result):
        length = len(seq)
        __ length==0:
            result.append(current)

        for ind, val in enumerate(seq):
            # try:
            self.get_permute(seq[:ind]+seq[ind+1:], current+[val], result)  # list(current).append(val) is side-effect
            # except IndexError:
            #     self.get_permute(seq[:ind], current+[val], result)
            # array slice out of index will return []

__ __name__=="__main__":
    print Solution().permute([1, 2, 3])