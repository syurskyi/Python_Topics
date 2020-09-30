'''
Created on Jan 24, 2017

@author: MT
'''

class Solution(object
    ___ subsets(self, nums
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        __ not nums:
            r_   # list
        result =   # list
        elem =   # list
        self.helper(nums, elem, 0, result)
        r_ result
    
    ___ helper(self, nums, elem, start, result
        result.append(list(elem))
        ___ i __ range(start, le.(nums)):
            elem.append(nums[i])
            self.helper(nums, elem, i+1, result)
            elem.p..
    
    ___ test(self
        testCases = [
            [1, 2, 3],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            result = self.subsets(nums)
            print('result: %s' % (result))
            print('-='*15+'-')

__  -n __ '__main__':
    Solution().test()
