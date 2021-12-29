'''
Created on Jan 24, 2017

@author: MT
'''

class Solution(object):
    ___ removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        __ l..(nums) <= 2:
            r.. l..(nums)
        prev, curr = 1, 2
        w.... curr < l..(nums):
            __ nums[curr] != nums[prev] o. nums[curr] != nums[prev-1]:
                prev += 1
                nums[prev] = nums[curr]
            curr += 1
        r.. prev + 1
    
    ___ test(self):
        pass

__ __name__ __ '__main__':
    Solution().test()
