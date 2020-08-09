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
            r_ []
        result = []
        elem = []
        self.helper(nums, elem, 0, result)
        r_ result
    
    ___ helper(self, nums, elem, start, result
        result.append(list(elem))
        ___ i in range(start, le.(nums)):
            elem.append(nums[i])
            self.helper(nums, elem, i+1, result)
            elem.pop()
    
    ___ test(self
        testCases = [
            [1, 2, 3],
        ]
        ___ nums in testCases:
            print('nums: %s' % (nums))
            result = self.subsets(nums)
            print('result: %s' % (result))
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()
