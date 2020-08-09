"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""
__author__ = 'Danyang'
class Solution:
    ___ permuteUnique_TLE(self, num
        """
        list to set
        Time Limit Exceeded
        :param num: a list of integer
        :return: a list of lists of integers
        """
        result = []
        self.get_permute(num, [], result)
        r_ map(list, set(map(tuple, result)))


    ___ get_permute_TLE(self, nums, current, result
        length = le.(nums)
        __ length__0:
            result.append(current)

        ___ ind, val in enumerate(nums
            self.get_permute(nums[:ind]+nums[ind+1:], current+[val], result)


    ___ permuteUnique(self, num
        """
        Jump
        compared to 045 Permutation, two lines added: sort and continue
        :param num: a list of integer
        :return: a list of lists of integers
        """
        result = []
        num.sort()
        self.get_permute(num, [], result)
        r_ result

    ___ get_permute(self, nums, current, result
        __ not nums:
            result.append(current)

        ___ ind, val in enumerate(nums
            __ ind-1>=0 and val__nums[ind-1]: continue  # JUMP; only need to compare to previous value
            self.get_permute(nums[:ind]+nums[ind+1:], current+[val], result)

__ __name____"__main__":
    print Solution().permuteUnique([1, 1, 2])