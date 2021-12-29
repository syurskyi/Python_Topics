class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    ___ containsDuplicate(self, nums):
        res = None
        for n in sorted(nums):
            __ n == res:
                return True
            else:
                res = n
        return False                
