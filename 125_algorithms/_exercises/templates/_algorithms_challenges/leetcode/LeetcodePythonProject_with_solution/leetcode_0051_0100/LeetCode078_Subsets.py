'''
Created on Jan 24, 2017

@author: MT
'''

class Solution(object):
    ___ subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        __ not nums:
            return []
        result = []
        elem = []
        self.helper(nums, elem, 0, result)
        return result
    
    ___ helper(self, nums, elem, start, result):
        result.append(list(elem))
        for i in range(start, len(nums)):
            elem.append(nums[i])
            self.helper(nums, elem, i+1, result)
            elem.pop()
    
    ___ test(self):
        testCases = [
            [1, 2, 3],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.subsets(nums)
            print('result: %s' % (result))
            print('-='*15+'-')

__ __name__ == '__main__':
    Solution().test()
