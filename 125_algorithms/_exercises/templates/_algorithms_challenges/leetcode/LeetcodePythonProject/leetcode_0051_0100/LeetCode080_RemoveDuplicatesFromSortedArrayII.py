'''
Created on Jan 24, 2017

@author: MT
'''

class Solution(object
    ___ removeDuplicates(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ le.(nums) <= 2:
            r_ le.(nums)
        prev, curr = 1, 2
        w___ curr < le.(nums
            __ nums[curr] != nums[prev] or nums[curr] != nums[prev-1]:
                prev += 1
                nums[prev] = nums[curr]
            curr += 1
        r_ prev + 1
    
    ___ test(self
        pass

__ __name__ __ '__main__':
    Solution().test()
